import math
# Inputs (example LEO X-band)
f = 8.4e9            # Hz
c = 3e8              # m/s
lam = c / f
R = 1.2e6            # slant range, m (1200 km)
Pt_dBW = 10.0        # transmit power, dBW (~10 W)
Gt_dBi = 12.0        # satellite TX antenna gain, dBi
Gr_dBi = 45.0        # ground RX antenna gain, dBi (3m dish)
Tsys = 150.0         # system temp, K (ground Rx)
Rb = 50e6            # bit rate, bps (50 Mbps)
k_dBW = -228.6       # Boltzmann constant in dBW/K/Hz

Lfs_dB = 20*math.log10(4*math.pi*R/lam)        # free-space loss
Pr_dBW = Pt_dBW + Gt_dBi + Gr_dBi - Lfs_dB    # received power
N0_dBWHz = k_dBW + 10*math.log10(Tsys)        # noise density
EbN0_dB = Pr_dBW - (N0_dBWHz + 10*math.log10(Rb))

print(f"Lfs = {Lfs_dB:.1f} dB, Pr = {Pr_dBW:.2f} dBW, Eb/N0 = {EbN0_dB:.1f} dB")
# Use result to judge modulation and coding choices.