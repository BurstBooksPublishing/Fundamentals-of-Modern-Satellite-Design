import math
sigma = 5.670374419e-8   # Stefan-Boltzmann
A = 1.0                  # m^2 area
Tm = 250.0               # K mean temperature
# empirical emissivity fit parameters (flight-calibrated)
eps_min = 0.002
eps0 = 0.05
alpha = 0.12
# spacer conduction assumptions (sum of supports)
k_spacer = 0.04          # W/mK
A_spacer_total = 1e-3    # m^2 total cross-section
L_spacer = 1e-3          # m (effective path)
G_cond = k_spacer*A_spacer_total/L_spacer
def eps_eff(N):
    return eps_min + (eps0-eps_min)*math.exp(-alpha*N)
def G_rad(N):
    return 4*sigma*A*eps_eff(N)*(Tm**3)
def heat_leak(N, dT):
    return (G_rad(N)+G_cond)*dT
# compute marginal benefit per layer
dT = 50.0
for N in [1,5,10,15,20,30]:
    q = heat_leak(N,dT)
    print(f"N={N:2d}, eps={eps_eff(N):.4f}, q={q:.3f} W")
# find N where incremental reduction < 5% per added layer
prev_q = heat_leak(0,dT)
for N in range(1,61):
    q = heat_leak(N,dT)
    if (prev_q - q)/prev_q < 0.05:
        print("Stop at N=", N, " (less than 5% incremental gain)")
        break
    prev_q = q