import math
# Constants (km, s)
mu = 398600.4418
Re = 6378.137
T_sid = 86164.0

def classify_orbit(h, e=0.0):
    a = Re + h                             # semimajor axis (km)
    T = 2*math.pi*math.sqrt(a**3/mu)       # period (s)
    n = math.sqrt(mu/a**3)                 # mean motion (rad/s)
    # Simple classification rules
    if h < 2000:
        kind = "LEO"
    elif h < 35786:
        kind = "MEO"
    elif abs(h-35786) < 100:               # tolerance for GEO altitude
        kind = "GEO"
    else:
        kind = "High-altitude"
    # flag typical mission uses
    uses = []
    if kind=="LEO" and 500<=h<=800:
        uses.append("Sun-synchronous candidate")
    if kind=="MEO" and 19000<=h<=21000:
        uses.append("Navigation (GPS-like)")
    return {"alt_km":h,"a_km":a,"period_s":T,"mean_motion_rad_s":n,
            "type":kind,"notes":uses}

# Examples
print(classify_orbit(550))    # common EO/SSO altitude
print(classify_orbit(20200))  # GPS-class MEO
print(classify_orbit(35786))  # GEO