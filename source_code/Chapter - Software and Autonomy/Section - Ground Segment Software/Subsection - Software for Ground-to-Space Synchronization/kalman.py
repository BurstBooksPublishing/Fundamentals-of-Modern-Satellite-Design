import numpy as np

# state x = [offset (s); freq_bias (s/s)]
def kalman_update(x,P,z,dt,Q,R):
    F = np.array([[1.0, dt],[0.0, 1.0]])        # state transition
    H = np.array([[1.0, 0.0]])                 # measurement matrix
    # Predict
    x = F @ x
    P = F @ P @ F.T + Q
    # Update with measurement z (two-way estimate of offset)
    y = z - (H @ x)                             # residual
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    x = x + K @ y
    P = (np.eye(2) - K @ H) @ P
    return x, P

# Example usage: iterate over measurements (z_i) with times dt_i