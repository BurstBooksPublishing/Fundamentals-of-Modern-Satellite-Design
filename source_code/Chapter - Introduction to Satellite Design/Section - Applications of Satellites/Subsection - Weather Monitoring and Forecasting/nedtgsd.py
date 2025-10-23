import math
# Input parameters (engineering units)
T_sys = 300.0         # K, system noise temperature
bandwidth = 1e9       # Hz, receiver bandwidth
tau = 0.1             # s, integration time per pixel
altitude = 800e3      # m, satellite altitude
ifov = 50e-6          # rad, instantaneous field of view

# Compute NEΔT using radiometer equation
delta_T = T_sys / math.sqrt(bandwidth * tau)
# Compute GSD using approximate geometry
gsd = altitude * ifov

print(f"NEΔT = {delta_T:.3f} K")   # radiometric sensitivity
print(f"GSD = {gsd:.1f} m")        # ground sample distance