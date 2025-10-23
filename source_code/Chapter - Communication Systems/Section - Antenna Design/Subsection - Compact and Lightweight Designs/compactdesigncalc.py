import math

# Mission parameters (example for Ka- and X-band)
freq_Hz = 30e9        # Ka-band example
c = 299792458.0
lam = c/freq_Hz
gain_dBi = 30.0       # required antenna gain
gain = 10**(gain_dBi/10.0)
eta = 0.6             # aperture efficiency
areal_density = 0.5   # kg/m^2 (select from ranges above)

# compute diameter from eqn (2)
D = lam/math.pi * math.sqrt(gain/eta)   # meters
area = math.pi*(D/2.0)**2
mass = areal_density * area

# compute surface RMS for 90% surface efficiency using Ruze inversion
target_eff_surface = 0.9
sigma_max = (lam/(4*math.pi))*math.sqrt(-math.log(target_eff_surface))

print(f"freq={freq_Hz/1e9:.1f} GHz, lambda={lam*1e3:.2f} mm")
print(f"D={D*1000:.1f} mm, area={area:.4f} m2, mass={mass:.3f} kg")
print(f"max RMS for 90% surface efficiency: {sigma_max*1e3:.2f} mm")
# inline comments: change freq_Hz and areal_density for other trades