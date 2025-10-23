import math
# Inputs (example for 2W device)  # units: SI
P = 2.0                 # power dissipated [W]
k_cu = 400.0            # copper thermal conductivity [W/mK]
via_dia = 0.5e-3        # via drilled diameter [m]
via_annulus = 0.15e-3   # plated annulus thickness (radial) [m]
board_thickness = 1.6e-3# board thickness [m]
pitch = 1.0e-3          # via pitch (not used directly) [m]
dT_target = 10.0        # allowable temp rise [K]

# approximate single-via effective conduction area (circular annulus)
via_area = math.pi*((via_dia/2 + via_annulus)**2 - (via_dia/2)**2)
# via thermal conductance (1D approx)
G_via = k_cu * via_area / board_thickness
# number of vias required (parallel conductors)
n_vias = math.ceil(P / (G_via * dT_target))
print("Estimated vias required:", n_vias)  # inline comment: conservative estimate