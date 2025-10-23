import math
# constants and scenario parameters (comments explain each)
c = 299792458.0                 # speed of light (m/s)
f = 14e9                        # uplink frequency (Hz), e.g., 14 GHz Ku-band
lambda_m = c / f
R = 3.6e7                       # slant range (m) approx GEO
Gt_dBi = 42.0                   # transmit antenna gain (dBi)
Gr_dBi = 52.0                   # receive antenna gain (dBi)
Tsys_dBK = 290.0                # system noise temp in Kelvin (K) expressed as dBK later
Rb = 50e6                       # bit rate (Hz)
EbN0_req_dB = 8.5               # required Eb/N0 in dB for chosen modulation/coding
margin_dB = 3.0                 # required system margin in dB
# convert gains and compute path loss
Gt = 10**(Gt_dBi/10.0)
Gr = 10**(Gr_dBi/10.0)
FSPL_dB = 20*math.log10(4*math.pi*R/lambda_m)
# compute receiver noise density N0 = k*Tsys (dBW/Hz)
k = 1.38064852e-23
Tsys = 250.0                    # actual system noise temp (K)
N0_dBWHz = 10*math.log10(k*Tsys)
# required Pr in dBW: Pr = Eb/N0 + N0 + 10log10(Rb)
Pr_req_dBW = EbN0_req_dB + N0_dBWHz + 10*math.log10(Rb) + margin_dB
# Pt required using gains and FSPL: Pt_dBW = Pr + FSPL - Gt_dBi - Gr_dBi
Pt_req_dBW = Pr_req_dBW + FSPL_dB - Gt_dBi - Gr_dBi
print("FSPL (dB):", round(FSPL_dB,2))
print("Required transmit power (dBW):", round(Pt_req_dBW,2))