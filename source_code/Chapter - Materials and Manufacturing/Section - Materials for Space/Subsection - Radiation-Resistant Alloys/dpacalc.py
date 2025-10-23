import numpy as np

def compute_dpa(flux, sigma_d, time_s):
    # flux: particles per cm^2 per s
    # sigma_d: displacement cross-section per atom (cm^2)
    # time_s: mission duration in seconds
    return flux * sigma_d * time_s  # dpa (dimensionless)

# Example: proton flux 1e8 cm^-2 s^-1, sigma_d 1e-24 cm^2, 5-year mission
flux = 1e8
sigma_d = 1e-24
time_s = 5 * 365.25 * 24 * 3600
dpa = compute_dpa(flux, sigma_d, time_s)
print("Estimated dpa:", dpa)  # engineer uses this to compare to thresholds