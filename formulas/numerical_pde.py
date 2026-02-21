# formulas/numerical_pde.py
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from .math_tools import SYMPY_FUNCS
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application
)
TRANSFORMATIONS = standard_transformations + (implicit_multiplication_application,)


def _parse_func(expr_str: str, x_sym: sp.Symbol, local_extra=None):
    expr_str = (expr_str or "").strip()
    if expr_str == "":
        expr_str = "0"
    expr_str = expr_str.replace("^", "**")
    local_dict = {"x": x_sym}
    local_dict.update(SYMPY_FUNCS)
    if local_extra:
        local_dict.update(local_extra)
    f_expr = parse_expr(expr_str, local_dict=local_dict, transformations=TRANSFORMATIONS)
    f = sp.lambdify(x_sym, f_expr, modules=["numpy"])
    return f_expr, f


def _tri_solve(a, b, c, d):
    """
    Thomas algorithm for tridiagonal system.
    a: subdiag (n-1), b: diag (n), c: superdiag (n-1), d: rhs (n)
    """
    n = len(b)
    cp = np.zeros(n-1, dtype=float)
    dp = np.zeros(n, dtype=float)

    cp[0] = c[0] / b[0]
    dp[0] = d[0] / b[0]

    for i in range(1, n-1):
        denom = b[i] - a[i-1] * cp[i-1]
        cp[i] = c[i] / denom
        dp[i] = (d[i] - a[i-1] * dp[i-1]) / denom

    dp[n-1] = (d[n-1] - a[n-2] * dp[n-2]) / (b[n-1] - a[n-2] * cp[n-2])

    x = np.zeros(n, dtype=float)
    x[n-1] = dp[n-1]
    for i in range(n-2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i+1]
    return x


