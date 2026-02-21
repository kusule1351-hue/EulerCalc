# formulas/thermo.py
import math

def first_law(vars):
    dU, Q, W = vars["dU"], vars["Q"], vars["W"]
    if dU is None:
        return f"ΔU = Q - W = {Q} - {W} = {Q-W}"
    if Q is None:
        return f"Q = ΔU + W = {dU} + {W} = {dU+W}"
    if W is None:
        return f"W = Q - ΔU = {Q} - {dU} = {Q-dU}"


def isothermal_work(vars):
    W, n, R, T, Vf, Vi = vars["W"], vars["n"], vars["R"], vars["T"], vars["Vf"], vars["Vi"]
    if W is None:
        return f"W = nRT ln(Vf/Vi) = {n}*{R}*{T}*ln({Vf}/{Vi}) = {n*R*T*math.log(Vf/Vi)}"


# ---------------- WAVES ----------------
def string_wave_speed(vars):
    v, T, mu = vars["v"], vars["T"], vars["mu"]
    if v is None:
        return f"v = sqrt(T/mu) = sqrt({T}/{mu}) = {math.sqrt(T/mu)}"
    if T is None:
        return f"T = v^2*mu = {v}^2*{mu} = {v*v*mu}"
    if mu is None:
        return f"mu = T/v^2 = {T}/{v}^2 = {T/(v*v)}"


def power_transmitted(vars):
    P, f, A, mu, v = vars["P"], vars["f"], vars["A"], vars["mu"], vars["v"]

    if P is None:
        return f"P = 2π^2 f^2 A^2 μ v = {2*(math.pi**2)*(f**2)*(A**2)*mu*v}"
    if f is None:
        return f"f = sqrt(P/(2π^2 A^2 μ v))"
    if A is None:
        return f"A = sqrt(P/(2π^2 f^2 μ v))"
    if mu is None:
        return f"μ = P/(2π^2 f^2 A^2 v)"
    if v is None:
        return f"v = P/(2π^2 f^2 A^2 μ)"


def standing_wave(vars):
    fn, n, v, L = vars["fn"], vars["n"], vars["v"], vars["L"]

    if fn is None:
        return f"fn = n v/(2L) = {n}*{v}/(2*{L}) = {(n*v)/(2*L)}"
    if n is None:
        return f"n = (2L fn)/v = (2*{L}*{fn})/{v} = {(2*L*fn)/v}"
    if v is None:
        return f"v = (2L fn)/n = (2*{L}*{fn})/{n} = {(2*L*fn)/n}"
    if L is None:
        return f"L = (n v)/(2 fn) = ({n}*{v})/(2*{fn}) = {(n*v)/(2*fn)}"

# -------------------------
# IDEAL GAS
# -------------------------

# PV = nRT
def ideal_gas(vars):
    P, V, n, R, T = vars["P"], vars["V"], vars["n"], vars["R"], vars["T"]

    if P is None:
        return f"P = nRT/V = {n}*{R}*{T}/{V} = {n*R*T/V}"
    if V is None:
        return f"V = nRT/P = {n}*{R}*{T}/{P} = {n*R*T/P}"
    if n is None:
        return f"n = PV/RT = {P}*{V}/({R}*{T}) = {P*V/(R*T)}"
    if T is None:
        return f"T = PV/(nR) = {P}*{V}/({n}*{R}) = {P*V/(n*R)}"


# -------------------------
# FIRST LAW
# -------------------------

# ΔU = Q - W
def first_law(vars):
    dU, Q, W = vars["dU"], vars["Q"], vars["W"]

    if dU is None:
        return f"ΔU = Q - W = {Q} - {W} = {Q-W}"
    if Q is None:
        return f"Q = ΔU + W = {dU} + {W} = {dU+W}"
    if W is None:
        return f"W = Q - ΔU = {Q} - {dU} = {Q-dU}"


# -------------------------
# WORK DONE
# -------------------------

# Isothermal work: W = nRT ln(Vf/Vi)
def isothermal_work(vars):
    W, n, R, T, Vf, Vi = vars["W"], vars["n"], vars["R"], vars["T"], vars["Vf"], vars["Vi"]

    if W is None:
        return f"W = nRT ln(Vf/Vi) = {n}*{R}*{T}*ln({Vf}/{Vi}) = {n*R*T*math.log(Vf/Vi)}"


