# Compute required solar area and mass for given continuous power need.
import math

# Mission parameters (example: GEO commsat continuous 20 kW)
P_req = 20000.0          # W
G = 1361.0               # W/m^2 at 1 AU
eta = 0.30               # end-of-life cell efficiency (30%)
f_ecl = 0.0              # eclipse fraction for GEO
alpha = 0.0              # radians, perfect pointing
S_sa = 200.0             # array specific power W/kg (typical high-performance)

# Compute area from eq. (1)
A_sa = P_req / (G * eta * math.cos(alpha) * (1.0 - f_ecl))
m_sa = P_req / S_sa      # mass estimate from required power and specific power

print(f"Required solar area: {A_sa:.1f} m^2")   # area that must be deployed
print(f"Estimated array mass: {m_sa:.1f} kg")   # mass from specific power
# Compare with RTG: use conservative 5 W/kg specific power
rtg_mass = P_req / 5.0
print(f"Equivalent RTG mass: {rtg_mass:.1f} kg") # shows infeasibility for large P_req