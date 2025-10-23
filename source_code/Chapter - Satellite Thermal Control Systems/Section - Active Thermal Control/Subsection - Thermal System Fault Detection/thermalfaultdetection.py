import numpy as np
# model matrices (prototype values)
A = np.array([[0.99,0.01],[0.0,0.98]])  # state transition
B = np.array([[0.1],[0.0]])            # heater coupling
C = np.eye(2)                          # direct temp sensors
Q = np.diag([1e-5,1e-5])               # process noise cov
R = np.diag([1e-3,1e-3])               # measurement noise cov

# Kalman init
x_hat = np.zeros((2,1))
P = np.eye(2)*1e-2

def kalman_step(u,y):
    global x_hat,P
    # predict
    x_pred = A @ x_hat + B*u
    P_pred = A @ P @ A.T + Q
    # update
    S = C @ P_pred @ C.T + R
    K = P_pred @ C.T @ np.linalg.inv(S)
    r = y - C @ x_pred                  # residual
    x_hat = x_pred + K @ r
    P = (np.eye(2)-K@C) @ P_pred
    return r.flatten(), S

# CUSUM parameters for step detection
h = 5.0          # threshold
k0 = 0.5         # reference value
g_pos = 0.0      # cumulative sum positive
g_neg = 0.0

def cusum_update(r_scalar):
    global g_pos,g_neg
    g_pos = max(0.0, g_pos + r_scalar - k0)
    g_neg = min(0.0, g_neg + r_scalar + k0)
    if g_pos > h or -g_neg > h:
        return True
    return False

# usage: loop reading u (heater) and y (temps), call kalman_step and cusum_update