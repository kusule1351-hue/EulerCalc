# formulas/semiconductor.py
import math

def conductivity(vars):
    sigma, n, q, mu = vars["sigma"], vars["n"], vars["q"], vars["mu"]

    if sigma is None:
        return f"σ = n q μ = {n}*{q}*{mu} = {n*q*mu}"
    if n is None:
        return f"n = σ/(qμ) = {sigma}/({q}*{mu}) = {sigma/(q*mu)}"
    if q is None:
        return f"q = σ/(nμ) = {sigma}/({n}*{mu}) = {sigma/(n*mu)}"
    if mu is None:
        return f"μ = σ/(nq) = {sigma}/({n}*{q}) = {sigma/(n*q)}"


def resistivity(vars):
    rho, sigma = vars["rho"], vars["sigma"]

    if rho is None:
        return f"ρ = 1/σ = 1/{sigma} = {1/sigma}"
    if sigma is None:
        return f"σ = 1/ρ = 1/{rho} = {1/rho}"


def shockley_diode(vars):
    I, I0, q, V, k, T = vars["I"], vars["I0"], vars["q"], vars["V"], vars["k"], vars["T"]

    if I is None:
        return f"I = I0*(exp(qV/kT)-1) = {I0}*(exp({q}*{V}/({k}*{T}))-1) = {I0*(math.exp(q*V/(k*T))-1)}"


def transistor_relation(vars):
    IE, IB, IC = vars["IE"], vars["IB"], vars["IC"]

    if IE is None:
        return f"IE = IB + IC = {IB}+{IC} = {IB+IC}"
    if IB is None:
        return f"IB = IE - IC = {IE}-{IC} = {IE-IC}"
    if IC is None:
        return f"IC = IE - IB = {IE}-{IB} = {IE-IB}"


def current_gain(vars):
    beta, IC, IB = vars["beta"], vars["IC"], vars["IB"]

    if beta is None:
        return f"β = IC/IB = {IC}/{IB} = {IC/IB}"
    if IC is None:
        return f"IC = β*IB = {beta}*{IB} = {beta*IB}"
    if IB is None:
        return f"IB = IC/β = {IC}/{beta} = {IC/beta}"
