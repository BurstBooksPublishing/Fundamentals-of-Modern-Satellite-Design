import math

g0 = 9.80665  # m/s^2

# Example propellants: (Isp_s, density_kg_per_m3)
propellants = {
    'hydrazine': (220.0, 1020.0),
    'AFM315E':  (240.0, 1220.0),
    'MMH_N2O4':  (320.0, 1320.0),  # representative combined density
    'LOX_RP1':   (340.0, 950.0),
    'LOX_LH2':   (450.0, 400.0)    # combined effective density for tanks
}

def prop_fraction(delta_v, Isp):
    return 1.0 - math.exp(-delta_v / (g0 * Isp))

# Example: compare for delta-v = 750 m/s
dv = 750.0
for name, (Isp, rho) in propellants.items():
    frac = prop_fraction(dv, Isp)
    print(f"{name}: Isp={Isp:.0f} s, prop_frac={frac:.3f}, rho={rho:.0f} kg/m^3")
# Comments: densities are engineering approximations; refine for tank sizing.