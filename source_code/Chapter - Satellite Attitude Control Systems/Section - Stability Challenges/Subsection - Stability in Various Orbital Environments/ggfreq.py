import numpy as np
# constants
mu = 3.986004418e14    # Earth's mu, m^3/s^2
R_earth = 6371e3       # Earth radius, m

def libration_frequency(h_km, I_x, I_z):
    r = R_earth + h_km*1e3
    omega_n2 = 3*mu/(r**3) * (I_z - I_x)/I_x
    return np.sqrt(abs(omega_n2))*np.sign(omega_n2)  # rad/s, sign indicates stable/unstable

# example: 700 km altitude, typical smallsat inertia (kg m^2)
print(libration_frequency(700, I_x=10.0, I_z=12.0))  # positive -> oscillatory natural mode