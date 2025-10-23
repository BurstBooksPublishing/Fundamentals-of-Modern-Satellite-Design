import math
# Given mission parameters (example values)
lam = 0.01              # wavelength, m (Ka-band ~1 cm)
gain_loss_db = 0.5      # allowed gain loss, dB
f_ctrl = 0.2            # control loop crossover, Hz
k = 8                   # margin factor: f1 >= k * f_ctrl
L = 4.0                 # boom length, m
rho = 1600.0            # density kg/m^3 for CFRP approximate
A = 0.003               # cross-section area m^2 (tube/boom)
beta1 = 1.875

# Ruze: solve for epsilon_rms that gives allowed gain loss
G_rel = 10**(-gain_loss_db/10)
eps_rms = (lam/(4*math.pi)) * math.sqrt(-math.log(G_rel))  # m

# Required first natural frequency
f1_req = k * f_ctrl  # Hz

# Solve Eq. (cantilever) for EI
omega1 = 2*math.pi*f1_req
EI = ( (omega1 * L**2) / (beta1**2) )**2 * (rho * A)  # N*m^2

print(f"eps_rms = {eps_rms*1e6:.1f} micron")
print(f"Required f1 = {f1_req:.3f} Hz, Required EI = {EI:.3e} N*m^2")