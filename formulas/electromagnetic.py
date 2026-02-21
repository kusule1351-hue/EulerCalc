# formulas/electromagnetic.py
import math


# -----------------------------
# MAGNETIC FIELD FORMULAS
# -----------------------------

# Long straight wire: B = μ0 I / (2πr)
def long_wire_field(vars):
    B, mu0, I, r = vars["B"], vars["mu0"], vars["I"], vars["r"]

    if B is None:
        return f"B = μ0I/(2πr) = {mu0}*{I}/(2π*{r}) = {mu0*I/(2*math.pi*r)}"
    if I is None:
        return f"I = B(2πr)/μ0 = {B}*(2π*{r})/{mu0} = {B*2*math.pi*r/mu0}"
    if r is None:
        return f"r = μ0I/(2πB) = {mu0}*{I}/(2π*{B}) = {mu0*I/(2*math.pi*B)}"


# Magnetic field at center of circular loop: B = μ0 I / (2R)
def loop_field_center(vars):
    B, mu0, I, R = vars["B"], vars["mu0"], vars["I"], vars["R"]

    if B is None:
        return f"B = μ0I/(2R) = {mu0}*{I}/(2*{R}) = {mu0*I/(2*R)}"
    if I is None:
        return f"I = 2RB/μ0 = 2*{R}*{B}/{mu0} = {2*R*B/mu0}"
    if R is None:
        return f"R = μ0I/(2B) = {mu0}*{I}/(2*{B}) = {mu0*I/(2*B)}"


# Solenoid: B = μ0 n I
def solenoid_field(vars):
    B, mu0, n, I = vars["B"], vars["mu0"], vars["n"], vars["I"]

    if B is None:
        return f"B = μ0 n I = {mu0}*{n}*{I} = {mu0*n*I}"
    if I is None:
        return f"I = B/(μ0 n) = {B}/({mu0}*{n}) = {B/(mu0*n)}"
    if n is None:
        return f"n = B/(μ0 I) = {B}/({mu0}*{I}) = {B/(mu0*I)}"


# Toroid: B = μ0 N I / (2πr)
def toroid_field(vars):
    B, mu0, N, I, r = vars["B"], vars["mu0"], vars["N"], vars["I"], vars["r"]

    if B is None:
        return f"B = μ0NI/(2πr) = {mu0}*{N}*{I}/(2π*{r}) = {mu0*N*I/(2*math.pi*r)}"
    if I is None:
        return f"I = B(2πr)/(μ0N) = {B}*(2π*{r})/({mu0}*{N}) = {B*2*math.pi*r/(mu0*N)}"


# Force on moving charge: F = qvB sinθ
def magnetic_force_charge(vars):
    F, q, v, B, theta = vars["F"], vars["q"], vars["v"], vars["B"], vars["theta"]

    if F is None:
        return f"F = qvB sinθ = {q}*{v}*{B}*sin({theta}) = {q*v*B*math.sin(theta)}"
    if B is None:
        return f"B = F/(qv sinθ) = {F}/({q}*{v}*sin({theta})) = {F/(q*v*math.sin(theta))}"


# Force on current carrying wire: F = BIL sinθ
def force_on_wire(vars):
    F, B, I, L, theta = vars["F"], vars["B"], vars["I"], vars["L"], vars["theta"]

    if F is None:
        return f"F = BIL sinθ = {B}*{I}*{L}*sin({theta}) = {B*I*L*math.sin(theta)}"
    if B is None:
        return f"B = F/(IL sinθ) = {F}/({I}*{L}*sin({theta})) = {F/(I*L*math.sin(theta))}"


# Force between two parallel wires: F/L = μ0 I1 I2 / (2πd)
def force_between_wires(vars):
    F, mu0, I1, I2, d, L = vars["F"], vars["mu0"], vars["I1"], vars["I2"], vars["d"], vars["L"]

    if F is None:
        return f"F = (μ0 I1 I2 L)/(2πd) = ({mu0}*{I1}*{I2}*{L})/(2π*{d}) = {mu0*I1*I2*L/(2*math.pi*d)}"


# -----------------------------
# MAGNETIC FLUX & INDUCTION
# -----------------------------

