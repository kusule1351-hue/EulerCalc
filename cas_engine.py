import sympy as sp

# SymPy locals (pi, e, trig, sqrt гэх мэт)
LOCALS = {
    "pi": sp.pi,
    "e": sp.E,
    "oo": sp.oo,
    "inf": sp.oo,
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "sec": sp.sec,
    "csc": sp.csc,
    "cot": sp.cot,
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "sinh": sp.sinh,
    "cosh": sp.cosh,
    "tanh": sp.tanh,
    "sqrt": sp.sqrt,
    "ln": sp.log,
    "log": sp.log,
    "exp": sp.exp,
}

def parse_expr(expr: str):
    expr = (expr or "").strip().replace("^", "**")
    if not expr:
        raise ValueError("Empty expression")
    return sp.sympify(expr, locals=LOCALS)

def parse_symbol(name: str):
    name = (name or "x").strip()
    return sp.Symbol(name)

def run_cas(mode: str, expr: str, var: str = "x", a: str = "", b: str = "") -> str:
    x = parse_symbol(var)
    E = parse_expr(expr)

    mode = (mode or "").lower()

    if mode == "simplify":
        out = sp.simplify(E)

    elif mode == "expand":
        out = sp.expand(E)

    elif mode == "factor":
        out = sp.factor(E)

    elif mode == "diff":
        out = sp.diff(E, x)

    elif mode == "integrate":
        # a,b өгвөл definite integral
        if (a or "").strip() and (b or "").strip():
            A = parse_expr(a)
            B = parse_expr(b)
            out = sp.integrate(E, (x, A, B))
        else:
            out = sp.integrate(E, x)

    elif mode == "solve":
        # expr=0 гэж үзээд solve
        out = sp.solve(sp.Eq(E, 0), x)

    elif mode == "limit":
        if not (a or "").strip():
            raise ValueError("Limit needs 'a' (point). Example: a=0")
        A = parse_expr(a)
        out = sp.limit(E, x, A)

    else:
        raise ValueError(f"Unknown mode: {mode}")

    # Pretty text (terminal-like)
    return sp.pretty(out, use_unicode=True)