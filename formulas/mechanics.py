# formulas/mechanics.py
import math

# Average velocity: vavg = displacement / time
def avg_velocity(vars):
    vavg, dx, dt = vars["vavg"], vars["dx"], vars["dt"]

    if vavg is None:
        return f"vavg = dx/dt = {dx}/{dt} = {dx/dt}"
    if dx is None:
        return f"dx = vavg*dt = {vavg}*{dt} = {vavg*dt}"
    if dt is None:
        return f"dt = dx/vavg = {dx}/{vavg} = {dx/vavg}"


# Average speed: speed = distance/time
def avg_speed(vars):
    speed, dist, dt = vars["speed"], vars["dist"], vars["dt"]

    if speed is None:
        return f"speed = dist/dt = {dist}/{dt} = {dist/dt}"
    if dist is None:
        return f"dist = speed*dt = {speed}*{dt} = {speed*dt}"
    if dt is None:
        return f"dt = dist/speed = {dist}/{speed} = {dist/speed}"


# Average acceleration: aavg = dv/dt
def avg_acceleration(vars):
    aavg, dv, dt = vars["aavg"], vars["dv"], vars["dt"]

    if aavg is None:
        return f"aavg = dv/dt = {dv}/{dt} = {dv/dt}"
    if dv is None:
        return f"dv = aavg*dt = {aavg}*{dt} = {aavg*dt}"
    if dt is None:
        return f"dt = dv/aavg = {dv}/{aavg} = {dv/aavg}"


# v = u + at
def motion_v(vars):
    v, u, a, t = vars["v"], vars["u"], vars["a"], vars["t"]

    if v is None:
        return f"v = u + at = {u} + {a}*{t} = {u+a*t}"
    if u is None:
        return f"u = v - at = {v} - {a}*{t} = {v-a*t}"
    if a is None:
        return f"a = (v-u)/t = ({v}-{u})/{t} = {(v-u)/t}"
    if t is None:
        return f"t = (v-u)/a = ({v}-{u})/{a} = {(v-u)/a}"


# s = ut + 1/2 at^2
def motion_s(vars):
    s, u, a, t = vars["s"], vars["u"], vars["a"], vars["t"]

    if s is None:
        return f"s = ut + 0.5at^2 = {u}*{t} + 0.5*{a}*{t}^2 = {u*t + 0.5*a*t*t}"
    if u is None:
        return f"u = (s - 0.5at^2)/t = ({s}-0.5*{a}*{t}^2)/{t} = {(s-0.5*a*t*t)/t}"
    if a is None:
        return f"a = 2(s-ut)/t^2 = 2*({s}-{u}*{t})/{t}^2 = {2*(s-u*t)/(t*t)}"


# v^2 = u^2 + 2as
def motion_v2(vars):
    v, u, a, s = vars["v"], vars["u"], vars["a"], vars["s"]

    if v is None:
        return f"v = sqrt(u^2+2as) = sqrt({u}^2+2*{a}*{s}) = {math.sqrt(u*u+2*a*s)}"
    if a is None:
        return f"a = (v^2-u^2)/(2s) = ({v}^2-{u}^2)/(2*{s}) = {(v*v-u*u)/(2*s)}"
    if s is None:
        return f"s = (v^2-u^2)/(2a) = ({v}^2-{u}^2)/(2*{a}) = {(v*v-u*u)/(2*a)}"


# Projectile: Time of flight T = 2u sinθ / g
def projectile_time(vars):
    T, u, theta, g = vars["T"], vars["u"], vars["theta"], vars["g"]

    if T is None:
        return f"T = 2u sinθ/g = 2*{u}*sin({theta})/{g} = {2*u*math.sin(theta)/g}"


# Range R = u^2 sin2θ / g
def projectile_range(vars):
    R, u, theta, g = vars["R"], vars["u"], vars["theta"], vars["g"]

    if R is None:
        return f"R = u^2 sin(2θ)/g = {u}^2*sin(2*{theta})/{g} = {(u*u*math.sin(2*theta))/g}"


