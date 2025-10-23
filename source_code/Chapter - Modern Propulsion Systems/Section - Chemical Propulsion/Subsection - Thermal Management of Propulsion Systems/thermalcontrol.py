import math
# inputs: heat (W), emissivity, allowed_temp_C
Q_diss = 200.0             # W, example continuous dissipation for bipropellant heater
eps = 0.85                 # high-emissivity paint
T_allowed = 323.15         # K (50 C)
sigma = 5.670374419e-8
A = Q_diss / (eps * sigma * T_allowed**4)  # Eq. (rad_area)
print(f"Radiator area = {A:.3f} m^2")       # area result
# further checks: mass penalty vs. heater power trade-off up to mission constraints