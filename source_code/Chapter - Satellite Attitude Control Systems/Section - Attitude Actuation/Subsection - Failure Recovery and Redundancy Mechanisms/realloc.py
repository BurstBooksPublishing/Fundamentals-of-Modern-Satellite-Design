import numpy as np

# Inputs: B (effectiveness), tau_des (desired body torque), mask (1=healthy,0=failed)
# u_nom initial guess, u_min/u_max actuator bounds
def reallocate(B, tau_des, mask, u_nom, u_min, u_max):
    B_eff = B[:, mask==1]               # remove failed actuator columns
    # unconstrained least squares solution
    u_eff, residuals, _, _ = np.linalg.lstsq(B_eff, tau_des, rcond=None)
    # map back to full command vector
    u = np.zeros(B.shape[1])
    u[mask==1] = u_eff
    # enforce bounds
    u = np.minimum(np.maximum(u, u_min), u_max)
    return u  # returns safe actuator commands

# Example usage would include validation of residual magnitude and fallback to thrusters.