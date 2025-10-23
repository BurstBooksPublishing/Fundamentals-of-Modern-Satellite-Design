import math
from scipy.optimize import brentq

# constants
sigma = 5.670374419e-8       # Stefan-Boltzmann, W/m^2/K^4
A = 0.5                      # radiating area, m^2 (example)
epsilon = 0.03               # effective emissivity with MLI (tunable)
P_int = 5.0                  # internal dissipation, W
P_ext = 100.0                # absorbed external power, W (solar+albedo comp.)
T_structure = 300.0          # structural temperature, K (conductive sink)
kA_over_L = 0.1              # effective conduction W/K (lumped)

def net_power(T):
    # net power at temperature T: positive means heating
    return P_int + P_ext - (epsilon * sigma * A * (T**4)) - (kA_over_L * (T - T_structure))

# solve between 3 K and 800 K
T_eq = brentq(net_power, 3.0, 800.0)
print("Equilibrium temperature: {:.1f} K".format(T_eq))