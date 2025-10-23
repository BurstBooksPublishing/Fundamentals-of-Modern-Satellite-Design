import math

# Inputs: component mass (kg), specific heat J/kg/K, deltaT K, allowed time s
def heater_power(mass, cp, deltaT, time_allowed, area, emissivity, T_target, T_space=3.0):
    # Basic energy required
    energy = mass * cp * deltaT  # J
    # Radiative loss estimate using Stefan-Boltzmann (simple vacuum radiative loss)
    sigma = 5.670374419e-8
    Q_loss = emissivity * sigma * area * (T_target**4 - T_space**4)  # W
    # Nominal power to meet time plus losses
    P_required = energy / time_allowed + Q_loss
    return P_required, energy, Q_loss

# Example: catalyst bed 0.15 kg, cp 500 J/kgK, need +100 K in 120 s
P, E, Q = heater_power(0.15, 500, 100, 120, area=0.01, emissivity=0.8, T_target=350)
# P is heater sizing recommendation (W). # Use battery/solar budget to validate.
print(f"Power {P:.1f} W, Energy {E:.1f} J, Radiative loss {Q:.1f} W")