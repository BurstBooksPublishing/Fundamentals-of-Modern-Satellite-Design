import math
# Constants
sigma = 5.670374419e-8  # Stefan-Boltzmann (W/m^2/K^4)
# Inputs (example for Ka-band SSPA)
P_out_W = 100.0         # desired RF output (W)
eff = 0.60              # RF-to-DC efficiency (linear)
epsilon = 0.85          # radiator emissivity
T_rad_K = 300.0         # radiator temperature (K)
T_bg_K = 4.0            # deep-space background (K)

# Compute DC power and waste heat
P_dc = P_out_W / eff    # supplied DC power (W)
Q = P_dc - P_out_W      # waste heat to radiate (W)

# Radiator area (m^2) using eq. (rad_area)
A_m2 = Q / (epsilon * sigma * (T_rad_K**4 - T_bg_K**4))

# Print results (convert to cm^2)
print(f"P_dc = {P_dc:.1f} W  # includes conversion losses")
print(f"Heat to radiate Q = {Q:.1f} W")
print(f"Radiator area = {A_m2*1e4:.1f} cm^2  # at {T_rad_K} K")