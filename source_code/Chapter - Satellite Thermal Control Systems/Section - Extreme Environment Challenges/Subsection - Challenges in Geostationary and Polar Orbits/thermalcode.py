import numpy as np
sigma = 5.670374419e-8  # Stefan-Boltzmann
# thermal parameters (J/K and W/K)
C_polar = 500.0   # moderate thermal capacitance (payload panel)
G_polar = 0.5     # conductance to radiator
C_geo = 2000.0    # larger bus thermal mass in GEO
G_geo = 0.2
# orbital angular frequencies
omega_polar = 2*np.pi / (5400.0)   # 90-min period
omega_geo   = 2*np.pi / (86400.0)  # 24-hr period
# incident heat amplitudes (W)
P0_polar = 20.0   # variable albedo/solar on panel
P0_geo   = 50.0   # eclipse-induced variation (waste heat redistribution)
# amplitude calc per eq (2)
amp_polar = (P0_polar/C_polar) / np.sqrt(omega_polar**2 + (G_polar/C_polar)**2)
amp_geo   = (P0_geo/C_geo) / np.sqrt(omega_geo**2 + (G_geo/C_geo)**2)
print("Polar LEO temperature amplitude (K):", amp_polar)
print("GEO temperature amplitude (K):", amp_geo)
# Use results to size heaters or thermal straps (design decision point).