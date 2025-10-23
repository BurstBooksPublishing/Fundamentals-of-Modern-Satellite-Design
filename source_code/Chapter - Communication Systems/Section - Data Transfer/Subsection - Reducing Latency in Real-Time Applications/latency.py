import math
c = 3e8                       # speed of light (m/s)
d = 700e3                     # slant range (500-1000 km LEO example)
B = 50e6                      # useful bitrate after coding (50 Mbps)
hdr = 40*8                    # header size in bits (e.g., UDP/IP)
ber = 1e-5                    # bit error rate assumption
def loss_prob(S_bits):        # approximate packet loss from BER
    return 1 - (1 - ber)**S_bits
def expected_latency(S_bytes):
    S = S_bytes*8
    Lprop = d / c
    p = loss_prob(S)
    Ltrans_expected = (S / B) / (1 - p)  # eq. for retransmission
    Lproc = 0.010                          # 10 ms onboard processing
    Lqueue = 0.005                         # 5 ms expected queuing
    return Lprop + Ltrans_expected + Lproc + Lqueue
# sweep packet sizes
sizes = list(range(64, 1501, 64))
best = min(sizes, key=expected_latency)
print("Best packet size (bytes):", best)
for s in [128, 512, 1200]:
    print(s, "bytes ->", expected_latency(s), "s")
# Note: real implementation must include FEC overhead and actual BER model.