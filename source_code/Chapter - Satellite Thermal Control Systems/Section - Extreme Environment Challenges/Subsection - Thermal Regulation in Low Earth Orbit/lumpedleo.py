import numpy as np

# physical constants
sigma = 5.670374419e-8  # Stefan-Boltzmann
S0 = 1361.0             # solar constant (W/m^2)
E_ir = 237.0            # approximate Earth IR (W/m^2)

# satellite / module parameters
m = 100.0               # kg
c = 900.0               # J/(kg K)
A = 1.0                 # radiating area (m^2)
eps = 0.85
alpha = 0.2
Q_int = 50.0            # internal dissipation (W)

# orbit/timestep
T_orbit = 5400.0        # 90 min in seconds
dt = 10.0
steps = int(T_orbit/dt)
eclipse_frac = 0.35     # approximate eclipse fraction
eclipse_steps = int(steps*eclipse_frac)

# initial condition
T = 290.0               # K
temps = []

for i in range(steps):
    # determine sunlit or eclipse
    sunlit = (i >= eclipse_steps)  # simple shift; real model needs geometry
    Qsolar = alpha * S0 * A if sunlit else 0.0
    Q_alb = 0.2 * S0 * A if sunlit else 0.0  # simplified albedo term
    Qin = Qsolar + Q_alb + alpha*E_ir*A + Q_int
    # Euler integration of lumped ODE
    dT = (Qin - eps * sigma * A * T**4) * dt / (m * c)
    T += dT
    temps.append(T)

# temps contains the orbital temperature history (K)