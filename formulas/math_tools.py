# formulas/math_tools.py
import re
import sympy as sp
from sympy import pretty
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

# ---------- Supported functions/constants for parsing ----------
SYMPY_FUNCS = {
    # trig
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "csc": sp.csc,
    "sec": sp.sec,
    "cot": sp.cot,

    # inverse trig
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,

    # hyperbolic
    "sinh": sp.sinh,
    "cosh": sp.cosh,
    "tanh": sp.tanh,

    # inverse hyperbolic
    "asinh": sp.asinh,
    "acosh": sp.acosh,
    "atanh": sp.atanh,

    # misc
    "pi": sp.pi,
    "e": sp.E,
    "sqrt": sp.sqrt,
    "ln": sp.log,
    "log": sp.log,
    "exp": sp.exp,

    # infinity
    "oo": sp.oo,
    "inf": sp.oo,
}

# For normal algebra parsing (allows 2x, etc.)
TRANSFORMATIONS = standard_transformations + (implicit_multiplication_application,)


# ---------- Core parsers ----------
def parse_expression(expr_str: str):
    """Parse math expression like: 2x + sin(x) - x^2"""
    expr_str = (expr_str or "").strip()
    expr_str = expr_str.replace("^", "**")

    x, y, z, t = sp.symbols("x y z t")
    local_dict = {"x": x, "y": y, "z": z, "t": t}
    local_dict.update(SYMPY_FUNCS)

    return parse_expr(expr_str, local_dict=local_dict, transformations=TRANSFORMATIONS)


def parse_matrix(text: str):
    """Parse matrix text like: [[1,2],[3,4]]"""
    return sp.Matrix(sp.sympify(text, locals=SYMPY_FUNCS))


# -----------------------------
# DIFFERENTIATION
# -----------------------------
def differentiate(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip()
    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)
    result = sp.diff(expr, var)

    return f"Expression:\n{pretty(expr)}\n\nDerivative:\n{pretty(result)}"


# -----------------------------
# INDEFINITE INTEGRAL
# -----------------------------
def indefinite_integral(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip()
    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)
    result = sp.integrate(expr, var)

    return f"Expression:\n{pretty(expr)}\n\nIntegral:\n{pretty(result)} + C"


# -----------------------------
# DEFINITE INTEGRAL
# -----------------------------
def definite_integral(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip()
    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)
    a = vars["a"]
    b = vars["b"]

    result = sp.integrate(expr, (var, a, b))
    return f"Expression:\n{pretty(expr)}\nFrom {a} to {b}\n\nResult:\n{pretty(result)}"


# -----------------------------
# SOLVE EQUATION  (solve eq = 0)
# -----------------------------
def solve_equation(vars):
    eq_expr = parse_expression(vars["eq"])
    var_str = (vars["var"] or "").strip()
    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)
    sol = sp.solve(eq_expr, var)
    return f"Solve {eq_expr} = 0 for {var} => {sol}"


# -----------------------------
# MATRIX (Large friendly)
# -----------------------------
def matrix_determinant(vars):
    M = parse_matrix(vars["matrix"])
    # LU is typically faster for bigger matrices
    return f"det(M) = {M.det(method='lu')}"


def matrix_inverse(vars):
    M = parse_matrix(vars["matrix"])
    # LU method helps (still heavy for 100x100 symbolic)
    return f"M^-1 = \n{M.inv(method='LU')}"


def matrix_multiply(vars):
    A = parse_matrix(vars["A"])
    B = parse_matrix(vars["B"])
    return f"A*B = \n{A * B}"


def matrix_eigenvalues(vars):
    M = parse_matrix(vars["matrix"])
    return f"Eigenvalues = {M.eigenvals()}"


# -----------------------------
# LIMIT
# -----------------------------
def limit_calc(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip()
    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)
    point = vars["point"]
    direction = (vars["dir"] or "").strip()

    if direction == "":
        result = sp.limit(expr, var, point)
        return (
            f"Expression:\n{pretty(expr)}\n\n"
            f"Limit:\nlim({var} → {point}) {pretty(expr)}\n\n"
            f"Answer:\n{pretty(result)}"
        )

    if direction not in ["+", "-"]:
        return "❌ dir must be + or - (or leave empty)."

    result = sp.limit(expr, var, point, dir=direction)
    return (
        f"Expression:\n{pretty(expr)}\n\n"
        f"Limit:\nlim({var} → {point}{direction}) {pretty(expr)}\n\n"
        f"Answer:\n{pretty(result)}"
    )


