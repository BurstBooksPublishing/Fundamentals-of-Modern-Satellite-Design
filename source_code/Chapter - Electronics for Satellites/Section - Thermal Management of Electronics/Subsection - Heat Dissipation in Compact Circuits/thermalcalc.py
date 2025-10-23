import math
# Inputs (SI units)
P = 2.0                      # power dissipation (W)
T_env = 250.0                # radiator temperature (K)
R_jc = 5.0                   # junction-to-case (K/W)
R_cond = 13.0                # PCB conduction (K/W) from Eq.(3)
A = 4e-4                     # radiating area (m^2)
eps = 0.8
sigma = 5.670374419e-8
# linearized radiative h at T~300K
T_ref = 300.0
h_rad = 4*eps*sigma*(T_ref**3)
R_rad = 1.0/(h_rad*A)        # radiative resistance (K/W)
R_total = R_jc + R_cond + R_rad
Tjunction = T_env + P*R_total
print(f"R_total={R_total:.1f} K/W, T_junction={Tjunction:.1f} K")
# Adjust design: add thermal strap reduces R_cond
R_cond_new = 1.0
R_total_new = R_jc + R_cond_new + R_rad
print(f"With strap T_j={T_env + P*R_total_new:.1f} K")