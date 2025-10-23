import numpy as np

# Constants
sigma = 5.670374419e-8         # Stefan-Boltzmann, W/m^2/K^4
S = 1361.0                     # Solar constant, W/m^2

def equilibrium_temperature(alpha, eps, A_proj, A_rad, Q_int, Q_env=0.0):
    # Solve alpha*S*A_proj + Q_int + Q_env = eps*sigma*A_rad*T^4
    numerator = alpha*S*A_proj + Q_int + Q_env
    T4 = numerator / (eps * sigma * A_rad)
    return T4**0.25

# Example: smallsat electronics deck
alpha = 0.25                   # low-absorption surface
eps = 0.85                     # high emissivity radiator
A_proj = 0.5                   # m^2 projected solar area
A_rad = 0.8                    # m^2 radiating area
Q_int = 20.0                   # W internal dissipation
Q_env = 15.0                   # W from albedo + IR estimate

T_eq = equilibrium_temperature(alpha, eps, A_proj, A_rad, Q_int, Q_env)
print(f"Equilibrium temperature = {T_eq:.1f} K")