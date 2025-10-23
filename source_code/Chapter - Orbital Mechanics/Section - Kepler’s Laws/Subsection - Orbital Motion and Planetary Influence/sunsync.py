import numpy as np

# Constants (Earth)
mu = 3.986004418e14        # m^3/s^2
Re = 6378137.0             # m
J2 = 1.08263e-3
deg_per_day = 360.0/365.2422

def sun_sync_inclination(alt_m, ecc=0.0):
    a = Re + alt_m
    n = np.sqrt(mu / a**3)                 # rad/s
    # target nodal regression in rad/s (retrograde ~ -deg_per_day)
    target = -np.deg2rad(360.0/365.2422) / 86400.0
    # coefficient from eqn for dot_Omega = -1.5 * n * J2 * (Re/(a*(1-e^2)))^2 * cos i
    coeff = -1.5 * n * J2 * (Re / (a * (1 - ecc**2)))**2
    cos_i = target / coeff
    # clamp and compute inclination
    if abs(cos_i) <= 1.0:
        i = np.arccos(cos_i)
        return np.rad2deg(i)               # degrees
    else:
        return None                         # no real solution

# Example: 700 km sun-synchronous target
alt = 700000.0
inc = sun_sync_inclination(alt)
print(f"Altitude {alt/1000:.0f} km -> sun-sync inclination {inc:.4f} deg")