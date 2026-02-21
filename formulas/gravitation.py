# formulas/gravitation.py
import math

def newton_gravitation(vars):
    F, G, m1, m2, r = vars["F"], vars["G"], vars["m1"], vars["m2"], vars["r"]

    if F is None:
        return f"F = G m1 m2 / r^2 = {G}*{m1}*{m2}/{r}^2 = {G*m1*m2/(r*r)}"
    if G is None:
        return f"G = F r^2 / (m1 m2) = {F}*{r}^2/({m1}*{m2}) = {F*r*r/(m1*m2)}"
    if m1 is None:
        return f"m1 = F r^2/(G m2) = {F}*{r}^2/({G}*{m2}) = {F*r*r/(G*m2)}"
    if m2 is None:
        return f"m2 = F r^2/(G m1) = {F}*{r}^2/({G}*{m1}) = {F*r*r/(G*m1)}"
    if r is None:
        return f"r = sqrt(G m1 m2 / F) = sqrt({G}*{m1}*{m2}/{F}) = {math.sqrt(G*m1*m2/F)}"


def gravitational_potential_energy(vars):
    U, G, m1, m2, r = vars["U"], vars["G"], vars["m1"], vars["m2"], vars["r"]

    if U is None:
        return f"U = -G m1 m2 / r = -{G}*{m1}*{m2}/{r} = {-G*m1*m2/r}"
    if G is None:
        return f"G = -U r/(m1 m2) = -{U}*{r}/({m1}*{m2}) = {-U*r/(m1*m2)}"
    if r is None:
        return f"r = -G m1 m2 / U = -{G}*{m1}*{m2}/{U} = {-G*m1*m2/U}"


def escape_velocity(vars):
    ve, G, M, R = vars["ve"], vars["G"], vars["M"], vars["R"]

    if ve is None:
        return f"ve = sqrt(2GM/R) = sqrt(2*{G}*{M}/{R}) = {math.sqrt(2*G*M/R)}"
    if G is None:
        return f"G = ve^2 R/(2M) = {ve}^2*{R}/(2*{M}) = {(ve*ve*R)/(2*M)}"
    if M is None:
        return f"M = ve^2 R/(2G) = {ve}^2*{R}/(2*{G}) = {(ve*ve*R)/(2*G)}"
    if R is None:
        return f"R = 2GM/ve^2 = 2*{G}*{M}/{ve}^2 = {(2*G*M)/(ve*ve)}"


def orbital_velocity(vars):
    v, G, M, R = vars["v"], vars["G"], vars["M"], vars["R"]

    if v is None:
        return f"v = sqrt(GM/R) = sqrt({G}*{M}/{R}) = {math.sqrt(G*M/R)}"
    if R is None:
        return f"R = GM/v^2 = {G}*{M}/{v}^2 = {G*M/(v*v)}"


def gravity_height(vars):
    gh, g, R, h = vars["gh"], vars["g"], vars["R"], vars["h"]

    if gh is None:
        return f"gh = g (R/(R+h))^2 = {g}*({R}/({R}+{h}))^2 = {g*(R/(R+h))**2}"
