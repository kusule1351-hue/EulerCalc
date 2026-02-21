# formulas/ac.py
import math

def vrms(vars):
    Vrms, V0 = vars["Vrms"], vars["V0"]
    if Vrms is None:
        return f"Vrms = V0/sqrt(2) = {V0}/sqrt(2) = {V0/math.sqrt(2)}"
    if V0 is None:
        return f"V0 = Vrms*sqrt(2) = {Vrms}*sqrt(2) = {Vrms*math.sqrt(2)}"

def irms(vars):
    Irms, I0 = vars["Irms"], vars["I0"]
    if Irms is None:
        return f"Irms = I0/sqrt(2) = {I0}/sqrt(2) = {I0/math.sqrt(2)}"
    if I0 is None:
        return f"I0 = Irms*sqrt(2) = {Irms}*sqrt(2) = {Irms*math.sqrt(2)}"
