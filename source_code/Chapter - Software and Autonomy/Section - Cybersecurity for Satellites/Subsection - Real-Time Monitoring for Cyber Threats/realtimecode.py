import numpy as np
# simple Kalman residual chi-square + CUSUM on scalar feature
# y: measurement vector; x_hat, P: estimator state and cov
def chi2_stat(y, H, x_hat, P, R):
    r = y - H.dot(x_hat)             # residual
    S = H.dot(P).dot(H.T) + R        # residual covariance
    return float(r.T.dot(np.linalg.inv(S)).dot(r))

# CUSUM update on log-likelihood ratio for scalar feature z
def cusum_update(S_prev, z, mu0, mu1, sigma2, h):
    # Gaussian log-likelihood ratio
    llr = ((z-mu0)**2 - (z-mu1)**2) / (2*sigma2)
    S = max(0.0, S_prev + llr)
    alarm = S > h
    return S, alarm

# example loop processing telemetry stream (pseudo-async)
S = 0.0
h = 10.0                             # design threshold
for packet in telemetry_stream():    # blocking call to receive telemetry
    y = packet.measurements
    z = packet.scalar_feature         # e.g., power draw delta
    chi2 = chi2_stat(y, H, x_hat, P, R)
    if chi2 > tau_chi2:              # precomputed threshold
        send_signed_alarm("chi2", chi2)  # minimal, authenticated alert
    S, alarm = cusum_update(S, z, mu0, mu1, sigma2, h)
    if alarm:
        send_signed_alarm("cusum", S)
    # update estimator as usual (omitted)