import numpy as np
mu = 3.986004418e14        # Earth mu, m^3/s^2
Re = 6378137.0             # Earth radius, m
J2 = 1.08262668e-3         # J2 coefficient

def acc_j2(r):             # J2 acceleration
    x,y,z = r
    r2 = np.dot(r,r)
    r5 = r2**2.5
    z2 = z*z
    factor = -1.5*J2*mu*(Re**2)/r5
    common = 1 - 5*z2/r2
    ax = factor * x * common
    ay = factor * y * common
    az = factor * z * (3 - 5*z2/r2)
    return np.array([ax,ay,az])

def acc_drag(r,v,A_over_m,Cd,rho0=1e-12,H=8000.0):
    alt = np.linalg.norm(r) - Re
    rho = rho0 * np.exp(-alt/H)    # crude exponential model
    v_rel = v                        # assume atmosphere co-rot negligible
    vnorm = np.linalg.norm(v_rel)
    if vnorm == 0: return np.zeros(3)
    drag = -0.5 * Cd * A_over_m * rho * vnorm * v_rel
    return drag

def dynamics(t,state,params):
    r = state[0:3]; v = state[3:6]
    a_grav = -mu * r / np.linalg.norm(r)**3
    a_j2 = acc_j2(r)
    a_drag = acc_drag(r,v,params['A_m'],params['Cd'])
    a_total = a_grav + a_j2 + a_drag + params.get('a_thrust',0)
    return np.hstack((v,a_total))
# integrate with scipy.integrate.solve_ivp in mission code (not shown)  # short comment