import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from . import math_tools
import matplotlib
matplotlib.use("TkAgg")

def _animate_expr(u_expr, x_sym, t_sym, L, title="Wave"):
    # defaults (user can override via vars if you want later)
    x_min = 0.0
    x_max = float(sp.N(L))
    xs = np.linspace(x_min, x_max, 200)

    # time
    t_max = 6.0
    frames = 120
    interval_ms = 30  # ~33 fps

    # lambdify
    f = sp.lambdify((x_sym, t_sym), u_expr, modules=["numpy"])

    # precompute to stabilize axis
    ts_preview = np.linspace(0, t_max, 30)
    y_min, y_max = None, None
    for tt in ts_preview:
        yy = np.array(f(xs, tt), dtype=float)
        m1, m2 = float(np.min(yy)), float(np.max(yy))
        y_min = m1 if y_min is None else min(y_min, m1)
        y_max = m2 if y_max is None else max(y_max, m2)
    pad = 0.1 * (y_max - y_min + 1e-9)
    y_min -= pad
    y_max += pad

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel(str(x_sym))
    ax.set_ylabel("u")

    (line,) = ax.plot(xs, np.zeros_like(xs))

    def update(frame):
        tt = (frame / (frames - 1)) * t_max
        yy = np.array(f(xs, tt), dtype=float)
        line.set_ydata(yy)
        ax.set_title(f"{title} | t = {tt:.3f}")
        return (line,)

    ani = FuncAnimation(fig, update, frames=frames, interval=interval_ms, blit=True)
    plt.show()


def wave_animate_dirichlet(vars):
    u_expr, x, t, L = math_tools._wave_series_dirichlet_expr(vars)
    _animate_expr(u_expr, x, t, L, title="Wave (Dirichlet)")


def wave_animate_neumann(vars):
    u_expr, x, t, L = math_tools._wave_series_neumann_expr(vars)
    _animate_expr(u_expr, x, t, L, title="Wave (Neumann)")


def wave_animate_mixed(vars):
    u_expr, x, t, L = math_tools._wave_series_mixed_expr(vars)
    _animate_expr(u_expr, x, t, L, title="Wave (Mixed)")

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


from .math_tools import SYMPY_FUNCS
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application
)
TRANSFORMATIONS = standard_transformations + (implicit_multiplication_application,)


