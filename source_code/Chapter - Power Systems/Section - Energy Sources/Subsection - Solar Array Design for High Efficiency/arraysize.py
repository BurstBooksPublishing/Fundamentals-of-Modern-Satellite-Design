import numpy as np

# Mission inputs (example)
P_req_EOL = 120.0          # W required at EOL (payload + charge)
G0 = 1361.0                # W/m^2 solar constant
eta_cell_BOL = 0.30        # BOL efficiency
degradation = 0.15         # 15% EOL degradation
eta_sys = 0.88             # system losses (optical+electrical)
cos_theta = 0.95           # worst-case incidence

# Derived efficiencies
eta_cell_EOL = eta_cell_BOL * (1.0 - degradation)
# Area from eq. (1)
A = P_req_EOL / (G0 * eta_cell_EOL * eta_sys * cos_theta)
# Electrical sizing assume cell V_mp and I_mp at STC
V_cell_mp = 0.68           # V per multi-junction cell at V_mp
I_cell_mp = 0.05           # A per cell (example small cell)
# pick string voltage ~ bus MPPT V_mp (e.g., 28V -> ~41 cells)
V_bus_mp = 28.0
n_cells_per_string = int(np.ceil(V_bus_mp / V_cell_mp))
# string current and count
I_string = I_cell_mp       # series cells same current
I_required = P_req_EOL / V_bus_mp
n_parallel_strings = int(np.ceil(I_required / I_string))

print(f"Required area: {A:.2f} m^2")
print(f"Cells per string: {n_cells_per_string}, parallel strings: {n_parallel_strings}")