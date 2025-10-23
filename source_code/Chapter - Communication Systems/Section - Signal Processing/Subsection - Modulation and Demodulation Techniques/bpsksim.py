import numpy as np
from scipy.special import erfc
# parameters
N=1000000                      # number of bits
EbN0_dB = np.arange(0,11,1)    # Eb/N0 range
bits = np.random.randint(0,2,N)
s = 2*bits-1                    # BPSK symbols +/-1
P_amp = 1.0                     # amplifier linear gain
clip_level = 0.8                # soft-limiter threshold (relative)
def soft_limiter(x,cl=clip_level):
    # simple saturation; models HPA compression
    return np.tanh(x/cl)*cl
bers=[]
for ebdb in EbN0_dB:
    EbN0 = 10**(ebdb/10)
    N0 = 1/EbN0
    noise = np.sqrt(N0/2)*np.random.randn(N)
    tx = s*P_amp
    tx_nl = soft_limiter(tx)     # apply nonlinearity
    rx = tx_nl + noise
    bits_hat = (rx>0).astype(int)
    ber = np.mean(bits_hat!=bits)
    bers.append(ber)
# theoretical BER for coherent BPSK (no nonlinearity) for reference
theoretical = 0.5*erfc(np.sqrt(10**(EbN0_dB/10)))
# print a few results (simple output)
for db,sim,th in zip(EbN0_dB,bers,theoretical):
    print(f"{db} dB: sim BER={sim:.3e}, theo={th:.3e}")