import math
sigma = 5.670374419e-8            # Stefan-Boltzmann
Qint = 500.0                      # W, internal dissipation
T = 300.0                         # K, radiator temp
eps = 0.88
alpha = 0.12
Gsun = 1361.0                     # W/m2
G_EIR = 237.0                     # W/m2
# two illumination cases
cases = [
  ("sunlit", 0.05, 0.5),
  ("eclipse", 0.0, 0.5)
]
for name, Fsun, FE in cases:
    denom = eps*sigma*T**4 - alpha*Gsun*Fsun - eps*G_EIR*FE
    if denom <= 0:
        print(name, "impossible at T=", T)
    else:
        A = Qint / denom
        print(f"{name}: Area = {A:.2f} m2")  # minimal comments; use for trade studies