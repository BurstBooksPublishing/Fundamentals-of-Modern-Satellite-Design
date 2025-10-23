import numpy as np

def dark_correct(frame, dark_frame):  # subtract stored dark frame
    return frame.astype(np.float32) - dark_frame

def kalman_update(x, P, z, F, H, Q, R):  # simple scalar Kalman for demo
    # predict
    x_pr = F*x
    P_pr = F*P*F + Q
    # update
    K = P_pr * H / (H*P_pr*H + R)
    x_up = x_pr + K*(z - H*x_pr)
    P_up = (1 - K*H)*P_pr
    return x_up, P_up

# example usage: stream of DN values
dark = np.load('dark_frame.npy')  # pre-calibrated dark frame (flight file)
F, H, Q, R = 1.0, 1.0, 1e-4, 1e-2
x, P = 0.0, 1.0  # initial bias estimate

for raw_frame in stream_of_frames():           # generator of frames
    corr = dark_correct(raw_frame, dark)       # dark subtraction
    mean_dn = corr.mean()                      # collapse to scalar telemetry
    x, P = kalman_update(x, P, mean_dn, F, H, Q, R)  # smooth bias/level
    send_downlink(corr - x)                    # send bias-corrected data