import numpy as np

def triad(s_b, e_b, s_i, e_i):
    # normalize vectors (body and inertial)
    t1_b = s_b / np.linalg.norm(s_b)
    t1_i = s_i / np.linalg.norm(s_i)
    v_b = np.cross(s_b, e_b)
    v_i = np.cross(s_i, e_i)
    t2_b = v_b / np.linalg.norm(v_b)         # orthogonal to t1_b
    t2_i = v_i / np.linalg.norm(v_i)
    t3_b = np.cross(t1_b, t2_b)
    t3_i = np.cross(t1_i, t2_i)
    R = np.column_stack((t1_b, t2_b, t3_b)) @ np.column_stack((t1_i, t2_i, t3_i)).T
    return R  # body-to-inertial rotation matrix
# Usage: R = triad(sun_body, earth_body, sun_inertial, earth_inertial)