# formulas/error_measurement.py

def absolute_error(vars):
    dx, xm, xt = vars["dx"], vars["xm"], vars["xt"]

    if dx is None:
        return f"Δx = |xm-xt| = |{xm}-{xt}| = {abs(xm-xt)}"
    if xm is None:
        return f"xm = xt ± Δx = {xt} ± {dx}"
    if xt is None:
        return f"xt = xm ± Δx = {xm} ± {dx}"


def relative_error(vars):
    rel, dx, xt = vars["rel"], vars["dx"], vars["xt"]

    if rel is None:
        return f"Relative = Δx/xt = {dx}/{xt} = {dx/xt}"
    if dx is None:
        return f"Δx = Relative*xt = {rel}*{xt} = {rel*xt}"
    if xt is None:
        return f"xt = Δx/Relative = {dx}/{rel} = {dx/rel}"


def percentage_error(vars):
    per, dx, xt = vars["per"], vars["dx"], vars["xt"]

    if per is None:
        return f"%Error = (Δx/xt)*100 = ({dx}/{xt})*100 = {(dx/xt)*100}"
    if dx is None:
        return f"Δx = (%Error*xt)/100 = ({per}*{xt})/100 = {(per*xt)/100}"
    if xt is None:
        return f"xt = (Δx*100)/%Error = ({dx}*100)/{per} = {(dx*100)/per}"


def propagation_sum(vars):
    dz, dx, dy = vars["dz"], vars["dx"], vars["dy"]

    if dz is None:
        return f"Δz = Δx + Δy = {dx}+{dy} = {dx+dy}"
    if dx is None:
        return f"Δx = Δz - Δy = {dz}-{dy} = {dz-dy}"
    if dy is None:
        return f"Δy = Δz - Δx = {dz}-{dx} = {dz-dx}"


def propagation_product(vars):
    frac, dz, z, dx, x, dy, y = vars["frac"], vars["dz"], vars["z"], vars["dx"], vars["x"], vars["dy"], vars["y"]

    if frac is None:
        return f"Δz/z = Δx/x + Δy/y = {dx}/{x} + {dy}/{y} = {(dx/x)+(dy/y)}"
