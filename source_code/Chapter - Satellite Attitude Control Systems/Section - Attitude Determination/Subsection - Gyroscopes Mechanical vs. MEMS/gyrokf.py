import numpy as np

# state: bias estimate (rad/s)
bias = 0.0
P = 1e-6            # state covariance
Q = 1e-9            # bias random walk variance per sec
R = (np.deg2rad(0.01))**2  # star-tracker angle variance (rad^2)

dt = 0.01           # gyro sample time (s)
def propagate(bias,P,dt):
    P = P + Q*dt    # bias random walk
    return bias,P

def update_with_star(bias,P,delta_theta_star):
    # measurement: delta_theta_star ≈ (omega_meas - bias)*dt
    H = -dt
    S = H*P*H + R
    K = P*H / S
    # correct bias with measurement residual
    bias = bias + K*(delta_theta_star - (-H*bias))
    P = (1 - K*H)*P
    return bias,P

# loop: high-rate gyro then occasional star update
for t in np.arange(0,600,dt):
    omega_meas = measure_gyro()                # placeholder
    bias,P = propagate(bias,P,dt)
    theta_propagated += (omega_meas - bias)*dt
    if star_update_available():
        delta_theta_star = get_star_delta()    # measured rotation since last star fix
        bias,P = update_with_star(bias,P,delta_theta_star)
# final bias used in attitude propagation