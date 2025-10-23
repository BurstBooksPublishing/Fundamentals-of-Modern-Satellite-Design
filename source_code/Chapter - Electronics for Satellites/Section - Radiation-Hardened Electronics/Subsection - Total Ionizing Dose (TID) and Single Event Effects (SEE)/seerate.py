import numpy as np

# Weibull parameters (example device) # σ in cm^2, LET in MeV·cm^2/mg
sigma_sat = 1e-5
LET0 = 2.0
W = 10.0
s = 1.5

# binned LET spectrum: centers (MeV·cm^2/mg) and flux (particles/cm^2/s per bin)
let_centers = np.array([0.5, 2.0, 5.0, 10.0, 20.0])
flux = np.array([1e2, 5.0, 0.5, 1e-2, 1e-3])  # example numbers

def weibull_sigma(LET):
    # returns cross-section per device for given LET
    x = np.maximum(0.0, (LET - LET0) / W)
    return sigma_sat * (1.0 - np.exp(-x**s))

# discrete sum approximation of eq. (1)
sigma_vals = weibull_sigma(let_centers)
rate_per_bin = sigma_vals * flux  # upsets per device per second per bin
R_total = np.sum(rate_per_bin)

print(f"Estimated SEU rate/device: {R_total:.3e} 1/s")