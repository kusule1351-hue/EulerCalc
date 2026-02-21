# formulas/electric.py
import math


# -------------------------
# CONSTANTS HELPERS
# -------------------------
def coulomb_constant(e0):
    return 1 / (4 * math.pi * e0)


# -------------------------
# ELECTROSTATICS
# -------------------------

# Coulomb law: F = k q1 q2 / r^2
def coulomb_law(vars):
    F, q1, q2, r, e0 = vars["F"], vars["q1"], vars["q2"], vars["r"], vars["e0"]
    k = coulomb_constant(e0)

    if F is None:
        return f"F = k q1 q2 / r^2 = {k}*{q1}*{q2}/{r}^2 = {k*q1*q2/(r*r)}"
    if q1 is None:
        return f"q1 = F r^2/(k q2) = {F}*{r}^2/({k}*{q2}) = {F*r*r/(k*q2)}"
    if q2 is None:
        return f"q2 = F r^2/(k q1) = {F}*{r}^2/({k}*{q1}) = {F*r*r/(k*q1)}"
    if r is None:
        return f"r = sqrt(k q1 q2 / F) = sqrt({k}*{q1}*{q2}/{F}) = {math.sqrt(k*q1*q2/F)}"


# Electric field: E = F/q
def electric_field(vars):
    E, F, q = vars["E"], vars["F"], vars["q"]

    if E is None:
        return f"E = F/q = {F}/{q} = {F/q}"
    if F is None:
        return f"F = Eq = {E}*{q} = {E*q}"
    if q is None:
        return f"q = F/E = {F}/{E} = {F/E}"


# Field of point charge: E = kq/r^2
def field_point_charge(vars):
    E, q, r, e0 = vars["E"], vars["q"], vars["r"], vars["e0"]
    k = coulomb_constant(e0)

    if E is None:
        return f"E = kq/r^2 = {k}*{q}/{r}^2 = {k*q/(r*r)}"
    if q is None:
        return f"q = E r^2/k = {E}*{r}^2/{k} = {E*r*r/k}"
    if r is None:
        return f"r = sqrt(kq/E) = sqrt({k}*{q}/{E}) = {math.sqrt(k*q/E)}"


# Electric potential: V = kq/r
def electric_potential(vars):
    V, q, r, e0 = vars["V"], vars["q"], vars["r"], vars["e0"]
    k = coulomb_constant(e0)

    if V is None:
        return f"V = kq/r = {k}*{q}/{r} = {k*q/r}"
    if q is None:
        return f"q = Vr/k = {V}*{r}/{k} = {V*r/k}"
    if r is None:
        return f"r = kq/V = {k}*{q}/{V} = {k*q/V}"


# Potential energy: U = k q1 q2 / r
def electric_potential_energy(vars):
    U, q1, q2, r, e0 = vars["U"], vars["q1"], vars["q2"], vars["r"], vars["e0"]
    k = coulomb_constant(e0)

    if U is None:
        return f"U = k q1 q2 / r = {k}*{q1}*{q2}/{r} = {k*q1*q2/r}"
    if q1 is None:
        return f"q1 = U r/(k q2) = {U}*{r}/({k}*{q2}) = {U*r/(k*q2)}"
    if q2 is None:
        return f"q2 = U r/(k q1) = {U}*{r}/({k}*{q1}) = {U*r/(k*q1)}"
    if r is None:
        return f"r = k q1 q2 / U = {k}*{q1}*{q2}/{U} = {k*q1*q2/U}"


# Relation: E = V/d (uniform field)
def uniform_field(vars):
    E, V, d = vars["E"], vars["V"], vars["d"]

    if E is None:
        return f"E = V/d = {V}/{d} = {V/d}"
    if V is None:
        return f"V = Ed = {E}*{d} = {E*d}"
    if d is None:
        return f"d = V/E = {V}/{E} = {V/E}"


# Force on charge in field: F = qE
def force_in_field(vars):
    F, q, E = vars["F"], vars["q"], vars["E"]

    if F is None:
        return f"F = qE = {q}*{E} = {q*E}"
    if q is None:
        return f"q = F/E = {F}/{E} = {F/E}"
    if E is None:
        return f"E = F/q = {F}/{q} = {F/q}"


# Dipole moment: p = qd
def dipole_moment(vars):
    p, q, d = vars["p"], vars["q"], vars["d"]

    if p is None:
        return f"p = qd = {q}*{d} = {q*d}"
    if q is None:
        return f"q = p/d = {p}/{d} = {p/d}"
    if d is None:
        return f"d = p/q = {p}/{q} = {p/q}"


# Torque on dipole: τ = pE sinθ
def dipole_torque(vars):
    tau, p, E, theta = vars["tau"], vars["p"], vars["E"], vars["theta"]

    if tau is None:
        return f"τ = pE sinθ = {p}*{E}*sin({theta}) = {p*E*math.sin(theta)}"
    if p is None:
        return f"p = τ/(E sinθ) = {tau}/({E}*sin({theta})) = {tau/(E*math.sin(theta))}"
    if E is None:
        return f"E = τ/(p sinθ) = {tau}/({p}*sin({theta})) = {tau/(p*math.sin(theta))}"


