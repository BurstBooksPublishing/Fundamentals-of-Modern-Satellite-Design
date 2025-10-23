import numpy as np

MU = 398600.4418  # Earth mu, km^3/s^2

def kepler_E(M, e, tol=1e-10, maxiter=50):
    # Newton-Raphson solve for eccentric anomaly E
    E = M if e < 0.8 else np.pi
    for _ in range(maxiter):
        f = E - e*np.sin(E) - M
        fp = 1 - e*np.cos(E)
        dE = -f/fp
        E += dE
        if abs(dE) < tol:
            break
    return E

def elts_to_eci(a, e, i, raan, argp, M0, dt):
    # a: km, e: -, i, raan, argp: rad, M0: rad, dt: s since epoch
    n = np.sqrt(MU / a**3)
    M = M0 + n * dt
    E = kepler_E(M % (2*np.pi), e)
    # compute r in orbital plane
    nu = 2*np.arctan2(np.sqrt(1+e)*np.sin(E/2),
                      np.sqrt(1-e)*np.cos(E/2))
    r_p = a*(1 - e*np.cos(E))
    # position in PQW frame
    r_perifocal = np.array([r_p*np.cos(nu), r_p*np.sin(nu), 0.0])
    # rotation PQW -> ECI via RAAN, incl, argp
    Rz_raan = rotation_matrix_z(raan)
    Rx_i = rotation_matrix_x(i)
    Rz_argp = rotation_matrix_z(argp)
    Q_pX = Rz_raan @ Rx_i @ Rz_argp
    r_eci = Q_pX @ r_perifocal
    return r_eci

# Minimal rotation functions (implementations omitted for brevity).