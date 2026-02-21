# formulas/communication.py

def am_modulation_index(vars):
    m, Am, Ac = vars["m"], vars["Am"], vars["Ac"]

    if m is None:
        return f"m = Am/Ac = {Am}/{Ac} = {Am/Ac}"
    if Am is None:
        return f"Am = m*Ac = {m}*{Ac} = {m*Ac}"
    if Ac is None:
        return f"Ac = Am/m = {Am}/{m} = {Am/m}"


def am_total_power(vars):
    Pt, Pc, m = vars["Pt"], vars["Pc"], vars["m"]

    if Pt is None:
        return f"Pt = Pc(1+m^2/2) = {Pc}*(1+{m}^2/2) = {Pc*(1+(m*m)/2)}"
    if Pc is None:
        return f"Pc = Pt/(1+m^2/2) = {Pt}/(1+{m}^2/2) = {Pt/(1+(m*m)/2)}"


def am_bandwidth(vars):
    BW, fm = vars["BW"], vars["fm"]

    if BW is None:
        return f"BW = 2fm = 2*{fm} = {2*fm}"
    if fm is None:
        return f"fm = BW/2 = {BW}/2 = {BW/2}"


def fm_deviation(vars):
    df, kf, Am = vars["df"], vars["kf"], vars["Am"]

    if df is None:
        return f"Δf = kf*Am = {kf}*{Am} = {kf*Am}"
    if kf is None:
        return f"kf = Δf/Am = {df}/{Am} = {df/Am}"
    if Am is None:
        return f"Am = Δf/kf = {df}/{kf} = {df/kf}"


def fm_bandwidth(vars):
    BW, df, fm = vars["BW"], vars["df"], vars["fm"]

    if BW is None:
        return f"BW ≈ 2(Δf+fm) = 2*({df}+{fm}) = {2*(df+fm)}"
    if df is None:
        return f"Δf = (BW/2) - fm = ({BW}/2)-{fm} = {(BW/2)-fm}"
    if fm is None:
        return f"fm = (BW/2) - Δf = ({BW}/2)-{df} = {(BW/2)-df}"
