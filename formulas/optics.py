# formulas/optics.py
import math

# Lens formula: 1/f = 1/v - 1/u
def lens_formula(vars):
    f, v, u = vars["f"], vars["v"], vars["u"]

    if f is None:
        return f"f = 1/(1/v - 1/u) = 1/(1/{v} - 1/{u}) = {1/(1/v - 1/u)}"
    if v is None:
        return f"v = 1/(1/f + 1/u) = 1/(1/{f} + 1/{u}) = {1/(1/f + 1/u)}"
    if u is None:
        return f"u = 1/(1/v - 1/f) = 1/(1/{v} - 1/{f}) = {1/(1/v - 1/f)}"


# Magnification: M = v/u
def magnification(vars):
    M, v, u = vars["M"], vars["v"], vars["u"]

    if M is None:
        return f"M = v/u = {v}/{u} = {v/u}"
    if v is None:
        return f"v = M*u = {M}*{u} = {M*u}"
    if u is None:
        return f"u = v/M = {v}/{M} = {v/M}"


# Path difference: dx = d sin(theta)
def path_difference(vars):
    dx, d, theta = vars["dx"], vars["d"], vars["theta"]

    if dx is None:
        return f"Δx = d sinθ = {d}*sin({theta}) = {d*math.sin(theta)}"
    if d is None:
        return f"d = Δx/sinθ = {dx}/sin({theta}) = {dx/math.sin(theta)}"


# Constructive interference: dx = nλ
def constructive(vars):
    dx, n, lam = vars["dx"], vars["n"], vars["lam"]

    if dx is None:
        return f"Δx = nλ = {n}*{lam} = {n*lam}"
    if lam is None:
        return f"λ = Δx/n = {dx}/{n} = {dx/n}"
    if n is None:
        return f"n = Δx/λ = {dx}/{lam} = {dx/lam}"


# Destructive interference: dx = (n+0.5)λ
def destructive(vars):
    dx, n, lam = vars["dx"], vars["n"], vars["lam"]

    if dx is None:
        return f"Δx = (n+0.5)λ = ({n}+0.5)*{lam} = {(n+0.5)*lam}"
    if lam is None:
        return f"λ = Δx/(n+0.5) = {dx}/({n}+0.5) = {dx/(n+0.5)}"
    if n is None:
        return f"n = (Δx/λ)-0.5 = ({dx}/{lam})-0.5 = {(dx/lam)-0.5}"


# Diffraction grating: d sin(theta) = nλ
def diffraction_grating(vars):
    d, theta, n, lam = vars["d"], vars["theta"], vars["n"], vars["lam"]

    if lam is None:
        return f"λ = d sinθ / n = {d}*sin({theta})/{n} = {(d*math.sin(theta))/n}"
    if d is None:
        return f"d = nλ/sinθ = {n}*{lam}/sin({theta}) = {(n*lam)/math.sin(theta)}"
