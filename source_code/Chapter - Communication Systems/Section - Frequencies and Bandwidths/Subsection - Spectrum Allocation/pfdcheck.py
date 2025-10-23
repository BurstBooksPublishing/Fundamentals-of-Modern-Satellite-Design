import math, numpy as np
k = 1.380649e-23             # Boltzmann constant
c = 299792458.0              # speed of light

# Mission parameters
data_rate = 100e6            # desired throughput (100 Mbps)
spectral_eff = 2.0           # bits/s/Hz (e.g., QPSK+coding)
freq = 12.5e9                # downlink centre freq (Hz, Ku band)
range_m = 36000e3            # GEO slant range (m)
G_rx_dBi = 40.0              # ground antenna gain (dBi)
T_sys = 500.0                # system noise temp (K)
margin_dB = 3.0              # required link margin (dB)

# Derived
bandwidth = data_rate / spectral_eff        # Hz
lambda_m = c / freq
# Required SNR from Shannon invert approx (assuming practical coding gap)
SNR_required_linear = 10**((10 + margin_dB)/10) # placeholder SNR linear
# Friis to get Pr from EIRP: Pr = EIRP * Gr * (lambda/(4*pi*R))^2
# Rearranged for EIRP required to reach SNR: EIRP = SNR * k*T*B / (Gr * lossp)
Gr_linear = 10**(G_rx_dBi/10)
loss_geom = (lambda_m/(4*math.pi*range_m))**2

noise_power = k * T_sys * bandwidth
EIRP_required_W = SNR_required_linear * noise_power / (Gr_linear * loss_geom)
EIRP_required_dBW = 10*math.log10(EIRP_required_W)

# Quick PFD at Earth's surface (approx): PFD = EIRP / (4*pi*R^2) per Hz if divided by B
PFD_Wm2Hz = EIRP_required_W / (4*math.pi*range_m**2) / bandwidth
print(f"Bandwidth: {bandwidth/1e6:.3f} MHz, EIRP: {EIRP_required_dBW:.1f} dBW, PFD: {PFD_Wm2Hz:.3e} W/m^2/Hz")