import math
# compute SEE probability (per eq. \ref{eq:see_prob})
sigma = 1e-6   # cm^2, device cross-section
phi = 1e6      # cm^-2, expected heavy-ion fluence
p_see = 1 - math.exp(-sigma*phi)   # probability of >=1 SEE

# thermal equilibrium (simple model per eq. \ref{eq:temp_simple})
G = 1361.0     # W/m^2, solar constant
alpha = 0.6    # absorptivity of RF radome
epsilon = 0.85 # emissivity of painted radiator
sigma_sb = 5.670374419e-8
T_equil = (alpha*G/(epsilon*sigma_sb))**0.25  # K

print(f"P_SEE={p_see:.3f}  T_equil={T_equil:.1f}K")  # quick assessment