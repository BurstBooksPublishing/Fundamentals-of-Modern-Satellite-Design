import math

# Inputs: BOL power (W), mission years, fluence (MeV/cm2 per year), cycles per year
P0 = 1000.0              # beginning-of-life array power (W)
years = 15               # mission lifetime (years)
fluence_per_year = 1e10  # proton fluence (MeV/cm2/yr) - orbit dependent
cycles_per_year = 365    # eclipse cycles per year - LEO vs GEO differ

# Empirical damage coefficients (calibrated by test)
k_DDD = 5e-12   # fractional power loss per fluence (per MeV/cm2)
k_cycle = 3e-5  # fractional loss per thermal cycle

# Compute cumulative degradation
total_fluence = fluence_per_year * years
alpha_rad = k_DDD * total_fluence / years     # convert to per-year equivalent
alpha_cycle = k_cycle * cycles_per_year       # per-year equivalent
alpha_tot = alpha_rad + alpha_cycle

# EOL power fraction using exponential approximation
EOL_fraction = math.exp(-alpha_tot * years)
P_EOL = P0 * EOL_fraction

print(f"EOL fraction: {EOL_fraction:.3f}  EOL power: {P_EOL:.1f} W")
# Inline comments provide calibration guidance.