# Magnetic flux: Φ = B A cosθ
def magnetic_flux(vars):
    phi, B, A, theta = vars["phi"], vars["B"], vars["A"], vars["theta"]

    if phi is None:
        return f"Φ = BA cosθ = {B}*{A}*cos({theta}) = {B*A*math.cos(theta)}"
    if B is None:
        return f"B = Φ/(A cosθ) = {phi}/({A}*cos({theta})) = {phi/(A*math.cos(theta))}"
    if A is None:
        return f"A = Φ/(B cosθ) = {phi}/({B}*cos({theta})) = {phi/(B*math.cos(theta))}"


# Faraday law: emf = -N dΦ/dt
def faraday_law(vars):
    emf, N, dphi, dt = vars["emf"], vars["N"], vars["dphi"], vars["dt"]

    if emf is None:
        return f"ε = -N(ΔΦ/Δt) = -{N}*({dphi}/{dt}) = {-N*dphi/dt}"
    if N is None:
        return f"N = -εΔt/ΔΦ = -{emf}*{dt}/{dphi} = {-emf*dt/dphi}"


# Motional emf: emf = B L v
def motional_emf(vars):
    emf, B, L, v = vars["emf"], vars["B"], vars["L"], vars["v"]

    if emf is None:
        return f"ε = BLv = {B}*{L}*{v} = {B*L*v}"
    if v is None:
        return f"v = ε/(BL) = {emf}/({B}*{L}) = {emf/(B*L)}"


# -----------------------------
# INDUCTANCE
# -----------------------------

# Self induced emf: emf = -L dI/dt
def self_induced_emf(vars):
    emf, L, dI, dt = vars["emf"], vars["L"], vars["dI"], vars["dt"]

    if emf is None:
        return f"ε = -L(ΔI/Δt) = -{L}*({dI}/{dt}) = {-L*dI/dt}"
    if L is None:
        return f"L = -εΔt/ΔI = -{emf}*{dt}/{dI} = {-emf*dt/dI}"


# Energy stored in inductor: U = 1/2 L I^2
def inductor_energy(vars):
    U, L, I = vars["U"], vars["L"], vars["I"]

    if U is None:
        return f"U = 0.5LI^2 = 0.5*{L}*{I}^2 = {0.5*L*I*I}"
    if L is None:
        return f"L = 2U/I^2 = 2*{U}/{I}^2 = {(2*U)/(I*I)}"
    if I is None:
        return f"I = sqrt(2U/L) = sqrt(2*{U}/{L}) = {math.sqrt((2*U)/L)}"


# Mutual inductance emf: emf2 = -M dI1/dt
def mutual_inductance(vars):
    emf2, M, dI1, dt = vars["emf2"], vars["M"], vars["dI1"], vars["dt"]

    if emf2 is None:
        return f"ε2 = -M(ΔI1/Δt) = -{M}*({dI1}/{dt}) = {-M*dI1/dt}"
    if M is None:
        return f"M = -ε2Δt/ΔI1 = -{emf2}*{dt}/{dI1} = {-emf2*dt/dI1}"


# -----------------------------
# AC CIRCUITS
# -----------------------------

# Inductive reactance: XL = ωL
def inductive_reactance(vars):
    XL, w, L = vars["XL"], vars["w"], vars["L"]

    if XL is None:
        return f"XL = ωL = {w}*{L} = {w*L}"
    if L is None:
        return f"L = XL/ω = {XL}/{w} = {XL/w}"


# Capacitive reactance: XC = 1/(ωC)
def capacitive_reactance(vars):
    XC, w, C = vars["XC"], vars["w"], vars["C"]

    if XC is None:
        return f"XC = 1/(ωC) = 1/({w}*{C}) = {1/(w*C)}"
    if C is None:
        return f"C = 1/(ωXC) = 1/({w}*{XC}) = {1/(w*XC)}"


# Impedance (RLC series): Z = sqrt(R^2 + (XL - XC)^2)
def impedance_rlc(vars):
    Z, R, XL, XC = vars["Z"], vars["R"], vars["XL"], vars["XC"]

    if Z is None:
        return f"Z = sqrt(R^2+(XL-XC)^2) = sqrt({R}^2+({XL}-{XC})^2) = {math.sqrt(R*R + (XL-XC)**2)}"


# Resonant frequency: f0 = 1/(2π sqrt(LC))
def resonance_frequency(vars):
    f0, L, C = vars["f0"], vars["L"], vars["C"]

    if f0 is None:
        return f"f0 = 1/(2π sqrt(LC)) = 1/(2π*sqrt({L}*{C})) = {1/(2*math.pi*math.sqrt(L*C))}"
    if L is None:
        return f"L = 1/((2πf0)^2 C) = 1/((2π*{f0})^2*{C}) = {1/(((2*math.pi*f0)**2)*C)}"
    if C is None:
        return f"C = 1/((2πf0)^2 L) = 1/((2π*{f0})^2*{L}) = {1/(((2*math.pi*f0)**2)*L)}"