def schrodinger_animate(vars):
    """
    1D time-dependent Schrödinger animation using Split-Step Fourier Method.
    Shows probability density |psi|^2.
    """

    # ---- grid ----
    # half-domain size: x in [-X, X]
    X = vars.get("X")
    if X is None:
        X = np.pi  # default domain half-width
    else:
        X = float(sp.N(X))

    N = int(vars.get("N") or 512)        # grid points (power of 2 is best)
    dt = float(vars.get("dt") or 0.005)  # time step
    a = float(vars.get("a") or 0.5)   # barrier half-width (|x|<a)
    steps_per_frame = int(vars.get("spf") or 5)  # integration steps per animation frame
    frames = int(vars.get("frames") or 240)

    # physics constants (can keep default ħ=1, m=1)
    
    x = np.linspace(-X, X, N, endpoint=False)
    dx = x[1] - x[0]
    hbar_in = vars.get("hbar")
    m_in = vars.get("m")

    hbar = 1.0 if (hbar_in is None or hbar_in == 0 or hbar_in == "") else float(sp.N(hbar_in))
    m = 1.0 if (m_in is None or m_in == 0 or m_in == "") else float(sp.N(m_in))
 
    # k-grid for FFT (angular wave numbers)
    k = 2 * np.pi * np.fft.fftfreq(N, d=dx)

    # ---- potential V(x) ----
    V_str = (vars.get("V") or "").strip()
    if V_str == "":
        V_str = "0"
    V_str = _convert_relations_to_piecewise(V_str)

    xsym = sp.Symbol("x", real=True)
    local_dict = {"x": xsym}
    local_dict.update(SYMPY_FUNCS)
    local_dict["Abs"] = sp.Abs
    local_dict["abs"] = sp.Abs
    local_dict["Piecewise"] = sp.Piecewise
    local_dict["Heaviside"] = sp.Heaviside
    # ---- potential V(x) ----
    V_str = (vars.get("V") or "").strip()
    if V_str == "":
        V_str = "0"

    xsym = sp.Symbol("x", real=True)
    local_dict = {"x": xsym}
    local_dict.update(SYMPY_FUNCS)
    local_dict["Abs"] = sp.Abs
    local_dict["abs"] = sp.Abs
    local_dict["Piecewise"] = sp.Piecewise
    local_dict["Heaviside"] = sp.Heaviside

    try:
        V_expr = parse_potential_with_relations(V_str, local_dict)
        V_fun = sp.lambdify(xsym, V_expr, modules=["numpy"])
        V = np.array(V_fun(x), dtype=float)
    except Exception as e:
        raise ValueError(f"V parse error: {e}")

   

    # ---- initial wave packet (Gaussian) ----
    # psi(x,0) = exp(-(x-x0)^2/(2*sigma^2)) * exp(i*k0*x)
    x0 = float(vars.get("x0") or (-0.4 * X))
    sigma = float(vars.get("sigma") or (0.15 * X))
    k0 = float(vars.get("k0") or (8.0 / X))  # momentum-ish

    psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)

    # normalize
    norm = np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
    psi = psi / (norm + 1e-15)

    # ---- split-step precompute ----
    # half-step potential phase
    expV_half = np.exp(-1j * V * (dt / 2) / hbar)

    # kinetic phase in k-space
    # exp(-i (ħ k^2 / 2m) dt)
    expT = np.exp(-1j * (hbar * (k ** 2) / (2 * m)) * dt)

    # ---- plot setup ----
    fig, ax = plt.subplots()
    ax.set_xlim(-X, X)
    ax.set_xlabel("x")
    ax.set_ylabel("|psi|^2 (probability density)")
    ax.set_title("Schrödinger 1D |ψ(x,t)|²")

    line_prob, = ax.plot(x, np.abs(psi) ** 2)
    info = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")
    # show potential scaled (optional) for visualization
    raw_showV = vars.get("showV")
    showV = "1" if raw_showV is None else str(raw_showV).strip().lower()
    if showV not in {"0", "false", "no", "n"}:

        # scale V into plot range
        Vmin, Vmax = np.min(V), np.max(V)
        if Vmax > Vmin:
            Vscaled = (V - Vmin) / (Vmax - Vmin + 1e-12)
            # scale to ~20% of max probability
            Vscaled = Vscaled * (0.2 * np.max(np.abs(psi) ** 2))
            ax.plot(x, Vscaled, linestyle="--")

    # y-limit auto
    ax.set_ylim(0, max(0.25 * np.max(np.abs(psi) ** 2), 1e-6))

    t_now = 0.0

    def step_once(psi_arr):
        # V half
        psi_arr *= expV_half
        # T full via FFT
        psi_k = np.fft.fft(psi_arr)
        psi_k *= expT
        psi_arr = np.fft.ifft(psi_k)
        # V half
        psi_arr *= expV_half
        return psi_arr

    def update(frame):
        nonlocal psi, t_now
        for _ in range(steps_per_frame):
            psi = step_once(psi)
            # renormalize slowly to avoid drift
            if frame % 20 == 0:
                norm = np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
                psi = psi / (norm + 1e-15)
            t_now += dt

        prob = np.abs(psi) ** 2
                # ---- probabilities ----
        # indices
        left_mask = x < -a
        barrier_mask = (x >= -a) & (x <= a)
        right_mask = x > a

        P_left = float(np.sum(prob[left_mask]) * dx)
        P_bar = float(np.sum(prob[barrier_mask]) * dx)
        P_right = float(np.sum(prob[right_mask]) * dx)

        info.set_text(f"P_left={P_left:.3f}  P_bar={P_bar:.3f}  P_right={P_right:.3f}")

        line_prob.set_ydata(prob)
        ax.set_title(f"Schrödinger 1D |ψ|²  |  t = {t_now:.3f}")
        return (line_prob, info)

    ani = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
    plt.show()

