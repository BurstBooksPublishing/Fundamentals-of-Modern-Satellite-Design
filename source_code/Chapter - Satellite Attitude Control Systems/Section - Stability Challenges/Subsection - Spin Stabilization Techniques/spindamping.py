import math
# Inputs (example satellite)  # inertia in kg*m^2, spin in rpm, damping tau in seconds
I1, I3 = 0.6, 0.8         # transverse and spin inertia
spin_rpm = 30.0
tau_d = 600.0             # damping time constant (s)

# Convert spin to rad/s
omega_s = spin_rpm * 2.0 * math.pi / 60.0

# Nutation frequency (rad/s) per equation (1)
omega_n = (I3 - I1) / I1 * omega_s

# Angular momentum
L = I3 * omega_s

# Simple exponential decay of nutation angle (initial 5 deg)
theta0 = math.radians(5.0)
times = [i*60 for i in range(0, 61)]  # 0..3600 s in 1-min steps
theta = [theta0 * math.exp(-t / tau_d) for t in times]

# Print key sizing outputs (inline comments)
print(f"omega_s={omega_s:.2f} rad/s")  # spin rate
print(f"omega_n={omega_n:.3f} rad/s")  # nutation frequency
print(f"L={L:.3f} N*m*s")             # stored momentum
# End: theta list contains nutation amplitude over time for planning