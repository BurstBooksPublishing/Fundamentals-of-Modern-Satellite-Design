import math
# simple calculator for boil-off and pressurant mass
L_v = 2.1e5        # latent heat J/kg (example for LOX)
Q_leak = 50.0      # heat leak W into tank
mdot_boil = Q_leak / L_v  # kg/s boil-off
# pressurant mass via ideal gas (isothermal)
p_final = 2e5      # final ullage pressure Pa
V_ullage = 0.2     # ullage volume m3
R_he = 2077.0      # J/(kg K) for helium
T = 293.0          # K
m_press = p_final * V_ullage / (R_he * T)  # kg
# brief prints for mission check
print(f"Boil-off kg/day: {mdot_boil*86400:.3f}")  # # day-scale loss
print(f"Pressurant mass kg: {m_press:.4f}")      # helium mass