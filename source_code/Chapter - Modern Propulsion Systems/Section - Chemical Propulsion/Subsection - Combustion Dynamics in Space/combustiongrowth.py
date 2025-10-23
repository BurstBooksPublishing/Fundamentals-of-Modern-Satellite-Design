import numpy as np

# parameters (engine-specific) -- adjust per mission
f_mode = 500.0            # mode frequency Hz
omega = 2*np.pi*f_mode
tau_c = 0.002             # combustion time constant s
K = 0.8                   # coupling gain (dimensionless)
omega_n = omega           # assume acoustic mode at omega

# transfer function G(iw) = K/(1 + i w tau_c)
G = K/(1 + 1j*omega_n*tau_c)
# acoustic damping factor (negative real part stabilizes)
Q_acoustic = 0.01         # acoustic dissipation (1/s)
# growth rate sigma = Re{G} - Q_acoustic (simplified)
sigma = np.real(G) - Q_acoustic

print("Mode freq (Hz):", f_mode)
print("Transfer fn real part:", np.real(G))
print("Estimated growth rate (1/s):", sigma)