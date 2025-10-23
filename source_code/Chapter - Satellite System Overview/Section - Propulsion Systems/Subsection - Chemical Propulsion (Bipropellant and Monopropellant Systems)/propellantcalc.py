import math

def propellant_mass(delta_v, Isp, mass_initial):
    g0 = 9.80665                       # m/s^2
    # Rocket equation: m_p = m0*(1 - exp(-dv/(Isp*g0)))
    mass_prop = mass_initial * (1.0 - math.exp(-delta_v/(Isp*g0)))
    return mass_prop

# Example: 200 m/s delta-v, Isp=310 s, initial mass 3000 kg
# result used to compare monopropellant vs bipropellant sizing
print(propellant_mass(200.0, 310.0, 3000.0))  # kg  # compute prop mass