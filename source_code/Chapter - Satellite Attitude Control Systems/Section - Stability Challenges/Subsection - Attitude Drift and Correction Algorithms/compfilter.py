# q: current quaternion (4,), b: gyro bias (3,), dt: timestep
def update(q, b, omega_meas, star_q=None, dt=0.01, alpha=0.98):
    omega = omega_meas - b                           # bias-corrected rate
    dq = quat_from_omega(omega, dt)                  # integrate small rotation
    q_prop = quat_normalize(quat_mul(q, dq))         # propagate attitude
    if star_q is None:
        return q_prop, b                             # no absolute update
    # compute error quaternion: q_err = star_q * q_prop^{-1}
    q_err = quat_mul(star_q, quat_conj(q_prop))
    e_vec = q_err[0:3]                               # vector part ~ axis*sin(theta/2)
    # complementary fusion and simple bias update
    q_new = quat_normalize(quat_slerp(q_prop, star_q, 1-alpha))
    b += -0.01 * e_vec                               # bias correction gain
    return q_new, b
# Helper functions assumed: quat_from_omega, quat_mul, quat_conj, quat_slerp, quat_normalize