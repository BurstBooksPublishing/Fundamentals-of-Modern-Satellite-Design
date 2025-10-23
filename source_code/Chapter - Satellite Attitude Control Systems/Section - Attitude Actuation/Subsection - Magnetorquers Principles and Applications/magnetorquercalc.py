# Simple magnetorquer sizing (SI units)
I = 0.01                # kg*m^2, example inertia
alpha_req = 0.01        # rad/s^2, desired angular accel
B_min = 3e-5            # T, worst-case LEO field
m_req = I*alpha_req/B_min   # required dipole (A*m^2)

# coil geometry and electrical limits
area = 0.01             # m^2, loop area (0.1m x 0.1m)
I_c_max = 0.5           # A, max continuous current
N_needed = m_req/(I_c_max*area)  # turns required

print(f"Required dipole m = {m_req:.3f} A*m^2")  # numeric result
print(f"Turns needed at {I_c_max} A and {area} m^2 = {N_needed:.1f}")