# simple screening: stress and RF proxy; replace with measured curves for flight design
import math

# candidate materials: name, alpha (1/K), E (GPa), eps_r, tan_delta, k (W/mK)
materials = [
  ("AlN", 4.7e-6, 330, 8.5, 0.0005, 170.0),
  ("Rogers_RO4350B", 6.0e-6, 20, 3.48, 0.0037, 0.6),
  ("Polyimide", 20e-6, 2.5, 3.5, 0.02, 0.12),
  ("HighTg_epoxy", 14e-6, 20, 4.5, 0.02, 0.3),
]

deltaT = 100.0  # expected thermal swing (K)
f = 2.4e9       # RF frequency (Hz)
c = 3e8

for m in materials:
    name, alpha, E_gpa, eps_r, tan_d, k = m
    # use silicon alpha ~2.6e-6, E ~130 GPa for package estimate
    sigma = 130e9 * (alpha - 2.6e-6) * deltaT  # Pa, from eqn approximation
    rf_proxy = (math.pi * f * math.sqrt(eps_r) * tan_d) / c  # approx attenuation factor
    print(f"{name}: stress={sigma/1e6:.1f} MPa, rf_proxy={rf_proxy:.3e}, k={k} W/mK")