import math
# Inputs (SI units)
I_panel = 2.5  # kg*m^2, panel rotational inertia about hinge
f_target = 2.0  # Hz, desired first mode
omega_n = 2*math.pi*f_target

# Required hinge stiffness for modal constraint
k_required = I_panel * omega_n**2
# Deployment torque limit to keep angular accel below alpha_max
alpha_max = 0.05  # rad/s^2 allowable during deployment
tau_limit = I_panel * alpha_max

print(f"Required stiffness k = {k_required:.2f} N*m/rad")
print(f"Deployment torque limit tau = {tau_limit:.2f} N*m")
# Simple check against reaction wheel capability (example)
wheel_torque_margin = 0.2  # N*m available to absorb impulse
if tau_limit > wheel_torque_margin:
    print("# Warning: ADCS may not absorb deployment impulse.")