# -----------------------------
# L'HOPITAL AUTO LIMIT
# -----------------------------
def lhopital_limit(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip()
    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)
    point = vars["point"]
    direction = (vars["dir"] or "").strip()

    if direction not in ["", "+", "-"]:
        return "❌ dir must be + or - (or leave empty)."

    num, den = sp.fraction(expr)

    try:
        if direction == "":
            L_num = sp.limit(num, var, point)
            L_den = sp.limit(den, var, point)
        else:
            L_num = sp.limit(num, var, point, dir=direction)
            L_den = sp.limit(den, var, point, dir=direction)
    except Exception as e:
        return f"❌ Cannot evaluate limit: {e}"

    indeterminate = (L_num == 0 and L_den == 0) or (
        L_num in [sp.oo, -sp.oo] and L_den in [sp.oo, -sp.oo]
    )

    if not indeterminate:
        result = sp.limit(expr, var, point) if direction == "" else sp.limit(expr, var, point, dir=direction)
        return f"Direct limit worked.\n\n{pretty(result)}"

    steps = []
    current_num = num
    current_den = den

    for i in range(1, 6):
        current_num = sp.diff(current_num, var)
        current_den = sp.diff(current_den, var)

        steps.append(f"Step {i}:")
        steps.append(f"d/d{var}(num) = {pretty(current_num)}")
        steps.append(f"d/d{var}(den) = {pretty(current_den)}\n")

        new_expr = current_num / current_den

        try:
            if direction == "":
                L_new_num = sp.limit(current_num, var, point)
                L_new_den = sp.limit(current_den, var, point)
            else:
                L_new_num = sp.limit(current_num, var, point, dir=direction)
                L_new_den = sp.limit(current_den, var, point, dir=direction)

            still_ind = (L_new_num == 0 and L_new_den == 0) or (
                L_new_num in [sp.oo, -sp.oo] and L_new_den in [sp.oo, -sp.oo]
            )

            if not still_ind:
                result = sp.limit(new_expr, var, point) if direction == "" else sp.limit(new_expr, var, point, dir=direction)
                return (
                    "L'Hôpital Rule Applied (Auto Mode)\n\n"
                    f"Original:\n{pretty(expr)}\n\n"
                    + "\n".join(steps)
                    + f"\nFinal limit:\n{pretty(result)}"
                )
        except Exception:
            pass

    return "❌ L'Hôpital could not resolve after 5 steps.\nTry normal limit or simplify expression."


# -----------------------------
# DOUBLE / TRIPLE INTEGRAL (Exact + Approx)
# -----------------------------
def double_integral(vars):
    expr = parse_expression(vars["expr"])

    var1 = (vars["var1"] or "").strip() or "x"
    var2 = (vars["var2"] or "").strip() or "y"

    x = sp.Symbol(var1)
    y = sp.Symbol(var2)

    a = vars["a"]
    b = vars["b"]
    c = vars["c"]
    d = vars["d"]

    result = sp.integrate(expr, (y, c, d), (x, a, b))
    approx = sp.N(result)

    return (
        f"Expression:\n{pretty(expr)}\n\n"
        f"Double Integral:\n∫[{a},{b}] ∫[{c},{d}] f({var1},{var2}) d{var2} d{var1}\n\n"
        f"Exact Result:\n{pretty(result)}\n\n"
        f"Approx Result:\n{approx}"
    )


def triple_integral(vars):
    expr = parse_expression(vars["expr"])

    var1 = (vars["var1"] or "").strip() or "x"
    var2 = (vars["var2"] or "").strip() or "y"
    var3 = (vars["var3"] or "").strip() or "z"

    x = sp.Symbol(var1)
    y = sp.Symbol(var2)
    z = sp.Symbol(var3)

    a = vars["a"]
    b = vars["b"]
    c = vars["c"]
    d = vars["d"]
    e = vars["e"]
    f_ = vars["f"]

    result = sp.integrate(expr, (z, e, f_), (y, c, d), (x, a, b))
    approx = sp.N(result)

    return (
        f"Expression:\n{pretty(expr)}\n\n"
        f"Triple Integral:\n∫[{a},{b}] ∫[{c},{d}] ∫[{e},{f_}] f({var1},{var2},{var3}) d{var3} d{var2} d{var1}\n\n"
        f"Exact Result:\n{pretty(result)}\n\n"
        f"Approx Result:\n{approx}"
    )


