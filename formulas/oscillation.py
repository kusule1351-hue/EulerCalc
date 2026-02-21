# formulas/oscillation.py
import math

# Spring-mass: T = 2π sqrt(m/k)
def spring_period(vars):
    T, m, k = vars["T"], vars["m"], vars["k"]

    if T is None:
        return f"T = 2π sqrt(m/k) = 2π*sqrt({m}/{k}) = {2*math.pi*math.sqrt(m/k)}"
    if m is None:
        return f"m = (T^2 k)/(4π^2) = ({T}^2*{k})/(4π^2) = {(T*T*k)/(4*math.pi**2)}"
    if k is None:
        return f"k = (4π^2 m)/T^2 = (4π^2*{m})/{T}^2 = {(4*math.pi**2*m)/(T*T)}"


# Reduced mass: mu = m1 m2/(m1+m2)
def reduced_mass(vars):
    mu, m1, m2 = vars["mu"], vars["m1"], vars["m2"]

    if mu is None:
        return f"μ = m1m2/(m1+m2) = {m1}*{m2}/({m1}+{m2}) = {(m1*m2)/(m1+m2)}"


# Pendulum: T = 2π sqrt(l/g)
def pendulum_period(vars):
    T, l, g = vars["T"], vars["l"], vars["g"]

    if T is None:
        return f"T = 2π sqrt(l/g) = 2π*sqrt({l}/{g}) = {2*math.pi*math.sqrt(l/g)}"
    if l is None:
        return f"l = (T^2 g)/(4π^2) = ({T}^2*{g})/(4π^2) = {(T*T*g)/(4*math.pi**2)}"
    if g is None:
        return f"g = (4π^2 l)/T^2 = (4π^2*{l})/{T}^2 = {(4*math.pi**2*l)/(T*T)}"


# Compound pendulum: T = 2π sqrt(I/(mgl))
def compound_pendulum(vars):
    T, I, m, g, l = vars["T"], vars["I"], vars["m"], vars["g"], vars["l"]

    if T is None:
        return f"T = 2π sqrt(I/(mgl)) = 2π*sqrt({I}/({m}*{g}*{l})) = {2*math.pi*math.sqrt(I/(m*g*l))}"


# Torsional pendulum: T = 2π sqrt(I/C)
def torsional_pendulum(vars):
    T, I, C = vars["T"], vars["I"], vars["C"]

    if T is None:
        return f"T = 2π sqrt(I/C) = 2π*sqrt({I}/{C}) = {2*math.pi*math.sqrt(I/C)}"


# Superposition amplitude: A = sqrt(A1^2 + A2^2 + 2A1A2 cos(phi))
def shm_superposition(vars):
    A, A1, A2, phi = vars["A"], vars["A1"], vars["A2"], vars["phi"]

    if A is None:
        return f"A = sqrt(A1^2 + A2^2 + 2A1A2 cosφ) = {math.sqrt(A1*A1 + A2*A2 + 2*A1*A2*math.cos(phi))}"
