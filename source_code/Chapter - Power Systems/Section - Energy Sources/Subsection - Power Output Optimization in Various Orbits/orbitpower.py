import numpy as np
R_e = 6371e3                   # Earth radius (m)
h = 600e3                      # orbit altitude (m)
r = R_e + h
n_samples = 2048
theta_an = np.linspace(0,2*np.pi,n_samples)   # true anomaly samples

# simple circular orbit ECI positions for inclination i (rad)
i = np.deg2rad(53)             # example inclination (e.g., LEO comms)
def sat_positions(r,i):
    x = r*np.cos(theta_an)
    y = r*np.sin(theta_an)*np.cos(i)
    z = r*np.sin(theta_an)*np.sin(i)
    return np.vstack((x,y,z)).T

r_sat = sat_positions(r,i)
s_hat = np.array([1.0,0.0,0.0])   # unit Sun vector in ECI (example)

def in_eclipse(r_vec,sun_hat):
    # t0 = -dot(r,sun) must be >0 for Earth between sat and Sun
    t0 = -np.dot(r_vec,sun_hat)
    perp = np.linalg.norm(np.cross(r_vec,sun_hat))
    return (perp < R_e) & (t0 > 0)

# panel normal for one-axis rotation about Y body axis, angle phi
def panel_normal(phi):
    # body-fixed: assume nominal body z-axis points to nadir; tilt about Y
    n = np.array([np.cos(phi),0,np.sin(phi)])
    return n/np.linalg.norm(n)

A = 4.0                         # array area m^2
eta = 0.28                      # reference efficiency
G0 = 1361.0
alphaT = -0.002                 # K^-1
T_ref = 298.0

def mean_power(phi):
    n = panel_normal(phi)
    P = 0.0
    for rvec in r_sat:
        if in_eclipse(rvec,s_hat):
            continue
        cos_inc = max(0.0, np.dot(n, s_hat))
        P += A * eta * G0 * cos_inc
    return P / n_samples

# optimize tilt angle by grid search
phis = np.linspace(-np.pi/2,np.pi/2,361)
Pvals = np.array([mean_power(p) for p in phis])
phi_opt = phis[np.argmax(Pvals)]
print("Optimal tilt (deg):", np.degrees(phi_opt))
print("Mean power (W):", Pvals.max())