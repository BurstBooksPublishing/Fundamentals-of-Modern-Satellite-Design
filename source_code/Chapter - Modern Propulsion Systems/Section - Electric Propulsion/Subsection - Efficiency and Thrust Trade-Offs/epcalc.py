import numpy as np

# Inputs (example): electrical power W, efficiency, vehicle mass kg, required delta-v m/s
P = 5000.0      # W
eta = 0.6       # conversion efficiency
m0 = 500.0      # initial mass kg
delta_v = 1500  # total delta-v m/s
g0 = 9.80665

def thrust(Isp):
    ve = Isp * g0
    return 2.0 * eta * P / ve   # Newtons from eq. (ref eq:thrust_power_final)

def transfer_time(Isp):
    T = thrust(Isp)
    a = T / m0                   # constant-mass approximation (conservative)
    if a <= 0:
        return np.inf
    return delta_v / a           # seconds

Isps = np.array([800, 1600, 3000])  # sample thruster families
for isp in Isps:
    T = thrust(isp)
    t_days = transfer_time(isp) / 86400.0
    print(f"Isp={isp} s: T={T:.3f} N, transfer time={t_days:.1f} days")