import math
# simple parameters (example values)
sigma = 1e-12   # cm^2/bit cross-section
phi0 = 1e4      # particles/cm^2/s at surface
mu = 0.02       # 1/(g/cm^2) attenuation coeff
bits = 8e6      # number of memory bits
seconds_per_day = 86400

def expected_upsets(shield_g_cm2):
    phi = phi0 * math.exp(-mu * shield_g_cm2)           # attenuated flux
    r_seu = sigma * phi * bits                         # upsets per second
    return r_seu * seconds_per_day                     # upsets per day

for x in [0, 1, 2, 5, 10]:                              # shielding in g/cm^2
    print(f"shield={x} g/cm^2 -> {expected_upsets(x):.3f} upsets/day")
# Note: use mission-specific flux and cross-section from test data.