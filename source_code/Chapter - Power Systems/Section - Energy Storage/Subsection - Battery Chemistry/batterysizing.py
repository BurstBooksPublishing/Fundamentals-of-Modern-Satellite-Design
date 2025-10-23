import math

# Mission parameters (example for a LEO comms satellite)
E_eclipse_Wh = 1500.0      # Wh required during eclipse
V_bus = 28.0               # Bus voltage (V)
DoD = 0.7                  # Depth-of-discharge (fraction)
eta_roundtrip = 0.9        # Charge/discharge efficiency
cycles_per_day = 2         # Two eclipse cycles per day
mission_years = 5

# Chemistry degradation parameters (tuned from test data)
alpha_cycle = 1e-4         # fraction loss per cycle
k0 = 1e-7                  # calendar pre-exponential factor (1/s)
Ea = 50000.0               # activation energy (J/mol)
R = 8.314                  # J/(mol*K)
T_oper = 298.0             # Kelvin

# Required nominal capacity (Ah)
C_nom_Ah = E_eclipse_Wh / (V_bus * DoD * eta_roundtrip)

# Time and cycle simulation
days = int(mission_years * 365)
capacity_Ah = C_nom_Ah
for day in range(days):
    # apply cycle degradation
    capacity_Ah *= (1 - alpha_cycle * cycles_per_day)
    # apply calendar degradation increment (Arrhenius rate)
    k = k0 * math.exp(-Ea / (R * T_oper))
    capacity_Ah *= math.exp(-k * 86400.0)  # one day
# report
print(f"Initial required capacity: {C_nom_Ah:.1f} Ah")
print(f"Capacity after {mission_years} years: {capacity_Ah:.1f} Ah")