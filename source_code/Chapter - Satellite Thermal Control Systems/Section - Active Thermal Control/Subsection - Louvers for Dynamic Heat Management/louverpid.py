import math
# parameters (example values)
A = 1.0               # radiator area [m2]  # panel size
eps_open = 0.85       # emissivity when open
eps_closed = 0.05     # emissivity when closed
sigma = 5.670374e-8   # Stefan-Boltzmann const
T_space = 3.0         # space temp [K]

# PID gains (tuned in test)
Kp, Ki, Kd = 0.8, 0.01, 0.05

# simple state
integral = 0.0
prev_err = 0.0
angle_deg = 0.0       # current louver angle (0=open, 90=closed)

def open_fraction(angle_deg):
    a = math.radians(angle_deg)
    return max(0.0, min(1.0, math.cos(a)))  # geometric approx

def radiative_cooling(T, f):
    eps_eff = eps_open*f + eps_closed*(1.0-f)
    return A*sigma*eps_eff*(T**4 - T_space**4)

def pid_control(T_meas, T_set, dt, P_payload, Q_env):
    global integral, prev_err, angle_deg
    err = T_set - T_meas
    integral += err*dt
    deriv = (err - prev_err)/dt if dt>0 else 0.0
    u = Kp*err + Ki*integral + Kd*deriv   # control effort
    prev_err = err
    # map u to angle change, limit to motor capability
    angle_deg += max(-5.0, min(5.0, 10.0*u*dt))  # deg/s clamped
    angle_deg = max(0.0, min(90.0, angle_deg))
    f = open_fraction(angle_deg)
    Qrad = radiative_cooling(T_meas, f)
    # thermal check (simple): if Qrad < dissipation, temp will rise
    return angle_deg, f, Qrad