# -----------------------------
# ELECTROMAGNETIC WAVES
# -----------------------------

# Speed of EM wave: c = 1/sqrt(mu0*e0)
def em_wave_speed(vars):
    c, mu0, e0 = vars["c"], vars["mu0"], vars["e0"]

    if c is None:
        return f"c = 1/sqrt(μ0ε0) = 1/sqrt({mu0}*{e0}) = {1/math.sqrt(mu0*e0)}"


# Relation between E and B: E/B = c
def e_b_relation(vars):
    E, B, c = vars["E"], vars["B"], vars["c"]

    if E is None:
        return f"E = Bc = {B}*{c} = {B*c}"
    if B is None:
        return f"B = E/c = {E}/{c} = {E/c}"
    if c is None:
        return f"c = E/B = {E}/{B} = {E/B}"


# Energy density: u = 1/2 ε0 E^2 + 1/2 B^2/μ0
def energy_density(vars):
    u, e0, E, B, mu0 = vars["u"], vars["e0"], vars["E"], vars["B"], vars["mu0"]

    if u is None:
        return f"u = 0.5ε0E^2 + 0.5(B^2/μ0) = {0.5*e0*E*E + 0.5*(B*B/mu0)}"

# -------------------------
# MAXWELL EQUATIONS (INTEGRAL)
# -------------------------

# Gauss law: ΦE = Q/ε0
def gauss_law_electric(vars):
    phiE, Q, e0 = vars["phiE"], vars["Q"], vars["e0"]

    if phiE is None:
        return f"ΦE = Q/ε0 = {Q}/{e0} = {Q/e0}"
    if Q is None:
        return f"Q = ΦE ε0 = {phiE}*{e0} = {phiE*e0}"
    if e0 is None:
        return f"ε0 = Q/ΦE = {Q}/{phiE} = {Q/phiE}"


# Gauss law magnetism: ΦB = 0
def gauss_law_magnetism(vars):
    return "Gauss law for magnetism: ΦB = 0 (no magnetic monopoles)"


# Faraday law: ∮E·dl = - dΦB/dt
def faraday_integral(vars):
    emf, dphiB, dt = vars["emf"], vars["dphiB"], vars["dt"]

    if emf is None:
        return f"ε = -ΔΦB/Δt = -{dphiB}/{dt} = {-dphiB/dt}"
    if dphiB is None:
        return f"ΔΦB = -εΔt = -{emf}*{dt} = {-emf*dt}"
    if dt is None:
        return f"Δt = -ΔΦB/ε = -{dphiB}/{emf} = {-dphiB/emf}"


# Ampere-Maxwell law: ∮B·dl = μ0(I + ε0 dΦE/dt)
def ampere_maxwell(vars):
    left, mu0, I, e0, dphiE, dt = vars["left"], vars["mu0"], vars["I"], vars["e0"], vars["dphiE"], vars["dt"]

    if left is None:
        return f"∮B·dl = μ0(I + ε0 ΔΦE/Δt) = {mu0}*({I} + {e0}*{dphiE}/{dt}) = {mu0*(I + e0*dphiE/dt)}"
    if I is None:
        return f"I = (∮B·dl)/μ0 - ε0 ΔΦE/Δt = {left}/{mu0} - {e0}*{dphiE}/{dt} = {(left/mu0) - (e0*dphiE/dt)}"


# -------------------------
# TRANSFORMER
# -------------------------

# Ideal transformer: Vp/Vs = Np/Ns
def transformer_voltage(vars):
    Vp, Vs, Np, Ns = vars["Vp"], vars["Vs"], vars["Np"], vars["Ns"]

    if Vp is None:
        return f"Vp = Vs*(Np/Ns) = {Vs}*({Np}/{Ns}) = {Vs*(Np/Ns)}"
    if Vs is None:
        return f"Vs = Vp*(Ns/Np) = {Vp}*({Ns}/{Np}) = {Vp*(Ns/Np)}"
    if Np is None:
        return f"Np = (Vp/Vs)*Ns = ({Vp}/{Vs})*{Ns} = {(Vp/Vs)*Ns}"
    if Ns is None:
        return f"Ns = (Vs/Vp)*Np = ({Vs}/{Vp})*{Np} = {(Vs/Vp)*Np}"


