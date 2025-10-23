import numpy as np

# Inputs (example for CFRP quasi-isotropic panel)
E = 70e9        # Pa, effective laminate modulus
rho = 1600      # kg/m^3, laminate density
sigma_allow = 600e6  # Pa, allowable tensile strength
L = 2.0         # m, column length
b = 0.02        # m, panel width (thickness direction)
t = 0.005       # m, panel (web) thickness
K = 1.0         # effective length factor (pinned-pinned)

# geometric properties for rectangular cross-section
I = (b * t**3) / 12.0   # m^4, bending about weak axis
P_cr = (np.pi**2 * E * I) / (K * L)**2  # Euler buckling (N)
mass = rho * b * t * L  # kg, mass of the member

# outputs
print("Specific strength S* (MPa/(kg/m3)):", (sigma_allow/rho)/1e6)
print("Critical buckling load P_cr (N):", P_cr)
print("Member mass (kg):", mass)
# Use P_required and safety factor to size thickness in iterative loop (omitted).