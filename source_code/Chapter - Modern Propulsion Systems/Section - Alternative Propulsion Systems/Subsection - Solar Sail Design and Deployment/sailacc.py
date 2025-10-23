import math
S0 = 1361.0            # W/m^2 at 1 AU
c = 299792458.0        # m/s
def sail_acceleration(sigma, r_AU, R, alpha_deg):
    alpha = math.radians(alpha_deg)
    # acceleration magnitude per equation (H)\label{eq:radpress}
    a = (1.0 + R) * S0 / c * (1.0 / sigma) * (1.0 / (r_AU**2)) * (math.cos(alpha)**2)
    # acceleration components in Sun-velocity plane
    ax = a * math.cos(alpha)         # radial (sunward) component
    ay = a * math.sin(alpha)         # transverse (along velocity) component
    return a, ax, ay

# Example: sigma = 5e-3 kg/m^2 (5 g/m^2), reflectivity 0.9, pitch 30 deg at 1 AU
a_total, a_radial, a_trans = sail_acceleration(5e-3, 1.0, 0.9, 30.0)
# returns accelerations in m/s^2 for trade studies