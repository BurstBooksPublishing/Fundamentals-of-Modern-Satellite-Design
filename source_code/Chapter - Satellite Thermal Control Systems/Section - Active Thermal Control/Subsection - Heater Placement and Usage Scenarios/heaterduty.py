# Simple heater duty-cycle estimator for maintaining battery temperature.
# Inputs: thermal parameters and mission constraints.
m = 5.0            # battery mass, kg
c = 900.0          # specific heat, J/(kg*K) (approx. Li-ion pack)
deltaT = 10.0      # allowed temperature swing, K
t_rise = 3600.0    # allowed warm-up time, s (1 hour)
Q_int = 1.0        # internal dissipation, W
R_th = 5.0         # thermal resistance to space, K/W
T_set = 273.0      # setpoint K
T_env = 200.0      # worst-case environment K
# Energy to raise temperature
E_needed = m * c * deltaT         # J
P_heater_peak = E_needed / t_rise # W required during warm-up
# Steady-state heater to hold temperature (eq. [1])
Q_hold = (T_set - T_env)/R_th - Q_int
Q_hold = max(Q_hold, 0.0)         # no negative heating
# Duty fraction for average power limit (P_avg_lim)
P_avg_lim = 15.0                  # available average power, W
duty = min(1.0, P_avg_lim / max(Q_hold, 1e-6))
print("Peak heater (W):", P_heater_peak)
print("Hold heater (W):", Q_hold)
print("Required duty fraction for hold:", duty)