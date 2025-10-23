import numpy as np

def k_out_of_n_reliability(R, n, k):  # compute eq:k_out_of_n
    from math import comb
    return sum(comb(n,i)*(R**i)*((1-R)**(n-i)) for i in range(k,n+1))

def residual_gate(z, H, x_pred, P_pred, Rz, alpha=0.01):
    r = z - H @ x_pred                       # innovation
    S = H @ P_pred @ H.T + Rz                # innovation cov
    gamma = float(r.T @ np.linalg.inv(S) @ r) # chi-square metric
    # chi2 threshold from approximation for 1 DOF or precomputed table
    threshold = -2*np.log(alpha)             # simple scalar approximation
    return gamma, gamma > threshold

# Example usage
R_sensor = 0.98
print(k_out_of_n_reliability(R_sensor, 3, 2)) # 2-of-3 reliability
# synthetic gating test (1D)
gamma, exceeded = residual_gate(np.array([0.5]), np.array([[1.]]),
                                np.array([0.0]), np.array([[0.1]]), np.array([[0.01]]))
# exceeded indicates outlier detection