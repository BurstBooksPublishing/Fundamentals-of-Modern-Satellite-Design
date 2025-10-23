import numpy as np

# state x = [delta_theta(3), bias(3), scale(3)]
x = np.zeros(9)
P = np.eye(9)*1e-3

def predict(x, P, omega_m, dt, Q):
    # apply inverse scale correction to get nominal omega
    scale = x[6:9]  # per-axis scale factors
    bias = x[3:6]
    omega_hat = (omega_m - bias) / (1.0 + scale)
    # propagate attitude error (small-angle approx)
    A = np.block([
        [np.eye(3) - dt*skew(omega_hat),  -dt*np.eye(3),  np.zeros((3,3))],
        [np.zeros((6,3)), np.eye(6)]
    ])
    x[:3] += -dt * np.cross(omega_hat, x[:3])  # kinematic approx
    # bias and scale treated as random walk
    P = A @ P @ A.T + Q
    return x, P

def update(x, P, q_star, R):
    # compute residual between star-tracker quaternion and integrated attitude
    y = attitude_error_vector(q_star, x[:3])  # small-angle residual
    H = np.zeros((3,9)); H[:3,:3] = np.eye(3)  # measurement jacobian wrt att. err.
    K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
    x = x + K @ y
    P = (np.eye(9) - K @ H) @ P
    return x, P

# helper functions: skew, attitude_error_vector defined elsewhere