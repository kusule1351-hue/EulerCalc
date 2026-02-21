# formulas/electrostatics.py

def coulomb_force(vars):
    F, k, q1, q2, r = vars["F"], vars["k"], vars["q1"], vars["q2"], vars["r"]
    if F is None:
        return f"F = k q1 q2 / r^2 = {k}*{q1}*{q2}/{r}^2 = {k*q1*q2/(r*r)}"

def e_field(vars):
    E, F, q = vars["E"], vars["F"], vars["q"]
    if E is None:
        return f"E = F/q = {F}/{q} = {F/q}"
    if F is None:
        return f"F = Eq = {E}*{q} = {E*q}"
    if q is None:
        return f"q = F/E = {F}/{E} = {F/E}"

def potential_energy(vars):
    U, k, q1, q2, r = vars["U"], vars["k"], vars["q1"], vars["q2"], vars["r"]
    if U is None:
        return f"U = k q1 q2 / r = {k}*{q1}*{q2}/{r} = {k*q1*q2/r}"
