import math

# Inputs (W); K; emissivity
P = 250.0            # dissipated power, W
Q_env = 50.0         # environmental heat load (solar+earth IR), W
eps = 0.86           # radiator emissivity
T_r = 310.0          # radiator temperature, K
sigma = 5.670374419e-8

# Area from equation (3)
A = (P + Q_env) / (eps * sigma * (T_r**4 - 3.0**4))  # space effective temp ~3 K
print(f"Required radiator area: {A:.2f} m^2")  # simple output