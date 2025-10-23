import numpy as np

# Example PSD: frequencies (Hz) and PSD values (g^2/Hz)
f = np.array([20, 50, 100, 200, 400])          # Hz
S = np.array([0.01, 0.02, 0.015, 0.005, 0.001])# g^2/Hz

# Integrate PSD to get a_rms (use trapezoidal rule)
a_rms = np.sqrt(np.trapz(S, f))
print("a_rms = {:.3f} g".format(a_rms))

# SDOF transmissibility for displacement base-excitation
def displacement_transmissibility(f_q, f_n, zeta):
    r = f_q / f_n
    num = r**2
    den = np.sqrt((1 - r**2)**2 + (2*zeta*r)**2)
    return num / den

# Example component: natural frequency 80 Hz, damping 2%
f_n = 80.0
zeta = 0.02
for fq in [20, 50, 100, 200]:
    T = displacement_transmissibility(fq, f_n, zeta)
    print("Freq {:3.0f} Hz -> disp trans = {:.3f}".format(fq, T))