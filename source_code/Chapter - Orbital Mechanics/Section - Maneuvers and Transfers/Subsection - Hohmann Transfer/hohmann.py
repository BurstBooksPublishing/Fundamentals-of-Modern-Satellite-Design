import math

# Earth's gravitational parameter (m^3/s^2)
mu = 3.986004418e14

def hohmann(r1, r2):
    a_t = 0.5*(r1 + r2)                       # transfer semi-major axis
    v1 = math.sqrt(mu / r1)                  # initial circular speed
    v2 = math.sqrt(mu / r2)                  # target circular speed
    v_p = math.sqrt(mu*(2.0/r1 - 1.0/a_t))   # speed at periapsis (transfer)
    v_a = math.sqrt(mu*(2.0/r2 - 1.0/a_t))   # speed at apoapsis (transfer)
    dv1 = v_p - v1                            # first burn (m/s)
    dv2 = v2 - v_a                            # second burn (m/s)
    dv_total = abs(dv1) + abs(dv2)
    tof = math.pi * math.sqrt(a_t**3 / mu)    # time of flight (s)
    return {'dv1': dv1, 'dv2': dv2, 'dv_total': dv_total, 'tof_s': tof}

# Example: 400 km LEO to GEO
Re = 6378000.0
r1 = Re + 400000.0
r2 = Re + 35786000.0
print(hohmann(r1, r2))   # prints burns in m/s and TOF in seconds