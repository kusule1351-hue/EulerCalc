# formulas/magnetism.py
import math

# Magnetic force: F = q v B sin(theta)
def magnetic_force(vars):
    F, q, v, B, theta = vars["F"], vars["q"], vars["v"], vars["B"], vars["theta"]

    if F is None:
        return f"F = qvB sinθ = {q}*{v}*{B}*sin({theta}) = {q*v*B*math.sin(theta)}"
    if q is None:
        return f"q = F/(vB sinθ) = {F}/({v}*{B}*sin({theta})) = {F/(v*B*math.sin(theta))}"
    if v is None:
        return f"v = F/(qB sinθ) = {F}/({q}*{B}*sin({theta})) = {F/(q*B*math.sin(theta))}"
    if B is None:
        return f"B = F/(qv sinθ) = {F}/({q}*{v}*sin({theta})) = {F/(q*v*math.sin(theta))}"


# Lorentz force magnitude: F = q(E + vB) (simplified)
def lorentz_force(vars):
    F, q, E, v, B = vars["F"], vars["q"], vars["E"], vars["v"], vars["B"]

    if F is None:
        return f"F = q(E + vB) = {q}*({E}+{v}*{B}) = {q*(E+v*B)}"
    if q is None:
        return f"q = F/(E+vB) = {F}/({E}+{v}*{B}) = {F/(E+v*B)}"


# Faraday law: emf = -dPhi/dt
def faraday(vars):
    emf, dphi, dt = vars["emf"], vars["dphi"], vars["dt"]

    if emf is None:
        return f"ε = -(ΔΦ/Δt) = -({dphi}/{dt}) = {-dphi/dt}"
    if dphi is None:
        return f"ΔΦ = -εΔt = -{emf}*{dt} = {-emf*dt}"
    if dt is None:
        return f"Δt = -(ΔΦ/ε) = -({dphi}/{emf}) = {-dphi/emf}"


# Long straight wire: B = mu0 I/(2πr)
def long_wire_field(vars):
    B, mu0, I, r = vars["B"], vars["mu0"], vars["I"], vars["r"]

    if B is None:
        return f"B = μ0I/(2πr) = {mu0}*{I}/(2π*{r}) = {mu0*I/(2*math.pi*r)}"
    if I is None:
        return f"I = (B 2πr)/μ0 = ({B}*2π*{r})/{mu0} = {(B*2*math.pi*r)/mu0}"
    if r is None:
        return f"r = μ0I/(2πB) = {mu0}*{I}/(2π*{B}) = {mu0*I/(2*math.pi*B)}"


# Inductor energy: U = 1/2 L I^2
def inductor_energy(vars):
    U, L, I = vars["U"], vars["L"], vars["I"]

    if U is None:
        return f"U = 0.5*L*I^2 = 0.5*{L}*{I}^2 = {0.5*L*I*I}"
    if L is None:
        return f"L = 2U/I^2 = 2*{U}/{I}^2 = {(2*U)/(I*I)}"
    if I is None:
        return f"I = sqrt(2U/L) = sqrt(2*{U}/{L}) = {math.sqrt((2*U)/L)}"

def lhopital_limit(vars):
    expr = parse_expression(vars["expr"])
    var_str = vars["var"].strip()

    if var_str == "":
        return "❌ Error: var is empty. Example: var = x"

    var = sp.Symbol(var_str)

    point = vars["point"]
    direction = vars["dir"].strip()

    if direction not in ["", "+", "-"]:
        return "❌ dir must be + or - (or leave empty)."

    # Split numerator/denominator
    num, den = sp.fraction(expr)

    # Evaluate direct limit first
    try:
        if direction == "":
            L_num = sp.limit(num, var, point)
            L_den = sp.limit(den, var, point)
        else:
            L_num = sp.limit(num, var, point, dir=direction)
            L_den = sp.limit(den, var, point, dir=direction)
    except Exception as e:
        return f"❌ Cannot evaluate limit: {e}"

    # Check indeterminate forms
    indeterminate = False
    if (L_num == 0 and L_den == 0):
        indeterminate = True
    if (L_num in [sp.oo, -sp.oo] and L_den in [sp.oo, -sp.oo]):
        indeterminate = True

    if not indeterminate:
        # Normal limit works
        result = sp.limit(expr, var, point) if direction == "" else sp.limit(expr, var, point, dir=direction)
        return (
            f"Direct limit worked.\n\n"
            f"lim({var}→{point}{direction}) ({sp.pretty(expr)}) =\n"
            f"{sp.pretty(result)}"
        )

    # Apply L'Hôpital rule
    steps = []
    current_num = num
    current_den = den

    for i in range(1, 6):  # max 5 iterations
        dnum = sp.diff(current_num, var)
        dden = sp.diff(current_den, var)

        steps.append(f"Step {i}:")
        steps.append(f"d/d{var}(numerator) = {sp.pretty(dnum)}")
        steps.append(f"d/d{var}(denominator) = {sp.pretty(dden)}\n")

        current_num, current_den = dnum, dden
        new_expr = current_num / current_den

        try:
            if direction == "":
                L_new_num = sp.limit(current_num, var, point)
                L_new_den = sp.limit(current_den, var, point)
            else:
                L_new_num = sp.limit(current_num, var, point, dir=direction)
                L_new_den = sp.limit(current_den, var, point, dir=direction)

            if not ((L_new_num == 0 and L_new_den == 0) or
                    (L_new_num in [sp.oo, -sp.oo] and L_new_den in [sp.oo, -sp.oo])):

                result = sp.limit(new_expr, var, point) if direction == "" else sp.limit(new_expr, var, point, dir=direction)

                return (
                    "L'Hôpital Rule Applied (Auto Mode)\n\n"
                    f"Original:\n{sp.pretty(expr)}\n\n" +
                    "\n".join(steps) +
                    f"\nFinal limit:\nlim({var}→{point}{direction}) = {sp.pretty(result)}"
                )

        except:
            pass

    return (
        "❌ L'Hôpital could not resolve after 5 iterations.\n"
        "Try normal limit or simplify expression."
    )

