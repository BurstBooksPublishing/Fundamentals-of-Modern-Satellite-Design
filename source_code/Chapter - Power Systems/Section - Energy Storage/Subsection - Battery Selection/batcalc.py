# Simple battery sizing and lifetime estimator
E_req = 500.0          # Wh, eclipse energy requirement
e_spec = 150.0         # Wh/kg, specific energy (Li-ion)
f_DoD = 0.8            # usable fraction (DoD)
eta_EoL = 0.8          # EoL capacity margin
# Mass calculation (kg)
m_bat = E_req / (e_spec * f_DoD * eta_EoL)
# Cycle life estimate using eq. (cycles)
N_ref = 3000.0         # cycles at DoD_ref
DoD_ref = 0.8
k = 0.8
DoD = 0.6              # planned operational DoD
N_cycles = N_ref * (DoD_ref/DoD)**k
# Mission life in years for daily cycling
cycles_per_year = 365.0
years_life = N_cycles / cycles_per_year
print(f"Battery mass {m_bat:.2f} kg, estimated cycles {N_cycles:.0f}, life {years_life:.1f} yr")
# Check C-rate (example)
P_peak = 200.0         # W peak payload draw
V_bus = 28.0           # V bus
I_peak = P_peak / V_bus
C_cell_Ah = 10.0       # cell capacity Ah
C_req = I_peak / C_cell_Ah
# Display C-rate requirement
print(f"Peak current {I_peak:.2f} A, required C-rate {C_req:.2f} C")