# Potential energy of dipole: U = -pE cosθ
def dipole_energy(vars):
    U, p, E, theta = vars["U"], vars["p"], vars["E"], vars["theta"]

    if U is None:
        return f"U = -pE cosθ = -{p}*{E}*cos({theta}) = {-p*E*math.cos(theta)}"


# -------------------------
# CURRENT ELECTRICITY
# -------------------------

# Ohm law: V = IR
def ohms_law(vars):
    V, I, R = vars["V"], vars["I"], vars["R"]

    if V is None:
        return f"V = IR = {I}*{R} = {I*R}"
    if I is None:
        return f"I = V/R = {V}/{R} = {V/R}"
    if R is None:
        return f"R = V/I = {V}/{I} = {V/I}"


# Power: P = VI
def power_vi(vars):
    P, V, I = vars["P"], vars["V"], vars["I"]

    if P is None:
        return f"P = VI = {V}*{I} = {V*I}"
    if V is None:
        return f"V = P/I = {P}/{I} = {P/I}"
    if I is None:
        return f"I = P/V = {P}/{V} = {P/V}"


# Power: P = I^2 R
def power_i2r(vars):
    P, I, R = vars["P"], vars["I"], vars["R"]

    if P is None:
        return f"P = I^2R = {I}^2*{R} = {I*I*R}"
    if I is None:
        return f"I = sqrt(P/R) = sqrt({P}/{R}) = {math.sqrt(P/R)}"
    if R is None:
        return f"R = P/I^2 = {P}/{I}^2 = {P/(I*I)}"


# Power: P = V^2/R
def power_v2r(vars):
    P, V, R = vars["P"], vars["V"], vars["R"]

    if P is None:
        return f"P = V^2/R = {V}^2/{R} = {V*V/R}"
    if V is None:
        return f"V = sqrt(PR) = sqrt({P}*{R}) = {math.sqrt(P*R)}"
    if R is None:
        return f"R = V^2/P = {V}^2/{P} = {V*V/P}"


# Resistivity: R = ρL/A
def resistance_resistivity(vars):
    R, rho, L, A = vars["R"], vars["rho"], vars["L"], vars["A"]

    if R is None:
        return f"R = ρL/A = {rho}*{L}/{A} = {rho*L/A}"
    if rho is None:
        return f"ρ = RA/L = {R}*{A}/{L} = {R*A/L}"
    if L is None:
        return f"L = RA/ρ = {R}*{A}/{rho} = {R*A/rho}"
    if A is None:
        return f"A = ρL/R = {rho}*{L}/{R} = {rho*L/R}"


# Current density: J = I/A
def current_density(vars):
    J, I, A = vars["J"], vars["I"], vars["A"]

    if J is None:
        return f"J = I/A = {I}/{A} = {I/A}"
    if I is None:
        return f"I = JA = {J}*{A} = {J*A}"
    if A is None:
        return f"A = I/J = {I}/{J} = {I/J}"


# Drift velocity: I = n q A vd
def drift_velocity(vars):
    I, n, q, A, vd = vars["I"], vars["n"], vars["q"], vars["A"], vars["vd"]

    if I is None:
        return f"I = nqAvd = {n}*{q}*{A}*{vd} = {n*q*A*vd}"
    if vd is None:
        return f"vd = I/(nqA) = {I}/({n}*{q}*{A}) = {I/(n*q*A)}"
    if n is None:
        return f"n = I/(qAvd) = {I}/({q}*{A}*{vd}) = {I/(q*A*vd)}"


# EMF relation: V = E - Ir
def internal_resistance(vars):
    V, E, I, r = vars["V"], vars["E"], vars["I"], vars["r"]

    if V is None:
        return f"V = E - Ir = {E} - {I}*{r} = {E - I*r}"
    if E is None:
        return f"E = V + Ir = {V} + {I}*{r} = {V + I*r}"
    if r is None:
        return f"r = (E-V)/I = ({E}-{V})/{I} = {(E-V)/I}"


# -------------------------
# RESISTORS COMBINATION
# -------------------------
def series_resistance(vars):
    Req, resistances = vars["Req"], vars["resistances"]

    if Req is None:
        return f"Req(series) = sum(R) = {sum(resistances)}"
    return "Series: Req = sum(resistances)"


def parallel_resistance(vars):
    Req, resistances = vars["Req"], vars["resistances"]
    inv_sum = sum(1/r for r in resistances)

    if Req is None:
        return f"Req(parallel) = 1/(Σ(1/R)) = 1/{inv_sum} = {1/inv_sum}"
    return "Parallel: Req = 1/(sum(1/Ri))"


