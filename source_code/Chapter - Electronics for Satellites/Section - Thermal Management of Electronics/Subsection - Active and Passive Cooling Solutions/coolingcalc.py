import math
sigma = 5.670374419e-8  # Stefan-Boltzmann constant
Q_in = 400.0            # heat to reject in watts (example GEO payload)
epsilon = 0.85          # radiator emissivity
T = 300.0               # desired radiator temperature (K)
T_space = 3.0           # effective deep-space temp (K)
A = Q_in / (epsilon * sigma * (T**4 - T_space**4))  # area in m^2
print(f"Required radiator area: {A:.3f} m^2")  # brief output