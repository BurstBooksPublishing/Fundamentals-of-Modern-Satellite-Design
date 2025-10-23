import math

# Inputs (example GEO dish panel)
I_panel = 25.0     # kg*m^2 rotational inertia about hinge
theta = math.radians(120.0)  # radians to deploy
t_deploy = 30.0    # seconds desired deployment time
T_friction = 2.0   # N*m Coulomb friction estimate
T_preload = 1.5    # N*m hinge preload
safety_margin = 1.5  # factor

# Compute required torque using eq (1) and (2)
alpha = 2*theta / (t_deploy**2)              # rad/s^2
T_inertia = I_panel * alpha                  # N*m
T_spec = safety_margin * (T_inertia + T_friction + T_preload)

print(f"alpha = {alpha:.5f} rad/s^2")
print(f"T_inertia = {T_inertia:.2f} N*m")
print(f"T_spec = {T_spec:.2f} N*m  # required motor torque")
# simple check against motor gearbox choices (mock)
gear_ratio = 100.0
motor_torque = T_spec / gear_ratio
print(f"motor torque at rotor = {motor_torque:.3f} N*m (before dynamic margin)")