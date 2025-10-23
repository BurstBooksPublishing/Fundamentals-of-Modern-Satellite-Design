# Simple throughput calculator for stack design (LEO/GEO/deep-space).
import math

def shannon_capacity(B, snr):
    return B * math.log2(1 + snr)  # bits per second theoretical

def app_throughput(B, snr, code_rate, overhead):
    C = shannon_capacity(B, snr)
    return C * code_rate * (1 - overhead)  # effective app throughput

# Example scenarios (Hz, linear SNR, code rate, protocol overhead)
scenarios = {
    "LEO_EO": (200e6, 10.0, 0.75, 0.12),      # high bandwidth, moderate SNR
    "GEO_Comm": (50e6, 20.0, 0.9, 0.08),     # continuous service, high SNR
    "Deep_Space": (5e6, 2.0, 0.5, 0.20)      # constrained BW, low SNR
}
for name, params in scenarios.items():
    B, snr, r, o = params
    R = app_throughput(B, snr, r, o)
    print(f"{name}: {R/1e6:.2f} Mbps")  # quick mission-level metric