import re

def _convert_relations_to_piecewise(s: str) -> str:
    """
    Convert patterns like:  (something < something)
    into: Piecewise((1, something < something),(0, True))
    so the user can write: 12*(abs(x) < 0.5)
    """
    if not isinstance(s, str):
        return s

    s = s.strip()

    # Replace boolean comparisons inside parentheses: (... < ...)  etc.
    # This is simple but works well for typical barrier conditions.
    pattern = r"\(([^()]+?)(<=|>=|<|>|==)([^()]+?)\)"
    while re.search(pattern, s):
        s = re.sub(pattern, r"Piecewise((1, \1\2\3),(0, True))", s)
    return s

import ast

def parse_potential_with_relations(v_str: str, local_dict: dict):
    """
    Allows V like: 12*(abs(x)<0.5) or (x>0)&(abs(x)<1)
    Converts comparisons to Piecewise((1,cond),(0,True)) BEFORE SymPy touches it.
    """
    v_str = (v_str or "").strip()
    if v_str == "":
        v_str = "0"
    v_str = v_str.replace("^", "**")

    def sym(node):
        if isinstance(node, ast.Constant):
            return sp.Integer(node.value) if isinstance(node.value, int) else sp.Float(node.value)
        if isinstance(node, ast.Name):
            return local_dict.get(node.id, sp.Symbol(node.id))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -sym(node.operand)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
            return +sym(node.operand)

        if isinstance(node, ast.BinOp):
            a = sym(node.left); b = sym(node.right)
            if isinstance(node.op, ast.Add): return a + b
            if isinstance(node.op, ast.Sub): return a - b
            if isinstance(node.op, ast.Mult): return a * b
            if isinstance(node.op, ast.Div): return a / b
            if isinstance(node.op, ast.Pow): return a ** b
            raise ValueError("Unsupported binary op")

        if isinstance(node, ast.Call):
            fn = sym(node.func)
            args = [sym(a) for a in node.args]
            return fn(*args)

        # comparisons: a < b, a <= b, ...
        if isinstance(node, ast.Compare):
            if len(node.ops) != 1 or len(node.comparators) != 1:
                raise ValueError("Chained comparisons not supported (use (a<b) & (b<c))")
            left = sym(node.left)
            right = sym(node.comparators[0])
            op = node.ops[0]
            if isinstance(op, ast.Lt):  cond = sp.Lt(left, right)
            elif isinstance(op, ast.LtE): cond = sp.Le(left, right)
            elif isinstance(op, ast.Gt):  cond = sp.Gt(left, right)
            elif isinstance(op, ast.GtE): cond = sp.Ge(left, right)
            elif isinstance(op, ast.Eq):  cond = sp.Eq(left, right)
            elif isinstance(op, ast.NotEq): cond = sp.Ne(left, right)
            else:
                raise ValueError("Unsupported compare op")

            return sp.Piecewise((1, cond), (0, True))

        # boolean: (a<b) & (c<d)  OR  (a<b) | (c<d)
        if isinstance(node, ast.BoolOp):
            vals = [sym(v) for v in node.values]
            if isinstance(node.op, ast.And):
                # And of Piecewise => multiply them (0/1)
                out = vals[0]
                for v in vals[1:]:
                    out = out * v
                return out
            if isinstance(node.op, ast.Or):
                # OR: 1 - (1-a)(1-b) for 0/1 values
                out = vals[0]
                for v in vals[1:]:
                    out = 1 - (1-out)*(1-v)
                return out
            raise ValueError("Unsupported BoolOp")

        if isinstance(node, ast.Subscript):
            raise ValueError("Subscript not supported")

        raise ValueError(f"Unsupported syntax: {type(node).__name__}")

    tree = ast.parse(v_str, mode="eval")
    return sp.simplify(sym(tree.body))