# Max height H = u^2 sin^2θ / (2g)
def projectile_height(vars):
    H, u, theta, g = vars["H"], vars["u"], vars["theta"], vars["g"]

    if H is None:
        return f"H = u^2 sin^2θ/(2g) = {u}^2*sin({theta})^2/(2*{g}) = {(u*u*(math.sin(theta)**2))/(2*g)}"


# Relative velocity: vAB = vA - vB
def relative_velocity(vars):
    vAB, vA, vB = vars["vAB"], vars["vA"], vars["vB"]

    if vAB is None:
        return f"vAB = vA - vB = {vA}-{vB} = {vA-vB}"
    if vA is None:
        return f"vA = vAB + vB = {vAB}+{vB} = {vAB+vB}"
    if vB is None:
        return f"vB = vA - vAB = {vA}-{vAB} = {vA-vAB}"


# Newton second law: F = m a
def newton_second(vars):
    F, m, a = vars["F"], vars["m"], vars["a"]

    if F is None:
        return f"F = m a = {m}*{a} = {m*a}"
    if m is None:
        return f"m = F/a = {F}/{a} = {F/a}"
    if a is None:
        return f"a = F/m = {F}/{m} = {F/m}"


# Spring force: F = kx
def spring_force(vars):
    F, k, x = vars["F"], vars["k"], vars["x"]

    if F is None:
        return f"F = kx = {k}*{x} = {k*x}"
    if k is None:
        return f"k = F/x = {F}/{x} = {F/x}"
    if x is None:
        return f"x = F/k = {F}/{k} = {F/k}"


# Work: W = F*s
def work(vars):
    W, F, s = vars["W"], vars["F"], vars["s"]

    if W is None:
        return f"W = F*s = {F}*{s} = {F*s}"
    if F is None:
        return f"F = W/s = {W}/{s} = {W/s}"
    if s is None:
        return f"s = W/F = {W}/{F} = {W/F}"


# Kinetic energy: K = 1/2 m v^2
def kinetic(vars):
    K, m, v = vars["K"], vars["m"], vars["v"]

    if K is None:
        return f"K = 0.5 m v^2 = 0.5*{m}*{v}^2 = {0.5*m*v*v}"
    if m is None:
        return f"m = 2K/v^2 = 2*{K}/{v}^2 = {(2*K)/(v*v)}"
    if v is None:
        return f"v = sqrt(2K/m) = sqrt(2*{K}/{m}) = {math.sqrt((2*K)/m)}"


# Potential energy: U = mgh
def potential(vars):
    U, m, g, h = vars["U"], vars["m"], vars["g"], vars["h"]

    if U is None:
        return f"U = mgh = {m}*{g}*{h} = {m*g*h}"
    if m is None:
        return f"m = U/(gh) = {U}/({g}*{h}) = {U/(g*h)}"
    if h is None:
        return f"h = U/(mg) = {U}/({m}*{g}) = {U/(m*g)}"


# Power: P = W/t
def power(vars):
    P, W, t = vars["P"], vars["W"], vars["t"]

    if P is None:
        return f"P = W/t = {W}/{t} = {W/t}"
    if W is None:
        return f"W = P*t = {P}*{t} = {P*t}"
    if t is None:
        return f"t = W/P = {W}/{P} = {W/P}"


# Angular velocity: omega = v/r
def angular_velocity(vars):
    omega, v, r = vars["omega"], vars["v"], vars["r"]

    if omega is None:
        return f"ω = v/r = {v}/{r} = {v/r}"
    if v is None:
        return f"v = ωr = {omega}*{r} = {omega*r}"
    if r is None:
        return f"r = v/ω = {v}/{omega} = {v/omega}"


# Centripetal acceleration: ac = v^2/r
def centripetal(vars):
    ac, v, r = vars["ac"], vars["v"], vars["r"]

    if ac is None:
        return f"ac = v^2/r = {v}^2/{r} = {v*v/r}"
    if v is None:
        return f"v = sqrt(ac*r) = sqrt({ac}*{r}) = {math.sqrt(ac*r)}"
    if r is None:
        return f"r = v^2/ac = {v}^2/{ac} = {v*v/ac}"
