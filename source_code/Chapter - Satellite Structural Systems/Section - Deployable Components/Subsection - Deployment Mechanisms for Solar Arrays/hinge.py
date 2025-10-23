import numpy as np

# Inputs (SI units)
I_panel = 5.0      # kg*m^2, panel inertia about hinge
I_sat = 200.0      # kg*m^2, spacecraft inertia
theta = np.deg2rad(90.0)  # rad, deployment angle
t_deploy = 20.0    # s, desired deployment time
tau_fric = 0.2     # N*m, estimated friction
c_visc = 0.01      # N*m*s/rad, damping estimate

# Derived
omega_avg = theta / t_deploy        # rad/s (average)
alpha = omega_avg / (t_deploy/2)    # rad/s^2 (approx. triangular profile)
tau_req = I_panel*alpha + c_visc*omega_avg + tau_fric

# Attitude impact
delta_omega_panel = omega_avg       # assume panel reaches avg; conservative
delta_omega_sat = - (I_panel/I_sat) * delta_omega_panel

print(f"Required torque (N*m): {tau_req:.3f}")
print(f"Estimated satellite rate change (deg/s): {np.rad2deg(delta_omega_sat):.4f}")