# Ideal transformer: Ip/Is = Ns/Np
def transformer_current(vars):
    Ip, Is, Np, Ns = vars["Ip"], vars["Is"], vars["Np"], vars["Ns"]

    if Ip is None:
        return f"Ip = Is*(Ns/Np) = {Is}*({Ns}/{Np}) = {Is*(Ns/Np)}"
    if Is is None:
        return f"Is = Ip*(Np/Ns) = {Ip}*({Np}/{Ns}) = {Ip*(Np/Ns)}"


# -------------------------
# POYNTING VECTOR (MAGNITUDE)
# -------------------------

# S = (1/μ0) E B
def poynting_vector(vars):
    S, mu0, E, B = vars["S"], vars["mu0"], vars["E"], vars["B"]

    if S is None:
        return f"S = (1/μ0)EB = (1/{mu0})*{E}*{B} = {(E*B)/mu0}"
    if E is None:
        return f"E = Sμ0/B = {S}*{mu0}/{B} = {(S*mu0)/B}"
    if B is None:
        return f"B = Sμ0/E = {S}*{mu0}/{E} = {(S*mu0)/E}"


# -------------------------
# INDUCTANCE (SOLENOID)
# -------------------------

# Solenoid inductance: L = μ0 N^2 A / l
def solenoid_inductance(vars):
    L, mu0, N, A, l = vars["L"], vars["mu0"], vars["N"], vars["A"], vars["l"]

    if L is None:
        return f"L = μ0 N^2 A / l = {mu0}*{N}^2*{A}/{l} = {mu0*N*N*A/l}"
    if N is None:
        return f"N = sqrt(L l/(μ0A)) = sqrt({L}*{l}/({mu0}*{A})) = {math.sqrt(L*l/(mu0*A))}"
    if A is None:
        return f"A = L l/(μ0N^2) = {L}*{l}/({mu0}*{N}^2) = {L*l/(mu0*N*N)}"
    if l is None:
        return f"l = μ0N^2A/L = {mu0}*{N}^2*{A}/{L} = {mu0*N*N*A/L}"


# -------------------------
# RL / LC / RLC CIRCUITS
# -------------------------

# RL time constant: tau = L/R
def rl_time_constant(vars):
    tau, L, R = vars["tau"], vars["L"], vars["R"]

    if tau is None:
        return f"τ = L/R = {L}/{R} = {L/R}"
    if L is None:
        return f"L = τR = {tau}*{R} = {tau*R}"
    if R is None:
        return f"R = L/τ = {L}/{tau} = {L/tau}"


# LC frequency: f = 1/(2π sqrt(LC))
def lc_frequency(vars):
    f, L, C = vars["f"], vars["L"], vars["C"]

    if f is None:
        return f"f = 1/(2π sqrt(LC)) = {1/(2*math.pi*math.sqrt(L*C))}"
    if L is None:
        return f"L = 1/((2πf)^2 C) = {1/(((2*math.pi*f)**2)*C)}"
    if C is None:
        return f"C = 1/((2πf)^2 L) = {1/(((2*math.pi*f)**2)*L)}"


# RLC impedance: Z = sqrt(R^2 + (ωL - 1/ωC)^2)
def rlc_impedance(vars):
    Z, R, w, L, C = vars["Z"], vars["R"], vars["w"], vars["L"], vars["C"]

    if Z is None:
        return f"Z = sqrt(R^2+(ωL-1/ωC)^2) = {math.sqrt(R*R + (w*L - 1/(w*C))**2)}"


# Phase angle: tanφ = (XL - XC)/R
def phase_angle(vars):
    phi, R, XL, XC = vars["phi"], vars["R"], vars["XL"], vars["XC"]

    if phi is None:
        return f"φ = arctan((XL-XC)/R) = atan(({XL}-{XC})/{R}) = {math.atan((XL-XC)/R)}"


# Quality factor: Q = ω0 L / R
def quality_factor(vars):
    Q, w0, L, R = vars["Q"], vars["w0"], vars["L"], vars["R"]

    if Q is None:
        return f"Q = ω0L/R = {w0}*{L}/{R} = {w0*L/R}"
    if R is None:
        return f"R = ω0L/Q = {w0}*{L}/{Q} = {w0*L/Q}"

