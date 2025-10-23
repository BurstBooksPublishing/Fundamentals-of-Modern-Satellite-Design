import math

# inputs (example): solar constant at 1 AU (W/m^2)
S0 = 1361.0
# effective incident solar flux (W/m^2) including projection and albedo
S_eff = 0.9 * S0  # e.g., sun angle and albedo factor
alpha = 0.12      # solar absorptance (dimensionless)
epsilon = 0.85    # thermal emissivity (dimensionless)
Q_int = 20.0      # internal dissipation (W)
A = 1.0           # radiating area (m^2)
Q_IR = 50.0       # absorbed Earth IR per m^2 (W/m^2)
sigma = 5.670374419e-8

# compute net absorbed flux per unit area
q_abs = alpha * S_eff + Q_int / A + Q_IR

# equilibrium temperature (K)
T_eq = (q_abs / (epsilon * sigma)) ** 0.25
print(f"Equilibrium temperature: {T_eq:.1f} K")
# adjust alpha for contamination and recompute quickly
alpha_contam = alpha + 0.03  # contamination increases absorptance
T_contam = ((alpha_contam * S_eff + Q_int/A + Q_IR) / (epsilon * sigma)) ** 0.25
print(f"With contamination (Delta alpha=0.03): {T_contam:.1f} K")