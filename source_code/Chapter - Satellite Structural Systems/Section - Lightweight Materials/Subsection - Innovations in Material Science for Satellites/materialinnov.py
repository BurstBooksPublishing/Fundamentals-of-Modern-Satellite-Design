import numpy as np
# Material properties (conservative)
E_al = 71e9      # Pa for Al 7075-T6
rho_al = 2700.0  # kg/m^3
E_cfrp = 130e9   # Pa along fiber (quasi-isotropic effective assumption)
rho_cfrp = 1600.0# kg/m^3

# Geometry for beam-like panel
L = 1.0          # m span
b = 0.2          # m width
t = 0.005        # m thickness
A = b * t
I = (b * t**3) / 12.0

# specific stiffness and frequency
spec_al = E_al / rho_al
spec_cfrp = E_cfrp / rho_cfrp
f1_al = (np.pi/2.0) * np.sqrt((E_al * I) / (rho_al * A * L**4))
f1_cfrp = (np.pi/2.0) * np.sqrt((E_cfrp * I) / (rho_cfrp * A * L**4))

print("Specific stiffness Al:", spec_al)
print("Specific stiffness CFRP:", spec_cfrp)
print("f1 Al (Hz):", f1_al)
print("f1 CFRP (Hz):", f1_cfrp)
print("Frequency ratio CFRP/Al:", f1_cfrp / f1_al)  # >1 indicates higher stiffness-to-weight