import numpy as np

# Parameters (example Li-ion cell)
m = 0.8            # kg
cp = 800.0         # J/(kg K)
A = 0.05           # m^2 radiating area
eps = 0.85
sigma = 5.670374e-8
T_space = 3.0      # K approximated
R_ref = 0.05       # ohm at T_ref
T_ref = 293.0      # K
Ea = 40000.0       # J/mol (example)
Rg = 8.314         # J/(mol K)

# Temperature-dependent internal resistance (Arrhenius-like approximation)
def R_int(T):
    return R_ref * np.exp(Ea/Rg*(1/T_ref - 1.0/T))

# Simple capacity scaling (empirical)
def capacity_scale(T):
    # linearized around 20°C for demo; replace with cell data
    return max(0.5, 1.0 - 0.01*(293.0 - T)/1.0)

# Time integration
dt = 1.0           # s
t_end = 5400.0     # 90 min orbit
T = 293.0          # initial K
I_profile = 2.0    # A constant draw for demo

temps = []
caps = []
for t in np.arange(0, t_end, dt):
    Q_in = 0.0                      # net environmental input (W) simplified
    P_loss = I_profile**2 * R_int(T)
    Q_rad = eps*sigma*A*(T**4 - T_space**4)
    dTdt = (P_loss + Q_in - Q_rad)/(m*cp)
    T += dTdt*dt
    temps.append(T)
    caps.append(capacity_scale(T))

# outputs for plotting/analysis (not shown)