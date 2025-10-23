import numpy as np

# Constants
sigma = 5.670374419e-8   # Stefan-Boltzmann, W/m^2/K^4
S0 = 1361.0              # Solar constant, W/m^2

# Design parameters (modify for mission)
area = 2.0               # m^2 effective radiating area
epsilon = 0.8            # emissivity
alpha = 0.2              # absorptivity to sun
mass = 50.0              # kg
cp = 900.0               # J/kg/K specific heat
Q_internal = 200.0       # W steady internal dissipation
solar_illum = 1.0        # fraction of full sun (0..1)

# Approximate absorbed solar (normal incidence)
Q_solar = alpha * S0 * area * solar_illum

# Solve for equilibrium temperature: epsilon*sigma*A*T^4 = Q_solar + Q_internal
Teq = ((Q_solar + Q_internal) / (epsilon * sigma * area))**0.25
C = mass * cp
tau = C / (4 * epsilon * sigma * area * Teq**3)

print(f"Equilibrium T = {Teq-273.15:.1f} °C, time constant = {tau/3600:.2f} h")
# Use this output to size radiators, heaters, or PCM mass.