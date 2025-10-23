import numpy as np
from scipy.special import erfc
# Q-function
Q = lambda x: 0.5*erfc(x/np.sqrt(2))

def ber_qpsk(EbN0_dB):
    # coherent QPSK ~= BPSK
    EbN0 = 10**(EbN0_dB/10)
    return Q(np.sqrt(2*EbN0))

def ber_mpsk_approx(EbN0_dB, M):
    EbN0 = 10**(EbN0_dB/10)
    EsN0 = EbN0 * np.log2(M)
    arg = np.sqrt(2*EsN0)*np.sin(np.pi/M)
    Ps = 2*Q(arg)           # symbol error approx
    return Ps/np.log2(M)   # crude bit-error approx

snr = np.linspace(0,20,41)
ber_q = np.array([ber_qpsk(x) for x in snr])
ber_8 = np.array([ber_mpsk_approx(x,8) for x in snr])

# print sample values for system budget table
for s,bq,b8 in zip(snr[::10], ber_q[::10], ber_8[::10]):
    print(f"SNR {s:3.0f} dB: QPSK BER {bq:.2e}, 8PSK BER {b8:.2e}")