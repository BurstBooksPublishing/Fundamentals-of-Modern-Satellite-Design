import math

# inputs (engineering values)
I_axis = 10.0           # kg*m^2, satellite inertia about control axis
theta = math.radians(30) # rad, desired slew
t_slew = 60.0           # s, time to slew
tau_dist = 5e-3         # N*m, worst-case disturbance torque
B_field = 3e-5          # T, typical LEO magnetic field magnitude

# compute peak accel and torque
alpha_max = 4*theta / (t_slew**2)            # eq (1)
tau_req = I_axis*alpha_max + tau_dist       # eq (2)

# choose wheel torque margin
tau_rw_design = max(0.02, 2*tau_req)         # N*m, select margin

# momentum storage requirement (example)
omega_sat = 0.01                              # rad/s worst-case spacecraft rate
H_margin = 0.1                                # N*m*s margin
h_required = I_axis*omega_sat + H_margin      # eq (4)

# magnetorquer dipole to desaturate in field
m_req = h_required / B_field                  # approximate dipole (A*m^2)

# print results (brief inline comments)
print(f"alpha_max = {alpha_max:.3e} rad/s^2")   # accel need
print(f"tau_req = {tau_req:.3e} N*m")          # torque need
print(f"tau_rw_design = {tau_rw_design:.3e} N*m") # wheel torque chosen
print(f"h_required = {h_required:.3e} N*m*s")  # momentum storage required
print(f"m_req = {m_req:.3e} A*m^2")            # magnetorquer dipole required