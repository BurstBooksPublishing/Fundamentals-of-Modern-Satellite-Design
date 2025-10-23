import numpy as np
from scipy.optimize import lsq_linear

# Inputs (example values) --------------------------------
tau_cmd = np.array([0.01, -0.02, 0.005])  # desired body torque (N·m)
B = np.array([2e-5, 1e-5, -3e-5])         # geomagnetic vector (T)
W = np.diag([1.0, 1.0, 1.0])              # weighting matrix
lambda_thr = 1e3                          # thruster penalty

# Build operator matrices --------------------------------
def A_of_B(B):                             # returns 3x3 cross-product matrix
    return np.array([[0, -B[2], B[1]],
                     [B[2], 0, -B[0]],
                     [-B[1], B[0], 0]])

A = A_of_B(B)
G = np.hstack([np.eye(3), A, np.eye(3)])   # 3x9 mapping

# Bounds: tau_rw, m, tau_thr
u_min = np.r_[ -0.1*np.ones(3), -0.2*np.ones(3), -0.05*np.ones(3)]
u_max = np.r_[  0.1*np.ones(3),  0.2*np.ones(3),  0.05*np.ones(3)]

# Weighted least squares solve (expanded to include thruster penalty)
Wsqrt = np.sqrt(W)
A_aug = np.vstack([Wsqrt @ G, np.sqrt(lambda_thr) * np.hstack([np.zeros((3,6)), np.eye(3)])])
b_aug = np.r_[Wsqrt @ tau_cmd, np.zeros(3)]

res = lsq_linear(A_aug, b_aug, bounds=(u_min, u_max), lsmr_tol='auto', verbose=0)
u = res.x  # allocated [tau_rw, m, tau_thr]
# u[0:3] -> reaction-wheel torques, u[3:6] -> magnetorquer dipoles, u[6:9] -> thruster torques