import numpy as np
# M: measured voltages shape (M, K)
# A: steering vectors shape (M, K) (a_i(theta_k))
# s: calibration tones shape (K,) complex
# returns g_hat shape (M,)
def estimate_g(M, A, s):
    # numerator: sum_k conj(s_k)*conj(a_ik)*m_ik
    num = np.sum(np.conj(s) * np.conj(A) * M, axis=1)
    # denominator: sum_k |s_k|^2 * |a_ik|^2
    den = np.sum(np.abs(s)**2 * np.abs(A)**2, axis=1)
    # avoid divide-by-zero with small epsilon
    eps = 1e-12
    return num / (den + eps)
# Example usage:
# g_hat = estimate_g(M_meas, A_steer, s_tones)