# -----------------------------
# TAYLOR / MACLAURIN
# -----------------------------
def taylor_series(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip() or "x"
    var = sp.Symbol(var_str)

    point = vars["point"]
    n = int(vars["n"])

    series_expr = sp.series(expr, var, point, n).removeO()
    approx = sp.N(series_expr)

    return (
        f"Expression:\n{pretty(expr)}\n\n"
        f"Taylor Series about {var} = {point} (order {n}):\n{pretty(series_expr)}\n\n"
        f"Approx:\n{approx}"
    )


def maclaurin_series(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip() or "x"
    var = sp.Symbol(var_str)

    n = int(vars["n"])
    series_expr = sp.series(expr, var, 0, n).removeO()
    approx = sp.N(series_expr)

    return (
        f"Expression:\n{pretty(expr)}\n\n"
        f"Maclaurin Series (order {n}):\n{pretty(series_expr)}\n\n"
        f"Approx:\n{approx}"
    )


# -----------------------------
# ODE (Shorthand: y' y'' y''' and normal equations)
# -----------------------------
def solve_ode(vars):
    eq_str = (vars["eq"] or "").strip()
    var_str = (vars["var"] or "").strip() or "x"

    if eq_str == "":
        return "❌ Error: eq is empty. Example: y' + y = 0"

    x = sp.Symbol(var_str)
    y = sp.Function("y")

    s = eq_str.replace(" ", "")

    s = re.sub(r"y'''", "diff(y(x),x,3)", s)
    s = re.sub(r"y''", "diff(y(x),x,2)", s)
    s = re.sub(r"y'", "diff(y(x),x,1)", s)
    s = re.sub(r"\by\b(?!\()", "y(x)", s)

    if "=" in s:
        left, right = s.split("=", 1)
        s = f"Eq({left},{right})"
    else:
        s = f"Eq({s},0)"

    local_dict = {"x": x, "y": y, "Eq": sp.Eq, "diff": sp.diff}
    local_dict.update(SYMPY_FUNCS)

    try:
        eq = parse_expr(s, local_dict=local_dict, transformations=standard_transformations)
    except Exception as e:
        return f"❌ Parse error: {e}\nParsed string was:\n{s}"

    try:
        sol = sp.dsolve(eq)
    except Exception as e:
        return f"❌ Cannot solve ODE: {e}"

    return f"ODE Input:\n{eq_str}\n\nParsed Equation:\n{pretty(eq)}\n\nSolution:\n{pretty(sol)}"


# -----------------------------
# LAPLACE / INVERSE LAPLACE
# -----------------------------
def laplace_transform(vars):
    expr = parse_expression(vars["expr"])
    t_str = (vars["t"] or "").strip() or "t"
    s_str = (vars["s"] or "").strip() or "s"

    t = sp.Symbol(t_str, positive=True)
    s = sp.Symbol(s_str)

    result = sp.laplace_transform(expr, t, s, noconds=True)
    approx = sp.N(result)

    return f"Expression:\n{pretty(expr)}\n\nLaplace:\n{pretty(result)}\n\nApprox:\n{approx}"


def inverse_laplace_transform(vars):
    expr = parse_expression(vars["expr"])
    s_str = (vars["s"] or "").strip() or "s"
    t_str = (vars["t"] or "").strip() or "t"

    s = sp.Symbol(s_str)
    t = sp.Symbol(t_str, positive=True)

    result = sp.inverse_laplace_transform(expr, s, t)
    approx = sp.N(result)

    return f"Expression:\n{pretty(expr)}\n\nInverse Laplace:\n{pretty(result)}\n\nApprox:\n{approx}"


# -----------------------------
# FOURIER SERIES
# -----------------------------
def fourier_series_calc(vars):
    expr = parse_expression(vars["expr"])
    var_str = (vars["var"] or "").strip() or "x"
    x = sp.Symbol(var_str)

    L = vars["L"]
    n_terms = int(vars["n"])

    series = sp.fourier_series(expr, (x, -L, L)).truncate(n_terms)
    approx = sp.N(series)

    return (
        f"Expression:\n{pretty(expr)}\n\n"
        f"Fourier Series on [-{L}, {L}] (first {n_terms} terms):\n{pretty(series)}\n\n"
        f"Approx:\n{approx}"
    )

# -----------------------------
# PDE (Shorthand: u_t, u_xx, u_xt, u_tt ...)
# -----------------------------
def solve_pde(vars):
    eq_in = (vars.get("eq") or "").replace(" ", "")

    # ---- Heat equation auto route (u_t - k*u_xx = 0, not wave) ----
    if ("_t" in eq_in) and ("_xx" in eq_in) and ("_tt" not in eq_in):
        bc = (vars.get("bc") or "").strip().lower()

        if bc in {"neumann", "n"}:
            return heat_equation_fourier_neumann(vars)

        if bc in {"mixed", "m"}:
            return heat_equation_fourier_mixed(vars)

        # default = dirichlet
        return heat_equation_fourier_dirichlet(vars)
        
    if ("_tt" in eq_in) and ("_xx" in eq_in):
                    bc = (vars.get("bc") or "").strip().lower()
                    return wave_equation_fourier_dirichlet(vars)

    # ---- If not heat, fall back to your general PDE solver ----
    return pdsolve_general(vars)
 
    v1 = (vars["var1"] or "").strip() or "x"
    v2 = (vars["var2"] or "").strip() or "t"
    fname = (vars["f"] or "").strip() or "u"

    # -------- HEAT EQUATION --------
    if "u_t" in eq_in and "u_xx" in eq_in:
        return heat_equation_separation(vars)

    # -------- WAVE EQUATION --------
    if "u_tt" in eq_in and "u_xx" in eq_in:
        return wave_equation_solver(vars)

    # -------- LAPLACE EQUATION --------
    if "u_xx" in eq_in and "u_yy" in eq_in:
        return laplace_equation_solver(vars)

    # -------- TRANSPORT --------
    if "u_t" in eq_in and "u_x" in eq_in and "u_xx" not in eq_in:
        return transport_equation_solver(vars)

    # -------- DEFAULT pdsolve --------
    try:
        return pdsolve_general(vars)
    except Exception as e:
        return f"❌ PDE not recognized / cannot solve: {e}"

def heat_equation_fourier_dirichlet(vars):
    """
    Solve heat equation on 0<x<L with Dirichlet BC:
      u_t = k u_xx
      u(0,t)=0, u(L,t)=0
      u(x,0)=f0(x)

    Output: truncated Fourier series (N terms)
    """
    v1 = (vars.get("var1") or "").strip() or "x"
    v2 = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"

    x = sp.Symbol(v1, real=True)
    t = sp.Symbol(v2, real=True)

    L = vars.get("L")
    k = vars.get("k")

    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi or L = 1"

    # k can be number; if user leaves blank, treat as symbol k
    if k is None:
        k = sp.Symbol("k", positive=True, real=True)
    else:
        k = sp.sympify(k)

    N = int(vars.get("n") or 10)
    if N < 1:
        return "❌ Error: n must be >= 1"

    f0_str = (vars.get("f0") or "").strip()
    if f0_str == "":
        return "❌ Error: f0 is empty. Example: f0 = sin(pi*x/L)"

    # Parse f0(x)
    local_dict = {v1: x}
    local_dict.update(SYMPY_FUNCS)
    local_dict.update({"L": sp.sympify(L), "k": k})
    try:
        f0 = parse_expr(f0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in f0: {e}"

    Lsym = sp.sympify(L)

    n = sp.Symbol("n", integer=True, positive=True)
    bn = (2 / Lsym) * sp.integrate(f0 * sp.sin(n * sp.pi * x / Lsym), (x, 0, Lsym))

    # Build truncated series
    series = sp.Integer(0)
    for i in range(1, N + 1):
        bi = sp.simplify(bn.subs(n, i))
        term = bi * sp.sin(i * sp.pi * x / Lsym) * sp.exp(-k * (i * sp.pi / Lsym) ** 2 * t)
        series += term

    series_simplified = sp.simplify(series)

    return (
        "Heat Equation (Fourier Series, Dirichlet BC)\n"
        f"PDE: {fname}_t = k*{fname}_xx,   0<{v1}<L\n"
        "BC: u(0,t)=0, u(L,t)=0\n"
        f"IC: u({v1},0)=f0({v1})\n\n"
        f"Given: L = {pretty(Lsym)},  k = {pretty(k)},  N = {N}\n\n"
        f"f0({v1}) = {pretty(f0)}\n\n"
        "General coefficients:\n"
        f"b_n = (2/L) * ∫[0..L] f0(x) sin(nπx/L) dx\n"
        f"b_n = {pretty(sp.simplify(bn))}\n\n"
        "Truncated solution (N terms):\n"
        f"{pretty(series_simplified)}\n\n"
        "Approx (decimal):\n"
        f"{sp.N(series_simplified)}"
    )

def heat_equation_fourier_neumann(vars):
    """
    u_t = k u_xx on 0<x<L
    Neumann BC: u_x(0,t)=0, u_x(L,t)=0
    IC: u(x,0)=f0(x)
    => cosine series
    """
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"
    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = vars.get("L")
    k = vars.get("k")
    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi"
    L = sp.sympify(L)

    if k is None:
        k = sp.Symbol("k", positive=True, real=True)
    else:
        k = sp.sympify(k)

    N = int(vars.get("n") or 10)
    if N < 1:
        return "❌ Error: n must be >= 1"

    f0_str = (vars.get("f0") or "").strip()
    if f0_str == "":
        return "❌ Error: f0 is empty. Example: f0 = cos(x)"

    local_dict = {xname: x, "L": L, "k": k, **SYMPY_FUNCS}
    f0 = parse_expr(f0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)

    n = sp.Symbol("n", integer=True, nonnegative=True)

    # a0 term:
    a0 = (2 / L) * sp.integrate(f0, (x, 0, L))

    # an for n>=1:
    an = (2 / L) * sp.integrate(f0 * sp.cos(n * sp.pi * x / L), (x, 0, L))

    series = sp.Rational(1, 2) * sp.simplify(a0)  # a0/2
    for i in range(1, N + 1):
        ai = sp.simplify(an.subs(n, i))
        term = ai * sp.cos(i * sp.pi * x / L) * sp.exp(-k * (i * sp.pi / L) ** 2 * t)
        series += term

    series = sp.simplify(series)

    return (
        "Heat Equation (Fourier Cosine Series, Neumann BC)\n"
        f"PDE: {fname}_t = k*{fname}_xx,   0<{xname}<L\n"
        "BC: u_x(0,t)=0, u_x(L,t)=0\n"
        f"IC: u({xname},0)=f0({xname})\n\n"
        f"Given: L = {pretty(L)},  k = {pretty(k)},  N = {N}\n\n"
        f"f0({xname}) = {pretty(f0)}\n\n"
        f"a0 = (2/L)∫[0..L] f0 dx = {pretty(sp.simplify(a0))}\n"
        f"an = (2/L)∫[0..L] f0 cos(nπx/L) dx\n\n"
        "Truncated solution:\n"
        f"{pretty(series)}\n\n"
        "Approx:\n"
        f"{sp.N(series)}"
    )

def heat_equation_fourier_mixed(vars):
    """
    u_t = k u_xx on 0<x<L
    Mixed BC: u(0,t)=0, u_x(L,t)=0
    IC: u(x,0)=f0(x)
    => sine half-integer series: sin((n+1/2)πx/L)
    """
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"
    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = vars.get("L")
    k = vars.get("k")
    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi"
    L = sp.sympify(L)

    if k is None:
        k = sp.Symbol("k", positive=True, real=True)
    else:
        k = sp.sympify(k)

    N = int(vars.get("n") or 10)
    if N < 1:
        return "❌ Error: n must be >= 1"

    f0_str = (vars.get("f0") or "").strip()
    if f0_str == "":
        return "❌ Error: f0 is empty."

    local_dict = {xname: x, "L": L, "k": k, **SYMPY_FUNCS}
    f0 = parse_expr(f0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)

    n = sp.Symbol("n", integer=True, nonnegative=True)

    # b_n = (2/L) ∫ f0(x) sin((n+1/2)πx/L) dx
    basis = sp.sin((n + sp.Rational(1, 2)) * sp.pi * x / L)
    bn = (2 / L) * sp.integrate(f0 * basis, (x, 0, L))

    series = sp.Integer(0)
    for i in range(0, N):  # n = 0..N-1
        bi = sp.simplify(bn.subs(n, i))
        lam = ((i + sp.Rational(1, 2)) * sp.pi / L) ** 2
        term = bi * sp.sin((i + sp.Rational(1, 2)) * sp.pi * x / L) * sp.exp(-k * lam * t)
        series += term

    series = sp.simplify(series)

    return (
        "Heat Equation (Half-Integer Sine Series, Mixed BC)\n"
        f"PDE: {fname}_t = k*{fname}_xx,   0<{xname}<L\n"
        "BC: u(0,t)=0, u_x(L,t)=0\n"
        f"IC: u({xname},0)=f0({xname})\n\n"
        f"Given: L = {pretty(L)},  k = {pretty(k)},  N = {N}\n\n"
        f"f0({xname}) = {pretty(f0)}\n\n"
        "Truncated solution:\n"
        f"{pretty(series)}\n\n"
        "Approx:\n"
        f"{sp.N(series)}"
    )

def wave_equation_fourier_dirichlet(vars):
    """
    Wave equation on 0<x<L with Dirichlet BC:
      u_tt = c^2 u_xx
      u(0,t)=0, u(L,t)=0
      u(x,0)=f0(x)
      u_t(x,0)=g0(x)

    Output: truncated Fourier series (N terms)
    """
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"

    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = vars.get("L")
    c = vars.get("c")

    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi"
    L = sp.sympify(L)

    if c is None or c == 0:
        return "❌ Error: c must be nonzero. Example: c = 1"
    c = sp.sympify(c)

    N = int(vars.get("n") or 10)
    if N < 1:
        return "❌ Error: n must be >= 1"

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip()

    if f0_str == "":
        return "❌ Error: f0 is empty. Example: f0 = sin(x)"
    if g0_str == "":
        g0_str = "0"  # allow empty => zero initial velocity

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}

    try:
        f0 = parse_expr(f0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in f0: {e}"

    try:
        g0 = parse_expr(g0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in g0: {e}"

    n = sp.Symbol("n", integer=True, positive=True)

    # Fourier sine coefficients for Dirichlet:
    # A_n = (2/L) ∫ f0(x) sin(nπx/L) dx
    # B_n = (2/(nπc)) ∫ g0(x) sin(nπx/L) dx
    An = (2 / L) * sp.integrate(f0 * sp.sin(n * sp.pi * x / L), (x, 0, L))
    Bn = (2 / (n * sp.pi * c)) * sp.integrate(g0 * sp.sin(n * sp.pi * x / L), (x, 0, L))

    series = sp.Integer(0)
    for i in range(1, N + 1):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        w = i * sp.pi * c / L
        term = (Ai * sp.cos(w * t) + Bi * sp.sin(w * t)) * sp.sin(i * sp.pi * x / L)
        series += term

    series = sp.simplify(series)

    return (
        "Wave Equation (Fourier Sine Series, Dirichlet BC)\n"
        f"PDE: {fname}_tt = c^2*{fname}_xx,   0<{xname}<L\n"
        "BC: u(0,t)=0, u(L,t)=0\n"
        f"IC: u({xname},0)=f0({xname}),   u_t({xname},0)=g0({xname})\n\n"
        f"Given: L = {pretty(L)},  c = {pretty(c)},  N = {N}\n\n"
        f"f0({xname}) = {pretty(f0)}\n"
        f"g0({xname}) = {pretty(g0)}\n\n"
        "Coefficients:\n"
        "A_n = (2/L)∫ f0(x) sin(nπx/L) dx\n"
        "B_n = (2/(nπc))∫ g0(x) sin(nπx/L) dx\n\n"
        "Truncated solution:\n"
        f"{pretty(series)}\n\n"
        "Approx:\n"
        f"{sp.N(series)}"
    )

def wave_equation_fourier_neumann(vars):
    """
    Wave equation on 0<x<L with Neumann BC:
      u_tt = c^2 u_xx
      u_x(0,t)=0, u_x(L,t)=0
      u(x,0)=f0(x)
      u_t(x,0)=g0(x)
    """
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"

    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = vars.get("L")
    c = vars.get("c")

    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi"
    L = sp.sympify(L)

    if c is None or c == 0:
        return "❌ Error: c must be nonzero. Example: c = 1"
    c = sp.sympify(c)

    N = int(vars.get("n") or 10)
    if N < 0:
        return "❌ Error: n must be >= 0"

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip()

    if f0_str == "":
        return "❌ Error: f0 is empty. Example: f0 = 1 + cos(x)"
    if g0_str == "":
        g0_str = "0"

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}

    try:
        f0 = parse_expr(f0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in f0: {e}"

    try:
        g0 = parse_expr(g0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in g0: {e}"

    n = sp.Symbol("n", integer=True, nonnegative=True)

    A0 = (1 / L) * sp.integrate(f0, (x, 0, L))
    An = (2 / L) * sp.integrate(f0 * sp.cos(n * sp.pi * x / L), (x, 0, L))
    Bn = (2 / (n * sp.pi * c)) * sp.integrate(g0 * sp.cos(n * sp.pi * x / L), (x, 0, L))

    series = sp.simplify(A0)

    for i in range(1, N + 1):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        w = i * sp.pi * c / L
        series += (Ai * sp.cos(w * t) + Bi * sp.sin(w * t)) * sp.cos(i * sp.pi * x / L)

    series = sp.simplify(series)

    return (
        "Wave Equation (Fourier Cosine Series, Neumann BC)\n"
        f"PDE: {fname}_tt = c^2*{fname}_xx,   0<{xname}<L\n"
        "BC: u_x(0,t)=0, u_x(L,t)=0\n"
        f"IC: u({xname},0)=f0({xname}),   u_t({xname},0)=g0({xname})\n\n"
        f"Given: L = {pretty(L)},  c = {pretty(c)},  N = {N}\n\n"
        f"Truncated solution:\n{pretty(series)}"
    )

def wave_equation_fourier_neumann(vars):
    """
    Wave equation on 0<x<L with Neumann BC:
      u_tt = c^2 u_xx
      u_x(0,t)=0, u_x(L,t)=0
      u(x,0)=f0(x)
      u_t(x,0)=g0(x)
    """
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"

    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = vars.get("L")
    c = vars.get("c")

    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi"
    L = sp.sympify(L)

    if c is None or c == 0:
        return "❌ Error: c must be nonzero. Example: c = 1"
    c = sp.sympify(c)

    N = int(vars.get("n") or 10)
    if N < 0:
        return "❌ Error: n must be >= 0"

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip()

    if f0_str == "":
        return "❌ Error: f0 is empty. Example: f0 = 1 + cos(x)"
    if g0_str == "":
        g0_str = "0"

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}

    try:
        f0 = parse_expr(f0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in f0: {e}"

    try:
        g0 = parse_expr(g0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    except Exception as e:
        return f"❌ Parse error in g0: {e}"

    n = sp.Symbol("n", integer=True, nonnegative=True)

    A0 = (1 / L) * sp.integrate(f0, (x, 0, L))
    An = (2 / L) * sp.integrate(f0 * sp.cos(n * sp.pi * x / L), (x, 0, L))
    Bn = (2 / (n * sp.pi * c)) * sp.integrate(g0 * sp.cos(n * sp.pi * x / L), (x, 0, L))

    series = sp.simplify(A0)

    for i in range(1, N + 1):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        w = i * sp.pi * c / L
        series += (Ai * sp.cos(w * t) + Bi * sp.sin(w * t)) * sp.cos(i * sp.pi * x / L)

    series = sp.simplify(series)

    return (
        "Wave Equation (Fourier Cosine Series, Neumann BC)\n"
        f"PDE: {fname}_tt = c^2*{fname}_xx,   0<{xname}<L\n"
        "BC: u_x(0,t)=0, u_x(L,t)=0\n"
        f"IC: u({xname},0)=f0({xname}),   u_t({xname},0)=g0({xname})\n\n"
        f"Given: L = {pretty(L)},  c = {pretty(c)},  N = {N}\n\n"
        f"Truncated solution:\n{pretty(series)}"
    )

def wave_equation_fourier_mixed(vars):
    """
    Wave equation on 0<x<L with Mixed BC:
      u_tt = c^2 u_xx
      u(0,t)=0, u_x(L,t)=0
      u(x,0)=f0(x)
      u_t(x,0)=g0(x)

    Basis: sin((n+1/2)πx/L)
    """
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    fname = (vars.get("f") or "").strip() or "u"

    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = vars.get("L")
    c = vars.get("c")

    if L is None or L == 0:
        return "❌ Error: L must be nonzero. Example: L = pi"
    L = sp.sympify(L)

    if c is None or c == 0:
        return "❌ Error: c must be nonzero. Example: c = 1"
    c = sp.sympify(c)

    N = int(vars.get("n") or 10)
    if N < 1:
        return "❌ Error: n must be >= 1"

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip()

    if f0_str == "":
        return "❌ Error: f0 is empty."
    if g0_str == "":
        g0_str = "0"

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}
    f0 = parse_expr(f0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    g0 = parse_expr(g0_str.replace("^","**"), local_dict=local_dict, transformations=TRANSFORMATIONS)

    n = sp.Symbol("n", integer=True, nonnegative=True)

    basis = sp.sin((n + sp.Rational(1, 2)) * sp.pi * x / L)

    # A_n = (2/L) ∫ f0(x) sin((n+1/2)πx/L) dx
    # B_n = (2/(ω_n L)) ∫ g0(x) sin((n+1/2)πx/L) dx
    # ω_n = (n+1/2)πc/L
    An = (2 / L) * sp.integrate(f0 * basis, (x, 0, L))
    wn = (n + sp.Rational(1, 2)) * sp.pi * c / L
    Bn = (2 / (wn * L)) * sp.integrate(g0 * basis, (x, 0, L))

    series = sp.Integer(0)
    for i in range(0, N):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        wi = sp.simplify(wn.subs(n, i))
        term = (Ai * sp.cos(wi * t) + Bi * sp.sin(wi * t)) * sp.sin((i + sp.Rational(1, 2)) * sp.pi * x / L)
        series += term

    series = sp.simplify(series)

    return (
        "Wave Equation (Half-Integer Sine Series, Mixed BC)\n"
        f"PDE: {fname}_tt = c^2*{fname}_xx,   0<{xname}<L\n"
        "BC: u(0,t)=0, u_x(L,t)=0\n"
        f"IC: u({xname},0)=f0({xname}),   u_t({xname},0)=g0({xname})\n\n"
        f"Given: L = {pretty(L)},  c = {pretty(c)},  N = {N}\n\n"
        f"Truncated solution:\n{pretty(series)}"
    )

def _wave_series_dirichlet_expr(vars):
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = sp.sympify(vars.get("L"))
    c = sp.sympify(vars.get("c"))
    N = int(vars.get("n") or 10)

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip() or "0"

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}
    f0 = parse_expr(f0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    g0 = parse_expr(g0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)

    n = sp.Symbol("n", integer=True, positive=True)
    An = (2 / L) * sp.integrate(f0 * sp.sin(n * sp.pi * x / L), (x, 0, L))
    Bn = (2 / (n * sp.pi * c)) * sp.integrate(g0 * sp.sin(n * sp.pi * x / L), (x, 0, L))

    series = sp.Integer(0)
    for i in range(1, N + 1):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        w = i * sp.pi * c / L
        series += (Ai * sp.cos(w * t) + Bi * sp.sin(w * t)) * sp.sin(i * sp.pi * x / L)

    return sp.simplify(series), x, t, L


def _wave_series_neumann_expr(vars):
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = sp.sympify(vars.get("L"))
    c = sp.sympify(vars.get("c"))
    N = int(vars.get("n") or 10)

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip() or "0"

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}
    f0 = parse_expr(f0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    g0 = parse_expr(g0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)

    n = sp.Symbol("n", integer=True, nonnegative=True)

    A0 = (1 / L) * sp.integrate(f0, (x, 0, L))
    An = (2 / L) * sp.integrate(f0 * sp.cos(n * sp.pi * x / L), (x, 0, L))
    Bn = (2 / (n * sp.pi * c)) * sp.integrate(g0 * sp.cos(n * sp.pi * x / L), (x, 0, L))

    series = sp.simplify(A0)
    for i in range(1, N + 1):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        w = i * sp.pi * c / L
        series += (Ai * sp.cos(w * t) + Bi * sp.sin(w * t)) * sp.cos(i * sp.pi * x / L)

    return sp.simplify(series), x, t, L


def _wave_series_mixed_expr(vars):
    xname = (vars.get("var1") or "").strip() or "x"
    tname = (vars.get("var2") or "").strip() or "t"
    x = sp.Symbol(xname, real=True)
    t = sp.Symbol(tname, real=True)

    L = sp.sympify(vars.get("L"))
    c = sp.sympify(vars.get("c"))
    N = int(vars.get("n") or 10)

    f0_str = (vars.get("f0") or "").strip()
    g0_str = (vars.get("g0") or "").strip() or "0"

    local_dict = {xname: x, "L": L, "c": c, **SYMPY_FUNCS}
    f0 = parse_expr(f0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)
    g0 = parse_expr(g0_str.replace("^", "**"), local_dict=local_dict, transformations=TRANSFORMATIONS)

    n = sp.Symbol("n", integer=True, nonnegative=True)
    basis = sp.sin((n + sp.Rational(1, 2)) * sp.pi * x / L)

    An = (2 / L) * sp.integrate(f0 * basis, (x, 0, L))
    wn = (n + sp.Rational(1, 2)) * sp.pi * c / L
    Bn = (2 / (wn * L)) * sp.integrate(g0 * basis, (x, 0, L))

    series = sp.Integer(0)
    for i in range(0, N):
        Ai = sp.simplify(An.subs(n, i))
        Bi = sp.simplify(Bn.subs(n, i))
        wi = sp.simplify(wn.subs(n, i))
        series += (Ai * sp.cos(wi * t) + Bi * sp.sin(wi * t)) * sp.sin((i + sp.Rational(1, 2)) * sp.pi * x / L)

    return sp.simplify(series), x, t, L
