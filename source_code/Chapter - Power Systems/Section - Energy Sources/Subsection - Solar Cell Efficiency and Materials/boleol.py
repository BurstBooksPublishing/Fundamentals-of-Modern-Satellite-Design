import math
# Inputs (engineering defaults)
G0 = 1361.0                        # W/m^2, solar constant
A = 10.0                           # m^2, total array area
eta0 = 0.30                        # cell+array efficiency at Tref
theta_deg = 0.0                    # incidence angle
T = 300.0                          # K, operating temperature
Tref = 298.0                        # K, reference temperature
beta = -8e-4                       # K^-1, temp coefficient (multi-junction)
alpha = 0.015                      # yr^-1, degradation constant
life = 15.0                        # yr, mission life
duty = 0.85                        # pointing & eclipse duty factor

# Compute irradiance, temp effect, BOL/EOL power
G = G0 * math.cos(math.radians(theta_deg))
eta_T = eta0 * (1 + beta * (T - Tref))    # eq: temp_coeff
Pbol = G * A * eta_T * duty               # eq: power_area
eta_eol = eta0 * math.exp(-alpha * life)  # eq: degrade
P_eol = G * A * eta_eol * duty

print(f"BOL power: {Pbol:.1f} W  EOL power: {P_eol:.1f} W")