import numpy as np

mu=3.986004418e14          # Earth's mu, m^3/s^2
Re=6371000.0               # Earth radius, m
P_sun=4.56e-6              # Solar pressure at 1 AU, N/m^2

def gravity_gradient_torque(I, r_vec):
    # I: 3x3 inertia matrix; r_vec: position vector (m)
    r_hat=r_vec/np.linalg.norm(r_vec)
    return 3*mu/np.linalg.norm(r_vec)**3 * np.cross(r_hat, I.dot(r_hat))

def srp_torque(A, Cp, L, solar_incidence=True):
    # A: area m^2, Cp: coeff, L: lever arm m
    sign=1.0 if solar_incidence else 0.0
    return P_sun*A*Cp*L*sign

def magnetic_torque(m_vec, B_vec):
    # m_vec: residual dipole (A·m^2), B_vec: geomagnetic field (T)
    return np.cross(m_vec, B_vec)

# Example usage (values are illustrative)
I=np.diag([50,60,80])      # kg·m^2
r_vec=np.array([Re+700e3,0,0])
Tgg=gravity_gradient_torque(I,r_vec)   # gravity-gradient vector
Tsrp=srp_torque(4.0,1.5,1.0)           # SRP scalar (approx)
Tmag=magnetic_torque(np.array([0.1,0,0]), np.array([2e-5,0,0]))
print(Tgg, Tsrp, Tmag)  # brief output for trade studies