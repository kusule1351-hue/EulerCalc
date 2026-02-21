# calculations.py
from utils import solve_formula_menu

from formulas import mechanics, thermo, gravitation, fluids, sound
from formulas import communication, semiconductor, error_measurement
from formulas import magnetism, optics, modern, oscillation
from formulas import electric
from formulas import electromagnetic
from formulas import math_tools
from formulas import plot_tools
from formulas import numerical_pde

def get_mechanics_formulas():
    return [

        ("Average velocity vavg=dx/dt", mechanics.avg_velocity, ["vavg", "dx", "dt"]),
        ("Average speed speed=dist/dt", mechanics.avg_speed, ["speed", "dist", "dt"]),
        ("Average acceleration aavg=dv/dt", mechanics.avg_acceleration, ["aavg", "dv", "dt"]),
        ("Motion v=u+at", mechanics.motion_v, ["v", "u", "a", "t"]),
        ("Motion s=ut+1/2at^2", mechanics.motion_s, ["s", "u", "a", "t"]),
        ("Motion v^2=u^2+2as", mechanics.motion_v2, ["v", "u", "a", "s"]),
        ("Projectile time of flight", mechanics.projectile_time, ["T", "u", "theta", "g"]),
        ("Projectile range", mechanics.projectile_range, ["R", "u", "theta", "g"]),
        ("Projectile max height", mechanics.projectile_height, ["H", "u", "theta", "g"]),
        ("Relative velocity vAB=vA-vB", mechanics.relative_velocity, ["vAB", "vA", "vB"]),
        ("Newton second law F=ma", mechanics.newton_second, ["F", "m", "a"]),
        ("Spring force F=kx", mechanics.spring_force, ["F", "k", "x"]),
        ("Work W=F*s", mechanics.work, ["W", "F", "s"]),
        ("Kinetic energy K=1/2mv^2", mechanics.kinetic, ["K", "m", "v"]),
        ("Potential energy U=mgh", mechanics.potential, ["U", "m", "g", "h"]),
        ("Power P=W/t", mechanics.power, ["P", "W", "t"]),
        ("Angular velocity ω=v/r", mechanics.angular_velocity, ["omega", "v", "r"]),
        ("Centripetal acceleration ac=v^2/r", mechanics.centripetal, ["ac", "v", "r"]),
    ]

def mechanics_menu():
    solve_formula_menu('Mechanics', get_mechanics_formulas())


def get_thermo_formulas():
    return [

        ("First law ΔU=Q-W", thermo.first_law, ["dU", "Q", "W"]),
        ("Isothermal work W=nRT ln(Vf/Vi)", thermo.isothermal_work, ["W", "n", "R", "T", "Vf", "Vi"]),
        ("Wave speed on string v=sqrt(T/mu)", thermo.string_wave_speed, ["v", "T", "mu"]),
        ("Power transmitted P=2π^2 f^2 A^2 μ v", thermo.power_transmitted, ["P", "f", "A", "mu", "v"]),
        ("Standing wave fn=nv/(2L)", thermo.standing_wave, ["fn", "n", "v", "L"]),
        ("Ideal gas PV=nRT", thermo.ideal_gas, ["P", "V", "n", "R", "T"]),
        ("First law ΔU=Q-W", thermo.first_law, ["dU", "Q", "W"]),
        ("Isothermal work W=nRT ln(Vf/Vi)", thermo.isothermal_work, ["W", "n", "R", "T", "Vf", "Vi"]),
        ("Adiabatic PV^γ=const", thermo.adiabatic_relation, ["P1", "V1", "P2", "V2", "gamma"]),
        ("Adiabatic TV^(γ-1)=const", thermo.adiabatic_temp_relation, ["T1", "V1", "T2", "V2", "gamma"]),

        ("Heat Q=mcΔT", thermo.heat_capacity, ["Q", "m", "c", "dT"]),
        ("Latent heat Q=mL", thermo.latent_heat, ["Q", "m", "L"]),

        ("Entropy ΔS=Qrev/T", thermo.entropy, ["dS", "Qrev", "T"]),
        ("Isothermal entropy ΔS=nR ln(Vf/Vi)", thermo.isothermal_entropy, ["dS", "n", "R", "Vf", "Vi"]),

        ("Efficiency η=W/Qh", thermo.efficiency, ["eta", "W", "Qh"]),
        ("Carnot efficiency η=1-Tc/Th", thermo.carnot_efficiency, ["eta", "Tc", "Th"]),

        ("Vrms = sqrt(3RT/M)", thermo.rms_speed, ["vrms", "R", "T", "M"]),
    ]

