import math
# Inputs (example values for a GEO Ka-band reflector)
freq = 30e9               # Hz (Ka band uplink)
c = 3e8
lam = c / freq
A = math.pi*(2.5)**2      # m^2 (5 m diameter)
eta_other = 0.6           # other efficiency factors
allow_loss_db = 1.0       # allowable Ruze loss in dB

# compute required Ruze efficiency for 1 dB loss
eta_ruze_req = 10**(-allow_loss_db/10.0)
# solve for sigma from Ruze: eta_ruze = exp[-(4*pi*sigma/lambda)^2]
sigma_req = (lam/(4*math.pi))*math.sqrt(-math.log(eta_ruze_req))

# Gain with required sigma
eta_total = eta_other * eta_ruze_req
G = eta_total * (4*math.pi*A)/(lam**2)
G_dBi = 10*math.log10(G)

# Attitude impulse example: impulse torque*time -> angular momentum
delta_H = 5.0             # N*m*s (example)
I = 120.0                 # kg*m^2 (spacecraft)
delta_omega = delta_H / I # rad/s

print(f"lambda={lam:.3e} m, required sigma={sigma_req*1e3:.2f} mm")
print(f"Gain={G_dBi:.2f} dBi, delta_omega={delta_omega:.4f} rad/s")
# Small printed comments are inline to explain outputs.