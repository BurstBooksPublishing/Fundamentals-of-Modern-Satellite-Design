import math

# Inputs: power (W), allowed temp rise (K), via params (m)
P = 5.0                 # power dissipated by PA, W
d = 0.0006              # via diameter, m (600 um)
L = 0.0016              # via length (board thickness), m
k_cu = 400.0            # copper thermal conductivity, W/(m*K)
deltaT_allow = 20.0     # allowable temperature rise, K

# thermal resistance per via (solid cylindrical approximation)
A = math.pi * (d**2) / 4.0
R_via = L / (k_cu * A)  # K/W per via

# required number of vias (rounded up)
n_vias = math.ceil((P * R_via) / deltaT_allow * 1.0)  # conservative
print(f"R_via = {R_via:.4f} K/W, required vias = {n_vias}")
# Note: account for composite pathways and plane spreading in detailed FEA.