def thermo_menu():
    solve_formula_menu('Thermodynamics + Waves', get_thermo_formulas())


def get_gravitation_formulas():
    return [

        ("Newton gravitation F=Gm1m2/r^2", gravitation.newton_gravitation, ["F", "G", "m1", "m2", "r"]),
        ("Potential energy U=-Gm1m2/r", gravitation.gravitational_potential_energy, ["U", "G", "m1", "m2", "r"]),
        ("Escape velocity ve=sqrt(2GM/R)", gravitation.escape_velocity, ["ve", "G", "M", "R"]),
        ("Orbital velocity v=sqrt(GM/R)", gravitation.orbital_velocity, ["v", "G", "M", "R"]),
        ("Gravity at height gh=g(R/(R+h))^2", gravitation.gravity_height, ["gh", "g", "R", "h"]),
    ]

def gravitation_menu():
    solve_formula_menu('Gravitation', get_gravitation_formulas())


def get_fluids_formulas():
    return [

        ("Pressure P=F/A", fluids.pressure, ["P", "F", "A"]),
        ("Continuity A1v1=A2v2", fluids.continuity, ["A1", "v1", "A2", "v2"]),
        ("Surface tension F=T*L", fluids.surface_tension_force, ["F", "T", "L"]),
        ("Drop excess pressure ΔP=2T/R", fluids.excess_pressure_drop, ["dP", "T", "R"]),
        ("Bubble excess pressure ΔP=4T/R", fluids.excess_pressure_bubble, ["dP", "T", "R"]),
    ]

def fluids_menu():
    solve_formula_menu('Fluids', get_fluids_formulas())


def get_sound_formulas():
    return [

        ("Speed of sound v=sqrt(gammaRT/M)", sound.speed_of_sound, ["v", "gamma", "R", "T", "M"]),
        ("Open pipe fn=nv/(2L)", sound.open_pipe_frequency, ["fn", "n", "v", "L"]),
        ("Closed pipe fn=nv/(4L)", sound.closed_pipe_frequency, ["fn", "n", "v", "L"]),
        ("Doppler f' = f(v+vo)/(v-vs)", sound.doppler_effect, ["fp", "f", "v", "vo", "vs"]),
    ]

def sound_menu():
    solve_formula_menu('Sound Waves', get_sound_formulas())


def get_communication_formulas():
    return [

        ("AM modulation index m=Am/Ac", communication.am_modulation_index, ["m", "Am", "Ac"]),
        ("AM total power Pt=Pc(1+m^2/2)", communication.am_total_power, ["Pt", "Pc", "m"]),
        ("AM bandwidth BW=2fm", communication.am_bandwidth, ["BW", "fm"]),
        ("FM deviation df=kf*Am", communication.fm_deviation, ["df", "kf", "Am"]),
        ("FM bandwidth BW≈2(df+fm)", communication.fm_bandwidth, ["BW", "df", "fm"]),
    ]

def communication_menu():
    solve_formula_menu('Communication', get_communication_formulas())


def get_semiconductor_formulas():
    return [

        ("Conductivity σ=nqμ", semiconductor.conductivity, ["sigma", "n", "q", "mu"]),
        ("Resistivity ρ=1/σ", semiconductor.resistivity, ["rho", "sigma"]),
        ("Shockley diode equation", semiconductor.shockley_diode, ["I", "I0", "q", "V", "k", "T"]),
        ("Transistor relation IE=IB+IC", semiconductor.transistor_relation, ["IE", "IB", "IC"]),
        ("Current gain β=IC/IB", semiconductor.current_gain, ["beta", "IC", "IB"]),
    ]

def semiconductor_menu():
    solve_formula_menu('Semiconductor', get_semiconductor_formulas())


