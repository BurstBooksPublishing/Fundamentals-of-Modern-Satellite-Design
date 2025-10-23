import numpy as np

# example LET (MeV*cm^2/mg) and differential flux (particles/cm2/s/(MeV*cm2/mg))
LET = np.linspace(0.1, 100, 1000)
flux = 1e-3 * np.exp(-LET/10.0)   # placeholder spectrum (replace with model)

# Weibull parameters from heavy-ion tests (fit to device)
L0 = 5.0     # threshold LET (MeV*cm2/mg)
sigma0 = 1e-4 # saturation cross-section (cm2/device)
W = 20.0     # width parameter
s = 2.0      # shape

# Weibull cross-section model
sigma = np.where(LET > L0, sigma0 * (1 - np.exp(-((LET - L0)/W)**s)), 0.0)

# integrate SEE rate per device (events/s)
R = np.trapz(flux * sigma, LET)
print("SEE rate (events/day):", R * 86400.0)  # scale to per-day