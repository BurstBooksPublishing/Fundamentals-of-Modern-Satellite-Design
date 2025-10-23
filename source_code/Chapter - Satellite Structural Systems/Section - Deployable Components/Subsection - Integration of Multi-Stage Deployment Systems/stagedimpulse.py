import numpy as np

# Satellite and wheel parameters (example values)
I_sat = 120.0         # spacecraft moment of inertia, kg*m^2
H_wheel_max = 50.0    # reaction wheels total capacity, N*m*s
thruster_reserve = 30.0  # reserve desat capability, N*m*s

# Stage definitions: (peak_torque_Nm, duration_s, safety_factor)
stages = [
    (5.0, 2.0, 1.1),   # small panel
    (12.0, 1.5, 1.2),  # antenna subreflector
    (8.0, 3.0, 1.0),   # solar wing half
]

def angular_impulse(torque, duration, sf):
    # triangular pulse approximation => impulse = 0.5*peak*duration
    return 0.5 * torque * duration * sf

H_total = 0.0
for i, (tau, dur, sf) in enumerate(stages, start=1):
    H_i = angular_impulse(tau, dur, sf)
    H_total += H_i
    delta_omega = H_i / I_sat
    # simple check against wheel capacity
    print(f"Stage {i}: H_i={H_i:.2f} N*m*s, delta_omega={delta_omega:.6f} rad/s")

H_avail = H_wheel_max + thruster_reserve
print(f"Cumulative H={H_total:.2f} N*m*s, Available H={H_avail:.2f} N*m*s")
# If H_total exceeds H_avail, plan for additional dwell or different sequence.