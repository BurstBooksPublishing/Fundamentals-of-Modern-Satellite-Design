import math

# Example fluid: water at 300K (replace with spacecraft fluid, e.g., ammonia)
rho_l = 997.0        # liquid density, kg/m^3
h_fg  = 2.26e6       # latent heat, J/kg
mu_l  = 8.9e-4       # viscosity, Pa*s
sigma = 0.0728       # surface tension, N/m
cos_theta = 1.0      # assume wetting

# Geometry and wick: user-defined
K = 1e-12            # wick permeability, m^2 (typical 1e-12 - 1e-10)
A = 1e-4             # evaporator wick area, m^2 (10x10 mm)
r_eff = 50e-6        # effective pore radius, m
L = 0.5              # liquid return length, m

# Capillary pressure (Pa)
delta_p_c = 2.0*sigma*cos_theta / r_eff

# Capillary-limited heat (W)
Q_max = rho_l * h_fg * (K * A * delta_p_c) / (mu_l * L)

print(f"Delta_p_c = {delta_p_c:.1f} Pa  |  Q_max = {Q_max:.3f} W")
# Use Q_max to validate heater-to-radiator transport requirements.