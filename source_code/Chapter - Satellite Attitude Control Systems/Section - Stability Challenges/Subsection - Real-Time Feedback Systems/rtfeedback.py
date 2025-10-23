import numpy as np
# system matrices (discrete) -- precomputed on ground
Ad = np.eye(6)  # placeholder discrete A
Bd = np.zeros((6,3))  # placeholder B
Qk = np.diag([1e-6]*3 + [1e-4]*3)  # process noise cov
Rk = np.diag([1e-2]*3 + [1e-1]*3)  # measurement noise cov

# LQR gain (computed offline) and estimator covariance
K = np.zeros((3,6))  # control gain mapping state->torque
P = np.eye(6)*1e-3

def ekf_predict(x, P):
    x_pred = Ad @ x
    P_pred = Ad @ P @ Ad.T + Qk
    return x_pred, P_pred

def ekf_update(x_pred, P_pred, z, H):
    S = H @ P_pred @ H.T + Rk
    Kk = P_pred @ H.T @ np.linalg.inv(S)
    x_upd = x_pred + Kk @ (z - H @ x_pred)
    P_upd = (np.eye(len(P)) - Kk @ H) @ P_pred
    return x_upd, P_upd

def control_law(x_est):
    tau = -K @ x_est  # LQR command
    # anti-windup: saturation at wheel torque capability
    tau_sat = np.clip(tau, -0.1, 0.1)  # [N*m] limits
    return tau_sat

# main timestep (onboard loop)
x = np.zeros(6)  # state: [theta; omega]
H = np.eye(6)  # measurement matrix (example)
z = np.zeros(6)  # measurement vector from sensors
x_pred, P_pred = ekf_predict(x, P)
x, P = ekf_update(x_pred, P_pred, z, H)
tau_cmd = control_law(x)
# send tau_cmd to wheel driver; momentum management handled separately