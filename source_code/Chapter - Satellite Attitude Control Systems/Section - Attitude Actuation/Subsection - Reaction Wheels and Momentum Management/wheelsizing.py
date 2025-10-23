import math

# Input: required body impulse (Nms) and max wheel speed (rad/s)
def wheel_inertia_required(delta_H_req, omega_w_max):
    # returns minimum wheel inertia in kg*m^2
    return delta_H_req / omega_w_max

# Input: momentum to remove (Nms), dipole moment (A*m^2), B-field (T)
def magnetorquer_dump_time(H_remove, m_dipole, B_field):
    # conservative torque: tau = m * B
    tau = m_dipole * B_field
    if tau <= 0:
        return float('inf')
    return H_remove / tau  # seconds

# Example usage for a 100-kg EO satellite
delta_H = 0.04  # Nms from sizing example
omega_max = 628.0  # rad/s (6000 rpm)
Iw = wheel_inertia_required(delta_H, omega_max)
# magnetorquer 0.5 A*m^2 in LEO, B~3e-5 T
dump_time = magnetorquer_dump_time(0.2, 0.5, 3e-5)  # remove 0.2 Nms
print("I_w min:", Iw, "kg*m^2")         # wheel inertia requirement
print("Dump time:", dump_time, "s")     # magnetorquer dump time