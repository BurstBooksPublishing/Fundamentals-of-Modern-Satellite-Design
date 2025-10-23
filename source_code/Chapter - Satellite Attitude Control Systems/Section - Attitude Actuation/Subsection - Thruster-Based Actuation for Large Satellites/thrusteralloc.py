import numpy as np
# geometry: 3 thrusters producing torques in roll,pitch,yaw (N*m per unit time)
B = np.array([[ 1.2, -1.2,  0.0],   # mapping matrix (example values)
              [ 0.0,  1.0, -1.0],
              [-0.5,  0.5,  1.0]])
tau_des = np.array([5.0, -2.0, 1.0])  # desired torque (N*m)
# unconstrained LS solution
u, *_ = np.linalg.lstsq(B, tau_des, rcond=None)
# enforce non-negativity and max pulse-width (u_max)
u = np.clip(u, 0.0, 10.0)  # seconds or normalized units
print(u)  # pulse widths/firing durations for each thruster