import math

# Constants
k = 1.38064852e-23           # Boltzmann constant
T = 290.0                    # reference temp in K
B = 25e3                     # bandwidth Hz (25 kHz telemetry)
Pt_dBW = 10*math.log10(1.0)  # 1 W transmit in dBW
Gt_dBi = 0.0                 # small deployable antenna
Gr_dBi = 2.0                 # small receive antenna
Lpath_dB = 120.0             # path loss dB (use free-space calc in practice)
Lmisc_dB = 2.0               # connector and polarization loss

# Received power (Eq. 1)
Pr_dBW = Pt_dBW + Gt_dBi + Gr_dBi - Lpath_dB - Lmisc_dB

# Noise floor
noise_dBW = 10*math.log10(k*T) + 10*math.log10(B)

# Required SNR (example: BPSK with coding ~ needed Eb/N0 7 dB, data rate=bandwidth)
EbN0_req = 7.0               # dB
Rb = B                       # assume symbol rate ~= B
SNR_req = EbN0_req + 10*math.log10(Rb/B)

# Required NF (Eq. 3)
NF_req_dB = Pr_dBW - noise_dBW - SNR_req

# Candidate LNAs (NF dB, gain dB, power mW)
candidates = [
    ("SiGe_LNA", 1.2, 18.0, 80),
    ("CMOS_LNA", 2.5, 15.0, 25),
    ("pHEMT_LNA", 0.6, 20.0, 120),
]

print("Pr (dBW):", round(Pr_dBW,3), "Noise (dBW):", round(noise_dBW,3))
print("Required system NF (dB):", round(NF_req_dB,3))
for name, nf, g, p in candidates:
    meets = "OK" if nf <= NF_req_dB else "NO"
    print(f"{name}: NF={nf} dB, Gain={g} dB, Power={p} mW -> {meets}")
# Use this output to trade-off NF vs power and radiation hardness.