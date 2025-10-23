import numpy as np
from scipy.stats import chi2

# r: residual vector; S: innovation covariance; persist_count: required consecutive alarms
def mahalanobis_alarm(r, S, alpha=1e-3, persist_count=3, state=None):
    # state holds past alarms count
    if state is None:
        state = {'count':0}
    # compute D^2
    try:
        Sinv = np.linalg.inv(S)              # replace with Cholesky on flight
    except np.linalg.LinAlgError:
        return False, state                  # covariance singular -> ignore or flag
    D2 = float(r.T @ Sinv @ r)
    m = r.size
    threshold = chi2.ppf(1-alpha, m)        # offline compute table for flight
    if D2 > threshold:
        state['count'] += 1
    else:
        state['count'] = 0
    alarm = (state['count'] >= persist_count)
    return alarm, state

# usage example: called each monitoring step with new residual and S