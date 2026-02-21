# formulas/capacitance.py

def capacitance(vars):
    C, Q, V = vars["C"], vars["Q"], vars["V"]

    if C is None:
        return f"C = Q/V = {Q}/{V} = {Q/V}"
    if Q is None:
        return f"Q = CV = {C}*{V} = {C*V}"
    if V is None:
        return f"V = Q/C = {Q}/{C} = {Q/C}"

def cap_energy(vars):
    U, C, V = vars["U"], vars["C"], vars["V"]

    if U is None:
        return f"U = 1/2 C V^2 = 0.5*{C}*{V}^2 = {0.5*C*V*V}"
    if C is None:
        return f"C = 2U/V^2 = 2*{U}/{V}^2 = {(2*U)/(V*V)}"
    if V is None:
        return f"V = sqrt(2U/C) = sqrt(2*{U}/{C})"
