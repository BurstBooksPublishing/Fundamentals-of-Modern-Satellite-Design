import math

# constants (SI)
mu = 3.986004418e14        # Earth's gravitational parameter, m^3/s^2
R_E = 6371e3               # Earth radius, m

def deorbit_delta_v(alt_initial_m, alt_perigee_m):
    r0 = R_E + alt_initial_m
    rp = R_E + alt_perigee_m
    v0 = math.sqrt(mu / r0)                    # circular speed
    a = 0.5 * (r0 + rp)                        # semimajor axis of ellipse
    v1 = math.sqrt(mu * (2.0 / r0 - 1.0 / a))  # speed after retroburn
    return v0 - v1

# example: 700 km initial altitude to 80 km perigee
dv = deorbit_delta_v(700e3, 80e3)
print(f"Required Δv = {dv:.1f} m/s")  # ~100 m/s depending on assumptions