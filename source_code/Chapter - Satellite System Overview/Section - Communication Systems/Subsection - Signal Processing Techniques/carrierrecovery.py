# input: complex baseband samples `rx_samples`, preamble `preamble`, sr (sample rate)
import numpy as np
# coarse frequency estimate via cross-correlation on preamble
corr = np.fft.ifft(np.fft.fft(rx_samples[:len(preamble)]) * np.conj(np.fft.fft(preamble)))
peak_idx = np.argmax(np.abs(corr))
# estimate phase slope => coarse freq (rad/sample)
phase = np.angle(corr[peak_idx])
# convert to Hz
coarse_freq = phase / (2*np.pi) * sr / len(preamble)  # coarse estimate (Hz)
# apply coarse correction
t = np.arange(len(rx_samples))/sr
rx_coarse = rx_samples * np.exp(-1j*2*np.pi*coarse_freq*t)
# fine correction: simple PLL loop
pll_bw = 0.01  # normalized loop bandwidth
pll_phase = 0.0
pll_freq = 0.0
out = np.empty_like(rx_coarse, dtype=complex)
for n, s in enumerate(rx_coarse):
    # phase detector (decision-directed): rotate by current estimate
    s_rot = s * np.exp(-1j*pll_phase)
    err = np.angle(s_rot*np.conj(decision_maker(s_rot)))  # quick phase error
    pll_freq += pll_bw * err
    pll_phase += pll_freq + pll_bw*err
    out[n] = s_rot
# 'out' now has carrier-corrected symbols