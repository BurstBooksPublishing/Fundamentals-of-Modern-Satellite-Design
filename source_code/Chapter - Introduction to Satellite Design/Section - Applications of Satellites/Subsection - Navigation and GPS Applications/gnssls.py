import numpy as np

def gnss_position(p_ranges, sat_pos, weights=None):
    # p_ranges: measured pseudoranges (m) shape (n,)
    # sat_pos: GNSS satellite positions ECEF shape (n,3)
    n = p_ranges.size
    if weights is None:
        W = np.eye(n)  # equal weights
    else:
        W = np.diag(weights)
    # initial guess: center of Earth + small altitude
    x = np.array([0.0, 0.0, 6371000.0, 0.0])  # [x,y,z,clock_bias]
    for _ in range(10):
        H = np.zeros((n,4))
        y = np.zeros(n)
        for i in range(n):
            rho_pred = np.linalg.norm(x[:3]-sat_pos[i]) + x[3]
            # geometry row
            H[i,0:3] = (x[:3]-sat_pos[i]) / np.linalg.norm(x[:3]-sat_pos[i])
            H[i,3] = 1.0
            y[i] = p_ranges[i] - rho_pred
        # weighted least squares update
        delta = np.linalg.inv(H.T @ W @ H) @ (H.T @ W @ y)
        x += delta
        if np.linalg.norm(delta) < 1e-4:  # convergence threshold (meters)
            break
    return x  # returns [x,y,z,clock_bias]

# Example usage with synthetic data (not shown here).