# -----------------------------
# HEAT: u_t = k u_xx  (Crank–Nicolson)
# BC Dirichlet: u(0,t)=0, u(L,t)=0
# IC: u(x,0)=f0(x)
# -----------------------------
def heat_cn_dirichlet_animate(vars):
    L = float(sp.N(vars.get("L") or np.pi))
    kappa = float(sp.N(vars.get("k") or 1.0))

    Nx = int(vars.get("Nx") or 201)     # grid points
    dt = float(vars.get("dt") or 0.001)
    frames = int(vars.get("frames") or 240)
    steps_per_frame = int(vars.get("spf") or 5)

    f0_str = (vars.get("f0") or "").strip()
    if f0_str == "":
        f0_str = "sin(pi*x/L)"

    x = np.linspace(0.0, L, Nx)
    dx = x[1] - x[0]

    xsym = sp.Symbol("x", real=True)
    f0_expr, f0 = _parse_func(f0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})

    u = np.array(f0(x), dtype=float)
    if u.ndim == 0:  # scalar -> broadcast to array
        u = np.full_like(x, float(u), dtype=float)

    # apply Dirichlet
    u[0] = 0.0
    u[-1] = 0.0

    r = kappa * dt / (dx * dx)

    # interior size
    n = Nx - 2  # indices 1..Nx-2

    # (I - r/2 A) u^{n+1} = (I + r/2 A) u^n
    # A is second-diff: [-2,1,1]
    a = - (r/2) * np.ones(n-1)      # subdiag
    b = (1 + r) * np.ones(n)        # diag
    c = - (r/2) * np.ones(n-1)      # superdiag

    # RHS operator
    aR = (r/2) * np.ones(n-1)
    bR = (1 - r) * np.ones(n)
    cR = (r/2) * np.ones(n-1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    line, = ax.plot(x, u)
    ax.set_title("Heat Equation (Crank–Nicolson, Dirichlet)")
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")

    t_now = 0.0

    def step(u):
        # build RHS for interior
        ui = u[1:-1]
        rhs = bR * ui
        rhs[1:] += aR * ui[:-1]
        rhs[:-1] += cR * ui[1:]

        # boundaries are zero -> no extra terms
        ui_next = _tri_solve(a, b, c, rhs)

        u2 = u.copy()
        u2[1:-1] = ui_next
        u2[0] = 0.0
        u2[-1] = 0.0
        return u2

    def update(frame):
        nonlocal u, t_now
        for _ in range(steps_per_frame):
            u = step(u)
            t_now += dt

        line.set_ydata(u)
        ax.set_title(f"Heat CN Dirichlet | t={t_now:.4f}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()


# -----------------------------
# WAVE: u_tt = c^2 u_xx  (Leapfrog explicit)
# Dirichlet: u(0,t)=0, u(L,t)=0
# IC: u(x,0)=f0(x),  u_t(x,0)=g0(x)
# CFL: c*dt/dx <= 1
# -----------------------------
def wave_leapfrog_dirichlet_animate(vars):
    L = float(sp.N(vars.get("L") or np.pi))
    c = float(sp.N(vars.get("c") or 1.0))

    Nx = int(vars.get("Nx") or 401)
    dt = float(vars.get("dt") or 0.001)
    frames = int(vars.get("frames") or 240)
    steps_per_frame = int(vars.get("spf") or 5)

    f0_str = (vars.get("f0") or "").strip() or "sin(pi*x/L)"
    g0_str = (vars.get("g0") or "").strip() or "0"

    x = np.linspace(0.0, L, Nx)
    dx = x[1] - x[0]

    # CFL check (we'll auto clamp dt if too big)
    lam = c * dt / dx
    if lam > 1.0:
        dt = 0.95 * dx / c
        lam = c * dt / dx

    xsym = sp.Symbol("x", real=True)
    f0_expr, f0 = _parse_func(f0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})
    g0_expr, g0 = _parse_func(g0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})

    u0 = np.array(f0(x), dtype=float)
    v0 = np.array(g0(x), dtype=float)

    if u0.ndim == 0:
        u0 = np.full_like(x, float(u0), dtype=float)
    if v0.ndim == 0:
        v0 = np.full_like(x, float(v0), dtype=float)


    # Dirichlet boundaries
    u0[0] = 0.0
    u0[-1] = 0.0
    v0[0] = 0.0
    v0[-1] = 0.0

    # first step: u^1 = u^0 + dt*v0 + 0.5*(c^2 dt^2)*u_xx^0
    u_xx0 = np.zeros_like(u0)
    u_xx0[1:-1] = (u0[2:] - 2*u0[1:-1] + u0[:-2]) / (dx*dx)

    u1 = u0 + dt * v0 + 0.5 * (c*c) * (dt*dt) * u_xx0
    u1[0] = 0.0
    u1[-1] = 0.0

    u_prev = u0
    u_curr = u1

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    line, = ax.plot(x, u_curr)
    ax.set_title(f"Wave (Leapfrog Dirichlet) | CFL={lam:.3f}")
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")

    t_now = dt

    def step(u_prev, u_curr):
        u_next = np.zeros_like(u_curr)
        u_next[1:-1] = (2*u_curr[1:-1] - u_prev[1:-1] +
                        (lam*lam) * (u_curr[2:] - 2*u_curr[1:-1] + u_curr[:-2]))
        # boundaries
        u_next[0] = 0.0
        u_next[-1] = 0.0
        return u_curr, u_next

    def update(frame):
        nonlocal u_prev, u_curr, t_now
        for _ in range(steps_per_frame):
            u_prev, u_curr = step(u_prev, u_curr)
            t_now += dt

        line.set_ydata(u_curr)
        ax.set_title(f"Wave Leapfrog Dirichlet | t={t_now:.4f} | CFL={lam:.3f}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()

def heat_cn_neumann_animate(vars):
    # u_t = k u_xx, 0<x<L
    # u_x(0,t)=0, u_x(L,t)=0
    L = float(sp.N(vars.get("L") or np.pi))
    kappa = float(sp.N(vars.get("k") or 1.0))

    Nx = int(vars.get("Nx") or 201)
    dt = float(vars.get("dt") or 0.001)
    frames = int(vars.get("frames") or 240)
    steps_per_frame = int(vars.get("spf") or 5)

    f0_str = (vars.get("f0") or "").strip() or "cos(pi*x/L)"

    x = np.linspace(0.0, L, Nx)
    dx = x[1] - x[0]

    xsym = sp.Symbol("x", real=True)
    f0_expr, f0 = _parse_func(f0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})
    u = np.array(f0(x), dtype=float)
    if u.ndim == 0:
        u = np.full_like(x, float(u), dtype=float)

    r = kappa * dt / (dx * dx)

    # Unknowns include boundaries now: size Nx
    n = Nx

    # Build tridiagonal for (I - r/2 A)
    a = np.zeros(n-1)
    b = np.ones(n)
    c = np.zeros(n-1)

    # Interior rows i=1..n-2
    for i in range(1, n-1):
        a[i-1] = -r/2
        b[i] = 1 + r
        c[i] = -r/2

    # Neumann left: u_x(0)=0 => u_-1 = u_1, so u_xx(0) = 2(u1-u0)/dx^2
    # Row 0 for CN: (I - r/2 A) with A0: [-2, +2]
    b[0] = 1 + r
    c[0] = -r

    # Neumann right: u_x(L)=0 => u_{n} = u_{n-2}, so u_xx(n-1)=2(u_{n-2}-u_{n-1})/dx^2
    a[n-2] = -r
    b[n-1] = 1 + r

    # RHS operator (I + r/2 A)
    aR = np.zeros(n-1)
    bR = np.ones(n)
    cR = np.zeros(n-1)

    for i in range(1, n-1):
        aR[i-1] = r/2
        bR[i] = 1 - r
        cR[i] = r/2

    bR[0] = 1 - r
    cR[0] = r
    aR[n-2] = r
    bR[n-1] = 1 - r

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    line, = ax.plot(x, u)
    ax.set_title("Heat (Crank–Nicolson, Neumann)")
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    t_now = 0.0

    def step(u):
        rhs = bR * u
        rhs[1:] += aR * u[:-1]
        rhs[:-1] += cR * u[1:]
        u_next = _tri_solve(a, b, c, rhs)
        return u_next

    def update(frame):
        nonlocal u, t_now
        for _ in range(steps_per_frame):
            u = step(u)
            t_now += dt
        line.set_ydata(u)
        ax.set_title(f"Heat CN Neumann | t={t_now:.4f}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()


def heat_cn_mixed_animate(vars):
    # u_t = k u_xx, 0<x<L
    # u(0,t)=0, u_x(L,t)=0
    L = float(sp.N(vars.get("L") or np.pi))
    kappa = float(sp.N(vars.get("k") or 1.0))

    Nx = int(vars.get("Nx") or 201)
    dt = float(vars.get("dt") or 0.001)
    frames = int(vars.get("frames") or 240)
    steps_per_frame = int(vars.get("spf") or 5)

    f0_str = (vars.get("f0") or "").strip() or "sin(pi*x/(2*L))"

    x = np.linspace(0.0, L, Nx)
    dx = x[1] - x[0]

    xsym = sp.Symbol("x", real=True)
    f0_expr, f0 = _parse_func(f0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})
    u = np.array(f0(x), dtype=float)
    if u.ndim == 0:
        u = np.full_like(x, float(u), dtype=float)

    # Dirichlet at x=0
    u[0] = 0.0

    r = kappa * dt / (dx * dx)

    # Unknowns include nodes 0..n-1, but node 0 fixed -> we can keep it in system or eliminate.
    # We'll keep full system and hard-enforce u0=0 each step.

    n = Nx
    a = np.zeros(n-1)
    b = np.ones(n)
    c = np.zeros(n-1)

    # Interior i=1..n-2
    for i in range(1, n-1):
        a[i-1] = -r/2
        b[i] = 1 + r
        c[i] = -r/2

    # Dirichlet row 0: u0 = 0
    b[0] = 1.0
    c[0] = 0.0

    # Neumann right at n-1:
    a[n-2] = -r
    b[n-1] = 1 + r

    # RHS
    aR = np.zeros(n-1)
    bR = np.ones(n)
    cR = np.zeros(n-1)

    for i in range(1, n-1):
        aR[i-1] = r/2
        bR[i] = 1 - r
        cR[i] = r/2

    # Dirichlet row 0 RHS -> 0
    bR[0] = 1.0
    cR[0] = 0.0

    # Neumann right RHS row
    aR[n-2] = r
    bR[n-1] = 1 - r

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    line, = ax.plot(x, u)
    ax.set_title("Heat (Crank–Nicolson, Mixed: Dirichlet+Neumann)")
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    t_now = 0.0

    def step(u):
        rhs = bR * u
        rhs[1:] += aR * u[:-1]
        rhs[:-1] += cR * u[1:]

        rhs[0] = 0.0  # enforce Dirichlet
        u_next = _tri_solve(a, b, c, rhs)
        u_next[0] = 0.0
        return u_next

    def update(frame):
        nonlocal u, t_now
        for _ in range(steps_per_frame):
            u = step(u)
            t_now += dt
        line.set_ydata(u)
        ax.set_title(f"Heat CN Mixed | t={t_now:.4f}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()

def wave_leapfrog_neumann_animate(vars):
    # u_tt + 2*beta*u_t = c^2 u_xx
    # u_x(0,t)=0, u_x(L,t)=0
    L = float(sp.N(vars.get("L") or np.pi))
    c = float(sp.N(vars.get("c") or 1.0))
    beta = float(sp.N(vars.get("beta") or 0.0))

    Nx = int(vars.get("Nx") or 401)
    dt = float(vars.get("dt") or 0.001)
    frames = int(vars.get("frames") or 240)
    spf = int(vars.get("spf") or 5)

    f0_str = (vars.get("f0") or "").strip() or "cos(pi*x/L)"
    g0_str = (vars.get("g0") or "").strip() or "0"

    x = np.linspace(0.0, L, Nx)
    dx = x[1] - x[0]

    lam = c * dt / dx
    if lam > 1.0:
        dt = 0.95 * dx / c
        lam = c * dt / dx

    xsym = sp.Symbol("x", real=True)
    _, f0 = _parse_func(f0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})
    _, g0 = _parse_func(g0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})

    u0 = np.array(f0(x), dtype=float)
    v0 = np.array(g0(x), dtype=float)
    if u0.ndim == 0: u0 = np.full_like(x, float(u0))
    if v0.ndim == 0: v0 = np.full_like(x, float(v0))

    # Neumann BC enforced by mirroring: u[-1]=u[1], u[N]=u[N-2]
    def apply_neumann(u):
        u[0] = u[1]
        u[-1] = u[-2]
        return u

    u0 = apply_neumann(u0)
    v0 = apply_neumann(v0)

    u_xx0 = np.zeros_like(u0)
    u_xx0[1:-1] = (u0[2:] - 2*u0[1:-1] + u0[:-2]) / (dx*dx)
    # boundaries from Neumann mirror effectively handled by apply_neumann

    u1 = u0 + dt * v0 + 0.5 * (c*c) * (dt*dt) * u_xx0
    u1 = apply_neumann(u1)

    u_prev, u_curr = u0, u1
    t_now = dt

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    line, = ax.plot(x, u_curr)
    ax.set_title(f"Wave (Leapfrog Neumann) | CFL={lam:.3f} | beta={beta}")
    ax.set_xlabel("x"); ax.set_ylabel("u(x,t)")

    damp = 1.0 / (1.0 + beta*dt)  # simple damping factor

    def step(u_prev, u_curr):
        u_next = np.zeros_like(u_curr)
        u_next[1:-1] = (2*u_curr[1:-1] - u_prev[1:-1] +
                        (lam*lam) * (u_curr[2:] - 2*u_curr[1:-1] + u_curr[:-2]))
        # damping on velocity-like term
        if beta != 0.0:
            u_next = u_curr + damp*(u_next - u_curr)

        u_next = apply_neumann(u_next)
        return u_curr, u_next

    def update(frame):
        nonlocal u_prev, u_curr, t_now
        for _ in range(spf):
            u_prev, u_curr = step(u_prev, u_curr)
            t_now += dt
        line.set_ydata(u_curr)
        ax.set_title(f"Wave Neumann | t={t_now:.4f} | CFL={lam:.3f} | beta={beta}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()


def wave_leapfrog_mixed_animate(vars):
    # u_tt + 2*beta*u_t = c^2 u_xx
    # u(0,t)=0, u_x(L,t)=0
    L = float(sp.N(vars.get("L") or np.pi))
    c = float(sp.N(vars.get("c") or 1.0))
    beta = float(sp.N(vars.get("beta") or 0.0))

    Nx = int(vars.get("Nx") or 401)
    dt = float(vars.get("dt") or 0.001)
    frames = int(vars.get("frames") or 240)
    spf = int(vars.get("spf") or 5)

    f0_str = (vars.get("f0") or "").strip() or "sin(pi*x/(2*L))"
    g0_str = (vars.get("g0") or "").strip() or "0"

    x = np.linspace(0.0, L, Nx)
    dx = x[1] - x[0]

    lam = c * dt / dx
    if lam > 1.0:
        dt = 0.95 * dx / c
        lam = c * dt / dx

    xsym = sp.Symbol("x", real=True)
    _, f0 = _parse_func(f0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})
    _, g0 = _parse_func(g0_str, xsym, local_extra={"L": sp.Float(L), "pi": sp.pi})

    u0 = np.array(f0(x), dtype=float)
    v0 = np.array(g0(x), dtype=float)
    if u0.ndim == 0: u0 = np.full_like(x, float(u0))
    if v0.ndim == 0: v0 = np.full_like(x, float(v0))

    def apply_mixed(u):
        u[0] = 0.0        # Dirichlet left
        u[-1] = u[-2]     # Neumann right
        return u

    u0 = apply_mixed(u0)
    v0 = apply_mixed(v0)

    u_xx0 = np.zeros_like(u0)
    u_xx0[1:-1] = (u0[2:] - 2*u0[1:-1] + u0[:-2]) / (dx*dx)

    u1 = u0 + dt * v0 + 0.5 * (c*c) * (dt*dt) * u_xx0
    u1 = apply_mixed(u1)

    u_prev, u_curr = u0, u1
    t_now = dt
    damp = 1.0 / (1.0 + beta*dt)

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    line, = ax.plot(x, u_curr)
    ax.set_title(f"Wave (Leapfrog Mixed) | CFL={lam:.3f} | beta={beta}")
    ax.set_xlabel("x"); ax.set_ylabel("u(x,t)")

    def step(u_prev, u_curr):
        u_next = np.zeros_like(u_curr)
        u_next[1:-1] = (2*u_curr[1:-1] - u_prev[1:-1] +
                        (lam*lam) * (u_curr[2:] - 2*u_curr[1:-1] + u_curr[:-2]))
        if beta != 0.0:
            u_next = u_curr + damp*(u_next - u_curr)
        u_next = apply_mixed(u_next)
        return u_curr, u_next

    def update(frame):
        nonlocal u_prev, u_curr, t_now
        for _ in range(spf):
            u_prev, u_curr = step(u_prev, u_curr)
            t_now += dt
        line.set_ydata(u_curr)
        ax.set_title(f"Wave Mixed | t={t_now:.4f} | CFL={lam:.3f} | beta={beta}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()
