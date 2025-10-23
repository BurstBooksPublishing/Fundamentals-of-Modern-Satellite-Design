import numpy as np

def fdi_check(y, C, x_hat, P, R, gamma):
    # y: measurement vector (m,)
    # C: measurement matrix (m,n)
    # x_hat: state estimate (n,)
    # P: state error covariance (n,n)
    # R: measurement noise covariance (m,m)
    # gamma: detection threshold (scalar)
    r = y - C.dot(x_hat)                 # residual vector
    S = C.dot(P).dot(C.T) + R           # residual covariance
    try:
        Sinv = np.linalg.inv(S)
    except np.linalg.LinAlgError:
        Sinv = np.linalg.pinv(S)        # robust inverse on-board
    J = float(r.T.dot(Sinv).dot(r))     # detection statistic
    alarm = (J > gamma)
    # isolation: normalized residual magnitudes
    diagS = np.sqrt(np.maximum(np.diag(S), 1e-12))
    z = np.abs(r) / diagS
    iso_rank = np.argsort(-z)           # indices sorted by suspicion
    return {'J': J, 'alarm': alarm, 'z': z, 'iso_rank': iso_rank}

# Example usage: invoked inside control loop with KF outputs.