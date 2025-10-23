import numpy as np

# small helper functions (omitted error checks for brevity)
def quat_mul(q1,q2):  # quaternion multiply
    w1,x1,y1,z1 = q1; w2,x2,y2,z2 = q2
    return np.array([w1*w2 - x1*x2 - y1*y2 - z1*z2,
                     w1*x2 + x1*w2 + y1*z2 - z1*y2,
                     w1*y2 - x1*z2 + y1*w2 + z1*x2,
                     w1*z2 + x1*y2 - y1*x2 + z1*w2])

def omega_matrix(w):
    wx,wy,wz = w
    return np.array([[0,-wx,-wy,-wz],
                     [wx,0,wz,-wy],
                     [wy,-wz,0,wx],
                     [wz,wy,-wx,0]])

def skew(v):
    x,y,z = v
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0]])

# state: q (4,), bias b (3,), P covariance (6x6)
def propagate(q,b,P,gyro_meas,dt,Q):
    # remove bias then integrate quaternion
    w = gyro_meas - b
    dq = np.concatenate(([1.0], 0.5*w*dt))  # first-order approx
    q = quat_mul(q, dq); q = q/np.linalg.norm(q)
    # state transition for small-angle error
    F = np.block([[np.eye(3) - skew(w)*dt, -np.eye(3)*dt],
                  [np.zeros((3,3)), np.eye(3)]])
    P = F @ P @ F.T + Q
    return q,b,P

def star_update(q,b,P,star_body,star_inertial,R):
    # predict star in body frame
    C = quat_to_rotmat(q)  # implementation omitted for brevity
    pred = C @ star_inertial
    # linearize: H maps small angle error to measurement residual
    H = np.hstack((skew(pred), np.zeros((3,3))))
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    y = star_body - pred
    dx = K @ y
    # apply corrections
    delta_theta = dx[:3]
    db = dx[3:]
    q = quat_mul(q, small_angle_quat(delta_theta))
    q = q/np.linalg.norm(q)
    b = b + db
    P = (np.eye(6) - K @ H) @ P
    return q,b,P

# Note: fill in Q, R, initial conditions, and measurement loop in flight code.