def get_error_formulas():
    return [

        ("Absolute error Δx=|xm-xt|", error_measurement.absolute_error, ["dx", "xm", "xt"]),
        ("Relative error Δx/xt", error_measurement.relative_error, ["rel", "dx", "xt"]),
        ("Percentage error", error_measurement.percentage_error, ["per", "dx", "xt"]),
        ("Propagation sum Δz=Δx+Δy", error_measurement.propagation_sum, ["dz", "dx", "dy"]),
        ("Propagation product Δz/z=Δx/x+Δy/y", error_measurement.propagation_product,
        ["frac", "dz", "z", "dx", "x", "dy", "y"]),
    ]

def error_menu():
    solve_formula_menu('Error & Measurement', get_error_formulas())


def get_magnetism_formulas():
    return [

        ("Magnetic force F=qvBsinθ", magnetism.magnetic_force, ["F", "q", "v", "B", "theta"]),
        ("Lorentz force (simplified)", magnetism.lorentz_force, ["F", "q", "E", "v", "B"]),
        ("Faraday law ε=-ΔΦ/Δt", magnetism.faraday, ["emf", "dphi", "dt"]),
        ("Long wire field B=μ0I/(2πr)", magnetism.long_wire_field, ["B", "mu0", "I", "r"]),
        ("Inductor energy U=1/2LI^2", magnetism.inductor_energy, ["U", "L", "I"]),
    ]

def magnetism_menu():
    solve_formula_menu('Magnetism & Induction', get_magnetism_formulas())


def get_optics_formulas():
    return [

        ("Lens formula 1/f = 1/v - 1/u", optics.lens_formula, ["f", "v", "u"]),
        ("Magnification M=v/u", optics.magnification, ["M", "v", "u"]),
        ("Path difference Δx=d sinθ", optics.path_difference, ["dx", "d", "theta"]),
        ("Constructive Δx=nλ", optics.constructive, ["dx", "n", "lam"]),
        ("Destructive Δx=(n+0.5)λ", optics.destructive, ["dx", "n", "lam"]),
        ("Diffraction grating d sinθ=nλ", optics.diffraction_grating, ["d", "theta", "n", "lam"]),
    ]

def optics_menu():
    solve_formula_menu('Optics', get_optics_formulas())


def get_modern_formulas():
    return [

        ("Photon energy E=hf", modern.photon_energy, ["E", "h", "f"]),
        ("Photon energy E=hc/λ", modern.photon_energy_wavelength, ["E", "h", "c", "lam"]),
        ("De Broglie λ=h/p", modern.de_broglie, ["lam", "h", "p"]),
    ]

def modern_menu():
    solve_formula_menu('Modern Physics', get_modern_formulas())


def get_oscillation_formulas():
    return [

        ("Spring period T=2π sqrt(m/k)", oscillation.spring_period, ["T", "m", "k"]),
        ("Reduced mass μ=m1m2/(m1+m2)", oscillation.reduced_mass, ["mu", "m1", "m2"]),
        ("Pendulum T=2π sqrt(l/g)", oscillation.pendulum_period, ["T", "l", "g"]),
        ("Compound pendulum", oscillation.compound_pendulum, ["T", "I", "m", "g", "l"]),
        ("Torsional pendulum", oscillation.torsional_pendulum, ["T", "I", "C"]),
        ("SHM Superposition amplitude", oscillation.shm_superposition, ["A", "A1", "A2", "phi"]),
    ]

def oscillation_menu():
    solve_formula_menu('Oscillations', get_oscillation_formulas())


