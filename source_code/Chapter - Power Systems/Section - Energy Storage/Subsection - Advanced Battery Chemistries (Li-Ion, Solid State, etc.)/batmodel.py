import math

# parameters for NMC and LFP cells
cells = {
  'NMC': {'rhoE':200.0, 'alpha':0.0008, 'beta':0.00003},  # Wh/kg, cycle fade, cal prefactor
  'LFP': {'rhoE':140.0, 'alpha':0.00025, 'beta':0.00002}
}

E_req = 200.0     # Wh required per eclipse/weekend or per orbit profile
eta_pack = 0.9
DoD = 0.8
days = 5*365      # 5-year mission
cycles_per_day = 1

for name,p in cells.items():
    m0 = E_req/(eta_pack*DoD*p['rhoE'])             # initial mass kg
    Q0 = 1.0                                       # normalized capacity
    N = cycles_per_day*days
    Qf = Q0 - p['alpha']*N - p['beta']*days        # simplified fade
    mass_EOL = m0 / max(Qf,0.6)                    # sized to meet EOL 60% capacity
    print(f"{name}: init_mass={m0:.2f} kg, SOH_end={Qf:.3f}, mass_EOL={mass_EOL:.2f} kg")
    # interpret results for system margin and thermal control allocation