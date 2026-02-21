# formulas/modern.py
import math

# Photon energy: E = h f
def photon_energy(vars):
    E, h, f = vars["E"], vars["h"], vars["f"]

    if E is None:
        return f"E = h f = {h}*{f} = {h*f}"
    if h is None:
        return f"h = E/f = {E}/{f} = {E/f}"
    if f is None:
        return f"f = E/h = {E}/{h} = {E/h}"


# E = hc/lambda
def photon_energy_wavelength(vars):
    E, h, c, lam = vars["E"], vars["h"], vars["c"], vars["lam"]

    if E is None:
        return f"E = hc/λ = {h}*{c}/{lam} = {h*c/lam}"
    if lam is None:
        return f"λ = hc/E = {h}*{c}/{E} = {h*c/E}"


# De Broglie: lambda = h/p
def de_broglie(vars):
    lam, h, p = vars["lam"], vars["h"], vars["p"]

    if lam is None:
        return f"λ = h/p = {h}/{p} = {h/p}"
    if p is None:
        return f"p = h/λ = {h}/{lam} = {h/lam}"
