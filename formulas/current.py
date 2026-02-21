# formulas/current.py

def ohm(vars):
    V, I, R = vars["V"], vars["I"], vars["R"]

    if V is None:
        return f"V = IR = {I}*{R} = {I*R}"
    if I is None:
        return f"I = V/R = {V}/{R} = {V/R}"
    if R is None:
        return f"R = V/I = {V}/{I} = {V/I}"
