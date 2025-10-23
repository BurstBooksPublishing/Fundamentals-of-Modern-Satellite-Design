import math
# Inputs (example values)
mu = 3.986004418e14              # Earth mu, m^3/s^2
a = 42164e3                      # GEO radius, m (or set for LEO)
v = math.sqrt(mu/a)              # orbital speed, m/s
Cd = 2.2                         # drag coefficient
A = 20.0                         # cross-section, m^2 (satellite)
m = 3000.0                       # mass, kg
rho = 4e-16                      # density, kg/m^3 (GEO ~0, LEO typical 4e-12)
# Drag acceleration and annual delta-v
ad = 0.5 * Cd * (A/m) * rho * v**2
dv_drag_per_year = abs(ad) * 365.25 * 24*3600  # m/s per year
# Inclination correction: specify drift rate (rad/year)
inc_drift_deg_per_year = 0.5     # example GEO luni-solar drift
inc_drift = math.radians(inc_drift_deg_per_year)
dv_inc_per_year = v * inc_drift   # small-angle approx
print(f"Drag dv/yr: {dv_drag_per_year:.3e} m/s")
print(f"Inclination dv/yr: {dv_inc_per_year:.3f} m/s")
# Sum budget; include margin factor
margin = 1.2
annual_budget = (dv_drag_per_year + dv_inc_per_year) * margin
print(f"Annual station-keeping budget: {annual_budget:.3f} m/s")