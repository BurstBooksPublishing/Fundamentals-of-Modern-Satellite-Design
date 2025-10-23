import math

g0 = 9.80665  # m/s^2
def prop_mass_fraction(delta_v, Isp):
    return 1.0 - math.exp(-delta_v / (Isp * g0))

# Example: 300 m/s delta-v budget for a 500 kg spacecraft
delta_v = 300.0  # m/s
m0 = 500.0       # kg (initial mass incl. propellant)

# Monoprop hydrazine Isp ~ 225 s; biprop MMH/NTO Isp ~ 320 s
mp_frac_mono = prop_mass_fraction(delta_v, 225.0)
mp_frac_bi   = prop_mass_fraction(delta_v, 320.0)

mp_mono = m0 * mp_frac_mono  # propellant mass mono
mp_bi   = m0 * mp_frac_bi    # propellant mass bi

print(f"Monopropellant mass required: {mp_mono:.1f} kg")  # # compute
print(f"Bipropellant mass required: {mp_bi:.1f} kg")