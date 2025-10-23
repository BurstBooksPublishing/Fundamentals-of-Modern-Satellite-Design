import math

g0 = 9.80665  # m/s^2
def propellant_mass(dry_mass, delta_v, isp):
    # returns propellant mass required (kg) using Tsiolkovsky
    m0_mf = math.exp(delta_v / (isp * g0))
    m0 = dry_mass * m0_mf
    return m0 - dry_mass

# Example satellite: dry_mass = 1000 kg, delta_v = 1500 m/s (GTO->GEO)
dry = 1000.0
dv = 1500.0
isos = {'Hydrazine monoprop':220, 'Hypergolic biprop':320, 'Cryogenic LH2/LOX':450}
for name, isp in isos.items():
    m_prop = propellant_mass(dry, dv, isp)
    print(f"{name}: Isp={isp} s -> Propellant mass = {m_prop:.1f} kg")  # concise results