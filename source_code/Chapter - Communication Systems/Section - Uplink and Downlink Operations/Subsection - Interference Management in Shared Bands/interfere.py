import math
# Constants and mission parameters (example: C-band GEO downlink)
f = 4.0e9                    # Hz, downlink freq
c = 299792458.0              # m/s
lam = c / f
Pt_target = 40.0             # dBm, potential terrestrial Tx power
Gt = 30.0                    # dBi, terrestrial Tx antenna gain
Gr_sat = 40.0                # dBi, satellite Rx gain
R_geo = 35786e3              # m, GEO slant approx
k = 1.38e-23                 # Boltzmann
T_sys = 500.0                # K, system noise temperature (example)
B = 36e6                     # Hz, channel bandwidth
N_dBm = 10*math.log10(k*T_sys*B) + 30  # dBm thermal noise
# Required protection ratio (linear)
Rp_dB = 10.0                 # dB protection margin
Rp = 10**(Rp_dB/10.0)
# Received signal from desired satellite (simplified Friis)
Pr_sat_dBm = 10*math.log10( (10**(0/10))* (10**(Gr_sat/10)) * (1) ) # placeholder
# Compute allowable interference from eq (Imax), simplified numeric approach
# Here we'd compute required exclusion distance using free-space path loss
def fspl_dB(distance_m):
    return 20*math.log10(4*math.pi*distance_m/lam)
# Iterate to find distance where interference falls below threshold
threshold_dBm = Pr_sat_dBm - Rp_dB  # allowed interference power at satellite input
for d_km in range(1,5000):
    path_loss = fspl_dB(d_km*1000)
    Pr_at_sat = Pt_target + Gt - path_loss   # dBm
    if Pr_at_sat < threshold_dBm:
        print(f"Exclusion radius ~ {d_km} km")  # simple operational estimate
        break
# Note: this is a simplified model; real analysis includes elevation angle, clutter, and antenna patterns.