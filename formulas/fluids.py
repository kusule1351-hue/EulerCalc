# formulas/fluids.py

def pressure(vars):
    P, F, A = vars["P"], vars["F"], vars["A"]

    if P is None:
        return f"P = F/A = {F}/{A} = {F/A}"
    if F is None:
        return f"F = P*A = {P}*{A} = {P*A}"
    if A is None:
        return f"A = F/P = {F}/{P} = {F/P}"


def continuity(vars):
    A1, v1, A2, v2 = vars["A1"], vars["v1"], vars["A2"], vars["v2"]

    # A1 v1 = A2 v2
    if A1 is None:
        return f"A1 = (A2*v2)/v1 = ({A2}*{v2})/{v1} = {(A2*v2)/v1}"
    if v1 is None:
        return f"v1 = (A2*v2)/A1 = ({A2}*{v2})/{A1} = {(A2*v2)/A1}"
    if A2 is None:
        return f"A2 = (A1*v1)/v2 = ({A1}*{v1})/{v2} = {(A1*v1)/v2}"
    if v2 is None:
        return f"v2 = (A1*v1)/A2 = ({A1}*{v1})/{A2} = {(A1*v1)/A2}"


def surface_tension_force(vars):
    F, T, L = vars["F"], vars["T"], vars["L"]

    if F is None:
        return f"F = T*L = {T}*{L} = {T*L}"
    if T is None:
        return f"T = F/L = {F}/{L} = {F/L}"
    if L is None:
        return f"L = F/T = {F}/{T} = {F/T}"


def excess_pressure_drop(vars):
    dP, T, R = vars["dP"], vars["T"], vars["R"]

    if dP is None:
        return f"ΔP = 2T/R = 2*{T}/{R} = {2*T/R}"
    if T is None:
        return f"T = (ΔP*R)/2 = ({dP}*{R})/2 = {(dP*R)/2}"
    if R is None:
        return f"R = 2T/ΔP = 2*{T}/{dP} = {2*T/dP}"


def excess_pressure_bubble(vars):
    dP, T, R = vars["dP"], vars["T"], vars["R"]

    if dP is None:
        return f"ΔP = 4T/R = 4*{T}/{R} = {4*T/R}"
    if T is None:
        return f"T = (ΔP*R)/4 = ({dP}*{R})/4 = {(dP*R)/4}"
    if R is None:
        return f"R = 4T/ΔP = 4*{T}/{dP} = {4*T/dP}"
