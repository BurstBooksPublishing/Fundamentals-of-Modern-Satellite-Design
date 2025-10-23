import numpy as np
# constants
mu = 3.986004418e14   # Earth's GM, m^3/s^2
R = 6371000.0         # Earth radius, m

def orbital_metrics(alt_km, ecc=0.0):
    a = R + alt_km*1000.0           # semi-major axis for circular approx
    e = ecc
    rp = a*(1-e)
    ra = a*(1+e)
    T = 2*np.pi*np.sqrt(a**3/mu)    # orbital period, s
    n = np.sqrt(mu/a**3)           # mean motion, rad/s
    vp = np.sqrt(mu*(2/rp - 1/a))  # speed at perigee, m/s
    va = np.sqrt(mu*(2/ra - 1/a))  # speed at apogee, m/s
    return dict(a=a, rp=rp, ra=ra, T=T, n=n, vp=vp, va=va)

# example: 700 km LEO
metrics = orbital_metrics(700.0)
# printed values used in mass and power trade studies (commented)
# print(metrics)