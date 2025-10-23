import math
# physical constants
mu = 3.986004418e14       # m^3/s^2
Re = 6378137.0            # m
J2 = 1.08263e-3
c = 299792458.0
f = 14e9                  # 14 GHz Ku-band
lam = c / f

def period_seconds(alt_m):
    a = Re + alt_m
    return 2*math.pi*math.sqrt(a**3 / mu)

def fspl_db(range_m):
    return 20*math.log10(4*math.pi*range_m/lam)

def nodal_regression_deg_per_day(alt_m, inc_deg, ecc=0.0):
    a = Re + alt_m
    T = period_seconds(alt_m)
    n = 2*math.pi / T
    inc = math.radians(inc_deg)
    dotO = -1.5 * J2 * (Re/a)**2 * n * math.cos(inc) / (1-ecc**2)**2
    return math.degrees(dotO) * 86400.0  # deg/day

alts = {'LEO':800e3, 'MEO':20200e3, 'GEO':35786e3}
for name, h in alts.items():
    T = period_seconds(h)
    R = h + Re
    print(f"{name}: T={T/3600:.2f} hr, FSPL={fspl_db(R):.1f} dB")
    print(f"  Nodal drift (inc=98deg): {nodal_regression_deg_per_day(h,98):.4f} deg/day")