# -------------------------
# CAPACITORS
# -------------------------

# C = Q/V
def capacitance_definition(vars):
    C, Q, V = vars["C"], vars["Q"], vars["V"]

    if C is None:
        return f"C = Q/V = {Q}/{V} = {Q/V}"
    if Q is None:
        return f"Q = CV = {C}*{V} = {C*V}"
    if V is None:
        return f"V = Q/C = {Q}/{C} = {Q/C}"


# Energy capacitor: U = 1/2 C V^2
def capacitor_energy(vars):
    U, C, V = vars["U"], vars["C"], vars["V"]

    if U is None:
        return f"U = 0.5CV^2 = 0.5*{C}*{V}^2 = {0.5*C*V*V}"
    if C is None:
        return f"C = 2U/V^2 = 2*{U}/{V}^2 = {(2*U)/(V*V)}"
    if V is None:
        return f"V = sqrt(2U/C) = sqrt(2*{U}/{C}) = {math.sqrt((2*U)/C)}"


# Energy capacitor: U = Q^2/(2C)
def capacitor_energy_q(vars):
    U, Q, C = vars["U"], vars["Q"], vars["C"]

    if U is None:
        return f"U = Q^2/(2C) = {Q}^2/(2*{C}) = {Q*Q/(2*C)}"
    if Q is None:
        return f"Q = sqrt(2UC) = sqrt(2*{U}*{C}) = {math.sqrt(2*U*C)}"
    if C is None:
        return f"C = Q^2/(2U) = {Q}^2/(2*{U}) = {Q*Q/(2*U)}"


def series_capacitance(vars):
    Ceq, caps = vars["Ceq"], vars["caps"]
    inv_sum = sum(1/c for c in caps)

    if Ceq is None:
        return f"Ceq(series) = 1/(Σ(1/C)) = 1/{inv_sum} = {1/inv_sum}"
    return "Series capacitors: Ceq = 1/(sum(1/Ci))"


def parallel_capacitance(vars):
    Ceq, caps = vars["Ceq"], vars["caps"]

    if Ceq is None:
        return f"Ceq(parallel) = sum(C) = {sum(caps)}"
    return "Parallel capacitors: Ceq = sum(Ci)"


# -------------------------
# RC CIRCUITS
# -------------------------

# Time constant: tau = RC
def rc_time_constant(vars):
    tau, R, C = vars["tau"], vars["R"], vars["C"]

    if tau is None:
        return f"τ = RC = {R}*{C} = {R*C}"
    if R is None:
        return f"R = τ/C = {tau}/{C} = {tau/C}"
    if C is None:
        return f"C = τ/R = {tau}/{R} = {tau/R}"


# Charging capacitor: Q = Q0(1 - e^(-t/RC))
def capacitor_charging(vars):
    Q, Q0, t, R, C = vars["Q"], vars["Q0"], vars["t"], vars["R"], vars["C"]

    if Q is None:
        return f"Q = Q0(1-e^(-t/RC)) = {Q0}*(1-exp(-{t}/({R}*{C}))) = {Q0*(1-math.exp(-t/(R*C)))}"


# Discharging capacitor: Q = Q0 e^(-t/RC)
def capacitor_discharging(vars):
    Q, Q0, t, R, C = vars["Q"], vars["Q0"], vars["t"], vars["R"], vars["C"]

    if Q is None:
        return f"Q = Q0 e^(-t/RC) = {Q0}*exp(-{t}/({R}*{C})) = {Q0*math.exp(-t/(R*C))}"


# -------------------------
# AC CIRCUITS
# -------------------------

# AC voltage: V = V0 sin(wt)
def ac_voltage(vars):
    V, V0, w, t = vars["V"], vars["V0"], vars["w"], vars["t"]

    if V is None:
        return f"V = V0 sin(wt) = {V0}*sin({w}*{t}) = {V0*math.sin(w*t)}"
    if V0 is None:
        return f"V0 = V/sin(wt) = {V}/sin({w}*{t}) = {V/math.sin(w*t)}"


# RMS voltage: Vrms = V0/sqrt(2)
def rms_voltage(vars):
    Vrms, V0 = vars["Vrms"], vars["V0"]

    if Vrms is None:
        return f"Vrms = V0/sqrt(2) = {V0}/sqrt(2) = {V0/math.sqrt(2)}"
    if V0 is None:
        return f"V0 = Vrms*sqrt(2) = {Vrms}*sqrt(2) = {Vrms*math.sqrt(2)}"


# RMS current: Irms = I0/sqrt(2)
def rms_current(vars):
    Irms, I0 = vars["Irms"], vars["I0"]

    if Irms is None:
        return f"Irms = I0/sqrt(2) = {I0}/sqrt(2) = {I0/math.sqrt(2)}"
    if I0 is None:
        return f"I0 = Irms*sqrt(2) = {Irms}*sqrt(2) = {Irms*math.sqrt(2)}"
