# formulas/sound.py
import math

def speed_of_sound(vars):
    v, gamma, R, T, M = vars["v"], vars["gamma"], vars["R"], vars["T"], vars["M"]

    if v is None:
        return f"v = sqrt(gammaRT/M) = sqrt({gamma}*{R}*{T}/{M}) = {math.sqrt(gamma*R*T/M)}"


def open_pipe_frequency(vars):
    fn, n, v, L = vars["fn"], vars["n"], vars["v"], vars["L"]

    if fn is None:
        return f"fn = n v/(2L) = {n}*{v}/(2*{L}) = {(n*v)/(2*L)}"
    if n is None:
        return f"n = 2L fn / v = 2*{L}*{fn}/{v} = {(2*L*fn)/v}"
    if v is None:
        return f"v = 2L fn / n = 2*{L}*{fn}/{n} = {(2*L*fn)/n}"
    if L is None:
        return f"L = n v/(2 fn) = {n}*{v}/(2*{fn}) = {(n*v)/(2*fn)}"


def closed_pipe_frequency(vars):
    fn, n, v, L = vars["fn"], vars["n"], vars["v"], vars["L"]

    if fn is None:
        return f"fn = n v/(4L) = {n}*{v}/(4*{L}) = {(n*v)/(4*L)}"
    if n is None:
        return f"n = 4L fn / v = 4*{L}*{fn}/{v} = {(4*L*fn)/v}"
    if v is None:
        return f"v = 4L fn / n = 4*{L}*{fn}/{n} = {(4*L*fn)/n}"
    if L is None:
        return f"L = n v/(4 fn) = {n}*{v}/(4*{fn}) = {(n*v)/(4*fn)}"


def doppler_effect(vars):
    fp, f, v, vo, vs = vars["fp"], vars["f"], vars["v"], vars["vo"], vars["vs"]

    # f' = f (v ± vo)/(v ∓ vs)
    if fp is None:
        return f"f' = f*(v+vo)/(v-vs) = {f}*({v}+{vo})/({v}-{vs}) = {f*(v+vo)/(v-vs)}"