def get_electric_formulas():
    return [

        ("Coulomb Law F=kq1q2/r^2", electric.coulomb_law, ["F", "q1", "q2", "r", "e0"]),
        ("Electric Field E=F/q", electric.electric_field, ["E", "F", "q"]),
        ("Field of point charge E=kq/r^2", electric.field_point_charge, ["E", "q", "r", "e0"]),
        ("Electric Potential V=kq/r", electric.electric_potential, ["V", "q", "r", "e0"]),
        ("Potential Energy U=kq1q2/r", electric.electric_potential_energy, ["U", "q1", "q2", "r", "e0"]),
        ("Uniform field E=V/d", electric.uniform_field, ["E", "V", "d"]),
        ("Force in field F=qE", electric.force_in_field, ["F", "q", "E"]),

        ("Dipole moment p=qd", electric.dipole_moment, ["p", "q", "d"]),
        ("Dipole torque τ=pE sinθ", electric.dipole_torque, ["tau", "p", "E", "theta"]),
        ("Dipole energy U=-pE cosθ", electric.dipole_energy, ["U", "p", "E", "theta"]),

        ("Ohm law V=IR", electric.ohms_law, ["V", "I", "R"]),
        ("Power P=VI", electric.power_vi, ["P", "V", "I"]),
        ("Power P=I^2R", electric.power_i2r, ["P", "I", "R"]),
        ("Power P=V^2/R", electric.power_v2r, ["P", "V", "R"]),
        ("Resistance R=ρL/A", electric.resistance_resistivity, ["R", "rho", "L", "A"]),
        ("Current density J=I/A", electric.current_density, ["J", "I", "A"]),
        ("Drift velocity I=nqAvd", electric.drift_velocity, ["I", "n", "q", "A", "vd"]),
        ("Terminal voltage V=E-Ir", electric.internal_resistance, ["V", "E", "I", "r"]),

        ("Series resistance", electric.series_resistance, ["Req", "resistances"]),
        ("Parallel resistance", electric.parallel_resistance, ["Req", "resistances"]),

        ("Capacitance C=Q/V", electric.capacitance_definition, ["C", "Q", "V"]),
        ("Capacitor energy U=1/2CV^2", electric.capacitor_energy, ["U", "C", "V"]),
        ("Capacitor energy U=Q^2/(2C)", electric.capacitor_energy_q, ["U", "Q", "C"]),
        ("Series capacitance", electric.series_capacitance, ["Ceq", "caps"]),
        ("Parallel capacitance", electric.parallel_capacitance, ["Ceq", "caps"]),

        ("RC time constant τ=RC", electric.rc_time_constant, ["tau", "R", "C"]),
        ("Capacitor charging Q=Q0(1-e^(-t/RC))", electric.capacitor_charging, ["Q", "Q0", "t", "R", "C"]),
        ("Capacitor discharging Q=Q0 e^(-t/RC)", electric.capacitor_discharging, ["Q", "Q0", "t", "R", "C"]),

        ("AC voltage V=V0 sin(wt)", electric.ac_voltage, ["V", "V0", "w", "t"]),
        ("RMS voltage Vrms=V0/sqrt(2)", electric.rms_voltage, ["Vrms", "V0"]),
        ("RMS current Irms=I0/sqrt(2)", electric.rms_current, ["Irms", "I0"]),
    ]

def electric_menu():
    solve_formula_menu('Electricity (Extended)', get_electric_formulas())


