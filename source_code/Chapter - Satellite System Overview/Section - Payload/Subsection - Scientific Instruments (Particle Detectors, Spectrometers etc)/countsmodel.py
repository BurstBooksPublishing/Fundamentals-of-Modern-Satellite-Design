import numpy as np
# input flux J(E) at mean energy (particles/cm2/s/sr/keV)
J = 1e3          # example flux
G = 1e-2         # geometric factor (cm2 sr)
DeltaE = 1.0     # energy bin (keV)
eff = 0.7        # detection efficiency
tau = 1e-4       # dead time (s)
t_int = 1.0      # integration time (s)

# expected observed counts before dead time
R_obs = G * J * DeltaE * eff
N_obs = R_obs * t_int
# dead time correction (non-paralyzable)
R_true = R_obs / (1 - tau * R_obs) if tau * R_obs < 1 else np.inf
N_true = R_true * t_int
# add Poisson noise
N_meas = np.random.poisson(N_true)
print("# Observed counts:", N_obs, " Corrected counts:", N_true, " Measured:", N_meas)