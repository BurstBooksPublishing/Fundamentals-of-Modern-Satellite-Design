import numpy as np
from scipy.stats import chi2

# incremental state (persist across windows)
mean = np.zeros(n)         # current mean vector
cov = np.eye(n)            # current covariance matrix
count = 0                  # sample count

def update_stats(x):
    global mean, cov, count
    count += 1
    # incremental mean update (Welford)
    delta = x - mean
    mean += delta / count
    # update covariance estimator (unnormalized)
    if count == 1:
        M2 = np.zeros((n,n))
    else:
        # outer product update for sample covariance
        M2 = cov * (count-1)  # recover sum of squares
        M2 += np.outer(delta, delta) * (count-1)/count
    cov = M2 / max(1, count-1)  # sample covariance

def mahalanobis_sq(x):
    # regularize covariance for numerical stability
    cov_reg = cov + 1e-6*np.eye(len(x))
    d = x - mean
    return float(d @ np.linalg.inv(cov_reg) @ d)

def is_anomaly(x, alpha=1e-3):
    update_stats(x)                       # update model online
    D2 = mahalanobis_sq(x)
    threshold = chi2.ppf(1-alpha, df=len(x))
    return D2 > threshold                 # True => anomaly