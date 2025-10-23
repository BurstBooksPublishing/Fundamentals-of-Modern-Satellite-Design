# Simple computation of angular accel and slosh freq (engineering tool)
import math

# spacecraft and disturbance parameters (example: Earth observation smallsat)
I = 50.0              # kg*m^2, principal inertia
T_disturb = 1e-3      # N*m, disturbance torque (1 mN*m)
H_wheel_max = 0.2     # N*m*s, wheel momentum capacity

# angular acceleration (rad/s^2)
alpha = T_disturb / I
# time to saturate wheel if torque constant (s)
t_to_sat = H_wheel_max / T_disturb

# slosh frequency estimate (capillary scaling)
sigma = 0.072         # N/m, water surface tension at 20C
rho = 1000.0          # kg/m^3, water density
L = 0.2               # m, characteristic tank length
omega_n = math.sqrt(sigma / (rho * L**3))

print(f"alpha = {alpha:.3e} rad/s^2")          # small angular accel
print(f"time to wheel saturation = {t_to_sat:.1f} s")
print(f"estimated slosh freq = {omega_n:.3f} rad/s (~{omega_n/(2*math.pi):.3f} Hz)")
# Use results to set controller bandwidth and desaturation schedule.