# Adiabatic: PV^γ = constant
def adiabatic_relation(vars):
    P1, V1, P2, V2, gamma = vars["P1"], vars["V1"], vars["P2"], vars["V2"], vars["gamma"]

    if P2 is None:
        return f"P2 = P1*(V1/V2)^γ = {P1}*({V1}/{V2})^{gamma} = {P1*((V1/V2)**gamma)}"
    if V2 is None:
        return f"V2 = V1*(P1/P2)^(1/γ) = {V1}*({P1}/{P2})^(1/{gamma}) = {V1*((P1/P2)**(1/gamma))}"


# Adiabatic temperature relation: TV^(γ-1)=constant
def adiabatic_temp_relation(vars):
    T1, V1, T2, V2, gamma = vars["T1"], vars["V1"], vars["T2"], vars["V2"], vars["gamma"]

    if T2 is None:
        return f"T2 = T1*(V1/V2)^(γ-1) = {T1}*({V1}/{V2})^{gamma-1} = {T1*((V1/V2)**(gamma-1))}"
    if V2 is None:
        return f"V2 = V1*(T1/T2)^(1/(γ-1)) = {V1}*({T1}/{T2})^(1/({gamma}-1)) = {V1*((T1/T2)**(1/(gamma-1)))}"


# -------------------------
# HEAT CAPACITY
# -------------------------

# Q = mcΔT
def heat_capacity(vars):
    Q, m, c, dT = vars["Q"], vars["m"], vars["c"], vars["dT"]

    if Q is None:
        return f"Q = mcΔT = {m}*{c}*{dT} = {m*c*dT}"
    if m is None:
        return f"m = Q/(cΔT) = {Q}/({c}*{dT}) = {Q/(c*dT)}"
    if c is None:
        return f"c = Q/(mΔT) = {Q}/({m}*{dT}) = {Q/(m*dT)}"
    if dT is None:
        return f"ΔT = Q/(mc) = {Q}/({m}*{c}) = {Q/(m*c)}"


# Latent heat: Q = mL
def latent_heat(vars):
    Q, m, L = vars["Q"], vars["m"], vars["L"]

    if Q is None:
        return f"Q = mL = {m}*{L} = {m*L}"
    if L is None:
        return f"L = Q/m = {Q}/{m} = {Q/m}"


# -------------------------
# ENTROPY
# -------------------------

# Entropy: ΔS = Qrev/T
def entropy(vars):
    dS, Qrev, T = vars["dS"], vars["Qrev"], vars["T"]

    if dS is None:
        return f"ΔS = Qrev/T = {Qrev}/{T} = {Qrev/T}"
    if Qrev is None:
        return f"Qrev = ΔS*T = {dS}*{T} = {dS*T}"
    if T is None:
        return f"T = Qrev/ΔS = {Qrev}/{dS} = {Qrev/dS}"


# Isothermal entropy change: ΔS = nR ln(Vf/Vi)
def isothermal_entropy(vars):
    dS, n, R, Vf, Vi = vars["dS"], vars["n"], vars["R"], vars["Vf"], vars["Vi"]

    if dS is None:
        return f"ΔS = nR ln(Vf/Vi) = {n}*{R}*ln({Vf}/{Vi}) = {n*R*math.log(Vf/Vi)}"


# -------------------------
# HEAT ENGINE
# -------------------------

# Efficiency: η = W/Qh
def efficiency(vars):
    eta, W, Qh = vars["eta"], vars["W"], vars["Qh"]

    if eta is None:
        return f"η = W/Qh = {W}/{Qh} = {W/Qh}"
    if W is None:
        return f"W = ηQh = {eta}*{Qh} = {eta*Qh}"


# Carnot efficiency: η = 1 - Tc/Th
def carnot_efficiency(vars):
    eta, Tc, Th = vars["eta"], vars["Tc"], vars["Th"]

    if eta is None:
        return f"η = 1 - Tc/Th = 1 - {Tc}/{Th} = {1 - Tc/Th}"
    if Tc is None:
        return f"Tc = Th(1-η) = {Th}*(1-{eta}) = {Th*(1-eta)}"
    if Th is None:
        return f"Th = Tc/(1-η) = {Tc}/(1-{eta}) = {Tc/(1-eta)}"


# -------------------------
# RMS SPEEDS (KINETIC THEORY)
# -------------------------

# Vrms = sqrt(3RT/M)
def rms_speed(vars):
    vrms, R, T, M = vars["vrms"], vars["R"], vars["T"], vars["M"]

    if vrms is None:
        return f"Vrms = sqrt(3RT/M) = sqrt(3*{R}*{T}/{M}) = {math.sqrt(3*R*T/M)}"
    if T is None:
        return f"T = (vrms^2 M)/(3R) = ({vrms}^2*{M})/(3*{R}) = {(vrms*vrms*M)/(3*R)}"