def get_electromagnetic_formulas():
    return [

        ("Long wire field B=μ0I/(2πr)", electromagnetic.long_wire_field, ["B", "mu0", "I", "r"]),
        ("Loop center field B=μ0I/(2R)", electromagnetic.loop_field_center, ["B", "mu0", "I", "R"]),
        ("Solenoid field B=μ0nI", electromagnetic.solenoid_field, ["B", "mu0", "n", "I"]),
        ("Toroid field B=μ0NI/(2πr)", electromagnetic.toroid_field, ["B", "mu0", "N", "I", "r"]),
        ("Force on charge F=qvB sinθ", electromagnetic.magnetic_force_charge, ["F", "q", "v", "B", "theta"]),
        ("Force on wire F=BIL sinθ", electromagnetic.force_on_wire, ["F", "B", "I", "L", "theta"]),
        ("Force between wires", electromagnetic.force_between_wires, ["F", "mu0", "I1", "I2", "d", "L"]),

        ("Magnetic flux Φ=BA cosθ", electromagnetic.magnetic_flux, ["phi", "B", "A", "theta"]),
        ("Faraday law ε=-NΔΦ/Δt", electromagnetic.faraday_law, ["emf", "N", "dphi", "dt"]),
        ("Motional emf ε=BLv", electromagnetic.motional_emf, ["emf", "B", "L", "v"]),

        ("Self induced emf ε=-LΔI/Δt", electromagnetic.self_induced_emf, ["emf", "L", "dI", "dt"]),
        ("Inductor energy U=1/2LI^2", electromagnetic.inductor_energy, ["U", "L", "I"]),
        ("Mutual inductance ε2=-MΔI/Δt", electromagnetic.mutual_inductance, ["emf2", "M", "dI1", "dt"]),

        ("Inductive reactance XL=ωL", electromagnetic.inductive_reactance, ["XL", "w", "L"]),
        ("Capacitive reactance XC=1/(ωC)", electromagnetic.capacitive_reactance, ["XC", "w", "C"]),
        ("Impedance Z=sqrt(R^2+(XL-XC)^2)", electromagnetic.impedance_rlc, ["Z", "R", "XL", "XC"]),
        ("Resonant frequency f0=1/(2π sqrt(LC))", electromagnetic.resonance_frequency, ["f0", "L", "C"]),

        ("EM wave speed c=1/sqrt(μ0ε0)", electromagnetic.em_wave_speed, ["c", "mu0", "e0"]),
        ("E/B=c relation", electromagnetic.e_b_relation, ["E", "B", "c"]),
        ("Energy density u", electromagnetic.energy_density, ["u", "e0", "E", "B", "mu0"]),
        ("Gauss law ΦE=Q/ε0", electromagnetic.gauss_law_electric, ["phiE", "Q", "e0"]),
        ("Gauss magnetism ΦB=0", electromagnetic.gauss_law_magnetism, []),
        ("Faraday integral form", electromagnetic.faraday_integral, ["emf", "dphiB", "dt"]),
        ("Ampere-Maxwell law", electromagnetic.ampere_maxwell, ["left", "mu0", "I", "e0", "dphiE", "dt"]),

        ("Transformer voltage Vp/Vs=Np/Ns", electromagnetic.transformer_voltage, ["Vp", "Vs", "Np", "Ns"]),
        ("Transformer current Ip/Is=Ns/Np", electromagnetic.transformer_current, ["Ip", "Is", "Np", "Ns"]),

        ("Poynting vector S=(1/μ0)EB", electromagnetic.poynting_vector, ["S", "mu0", "E", "B"]),

        ("Solenoid inductance L=μ0N^2A/l", electromagnetic.solenoid_inductance, ["L", "mu0", "N", "A", "l"]),

        ("RL time constant τ=L/R", electromagnetic.rl_time_constant, ["tau", "L", "R"]),
        ("LC frequency f=1/(2π sqrt(LC))", electromagnetic.lc_frequency, ["f", "L", "C"]),
        ("RLC impedance", electromagnetic.rlc_impedance, ["Z", "R", "w", "L", "C"]),
        ("Phase angle φ=atan((XL-XC)/R)", electromagnetic.phase_angle, ["phi", "R", "XL", "XC"]),
        ("Quality factor Q=ω0L/R", electromagnetic.quality_factor, ["Q", "w0", "L", "R"]),
    ]

def electromagnetic_menu():
    solve_formula_menu('Electromagnetic', get_electromagnetic_formulas())


