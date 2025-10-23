import math, numpy as np
# constants
Re = 6371e3             # m
mu = 3.986004418e14     # m^3/s^2
c = 299792458.0         # m/s

def contact_and_link(h, elev_mask_deg, freq_hz):
    a = Re + h
    n = math.sqrt(mu / a**3)                # rad/s
    E_min = math.radians(elev_mask_deg)
    psi = math.acos((Re / a) * math.cos(E_min))  # rad
    T_contact = 2*psi / n                   # seconds

    # worst-case slant at horizon approximation
    r_max = math.sqrt(a**2 - Re**2)         # m, simple bound
    fspl_db = 20*math.log10(4*math.pi*r_max*freq_hz / c)
    return T_contact, r_max, fspl_db

# Example: 500 km LEO, 10 deg mask, X-band 8 GHz
T, r_max, fspl = contact_and_link(500e3, 10.0, 8e9)
print(f"Contact {T:.0f}s, range {r_max/1e3:.0f} km, FSPL {fspl:.1f} dB")
# Doppler compute per satellite velocity profile in scheduler (not shown).