def get_math_formulas():
    return [

        ("Differentiate d/dx", math_tools.differentiate, ["expr", "var"]),
        ("Indefinite Integral ∫f(x)dx", math_tools.indefinite_integral, ["expr", "var"]),
        ("Definite Integral ∫[a,b] f(x)dx", math_tools.definite_integral, ["expr", "var", "a", "b"]),
        ("Solve equation", math_tools.solve_equation, ["eq", "var"]),

        ("Matrix determinant det(M)", math_tools.matrix_determinant, ["matrix"]),
        ("Matrix inverse M^-1", math_tools.matrix_inverse, ["matrix"]),
        ("Matrix multiply A*B", math_tools.matrix_multiply, ["A", "B"]),
        ("Matrix eigenvalues", math_tools.matrix_eigenvalues, ["matrix"]),
        ("Limit lim(x→a) f(x)", math_tools.limit_calc, ["expr", "var", "point", "dir"]),
        ("L'Hôpital Auto Limit", math_tools.lhopital_limit, ["expr", "var", "point", "dir"]),
        ("Double Integral ∫∫", math_tools.double_integral,
        ["expr", "var1", "var2", "a", "b", "c", "d"]),

        ("Triple Integral ∫∫∫", math_tools.triple_integral,
        ["expr", "var1", "var2", "var3", "a", "b", "c", "d", "e", "f"]),
        ("Maclaurin Series", math_tools.maclaurin_series, ["expr", "var", "n"]),
        ("Taylor Series", math_tools.taylor_series, ["expr", "var", "point", "n"]),
        ("ODE Solver (dsolve)", math_tools.solve_ode, ["eq", "var"]),
        ("Laplace Transform", math_tools.laplace_transform, ["expr", "t", "s"]),
        ("Inverse Laplace Transform", math_tools.inverse_laplace_transform, ["expr", "s", "t"]),
        ("Fourier Series", math_tools.fourier_series_calc, ["expr", "var", "L", "n"]),
        ("Heat PDE (Auto BC)", math_tools.solve_pde,
        ["eq", "var1", "var2", "f", "bc", "L", "k", "f0", "n"]),

        ("Wave PDE (Dirichlet)", math_tools.wave_equation_fourier_dirichlet,
        ["var1", "var2", "f", "L", "c", "f0", "g0", "n"]),
        ("Wave PDE (Neumann)", math_tools.wave_equation_fourier_neumann,
        ["var1","var2","f","L","c","f0","g0","n"]),

        ("Wave PDE (Mixed)", math_tools.wave_equation_fourier_mixed,
        ["var1","var2","f","L","c","f0","g0","n"]),
        ("Wave Animate (Dirichlet)", plot_tools.wave_animate_dirichlet,
        ["var1","var2","L","c","f0","g0","n"]),

        ("Wave Animate (Neumann)", plot_tools.wave_animate_neumann,
        ["var1","var2","L","c","f0","g0","n"]),

        ("Wave Animate (Mixed)", plot_tools.wave_animate_mixed,
        ["var1","var2","L","c","f0","g0","n"]),
        ("Schrödinger Animation (1D)", plot_tools.schrodinger_animate,
        ["V","X","N","dt","spf","frames","m","hbar","x0","sigma","k0","showV", "a"]),
        ("Heat (Numeric CN, Dirichlet) Animate", numerical_pde.heat_cn_dirichlet_animate,
        ["L","k","Nx","dt","spf","frames","f0"]),

        ("Wave (Numeric Leapfrog, Dirichlet) Animate", numerical_pde.wave_leapfrog_dirichlet_animate,
        ["L","c","Nx","dt","spf","frames","f0","g0"]),
        ("Heat (Numeric CN, Neumann) Animate", numerical_pde.heat_cn_neumann_animate,
        ["L","k","Nx","dt","spf","frames","f0"]),

        ("Heat (Numeric CN, Mixed) Animate", numerical_pde.heat_cn_mixed_animate,
        ["L","k","Nx","dt","spf","frames","f0"]),
        ("Wave (Numeric Leapfrog, Neumann) Animate", numerical_pde.wave_leapfrog_neumann_animate,
        ["L","c","beta","Nx","dt","spf","frames","f0","g0"]),

        ("Wave (Numeric Leapfrog, Mixed) Animate", numerical_pde.wave_leapfrog_mixed_animate,
        ["L","c","beta","Nx","dt","spf","frames","f0","g0"]),
    ]

def math_menu():
    solve_formula_menu('Math Tools (CAS)', get_math_formulas())




# GUI registry (category name -> formulas getter)
CATEGORIES = {
    "Mechanics": get_mechanics_formulas,
    "Thermodynamics + Waves": get_thermo_formulas,
    "Gravitation": get_gravitation_formulas,
    "Fluids": get_fluids_formulas,
    "Sound": get_sound_formulas,
    "Electromagnetic": get_electromagnetic_formulas,
    "Communication": get_communication_formulas,
    "Semiconductor": get_semiconductor_formulas,
    "Error & Measurement": get_error_formulas,
    "Magnetism": get_magnetism_formulas,
    "Optics": get_optics_formulas,
    "Modern Physics": get_modern_formulas,
    "Oscillation": get_oscillation_formulas,
    "Electric": get_electric_formulas,
    "Math Tools": get_math_formulas,
}
