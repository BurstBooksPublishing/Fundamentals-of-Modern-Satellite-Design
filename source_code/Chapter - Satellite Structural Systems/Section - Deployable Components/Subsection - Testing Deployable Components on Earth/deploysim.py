import numpy as np

# Parameters (SI)
I = 2.0           # kg*m^2, rotational inertia
k = 0.0           # Nm/rad, hinge stiffness (set 0 for free hinge)
c = 0.1           # Nms/rad, damping
tau_drive = 5.0   # Nm, constant drive torque (simplified)
tau_coulomb = 0.5 # Nm, Coulomb friction magnitude
m = 50.0          # kg, panel mass
g = 9.81
r_cg = 1.0        # m, cg lever arm
dt = 0.001
T = 20.0
n = int(T/dt)
theta = 0.0
omega = 0.0
t_arr = np.linspace(0, T, n)
theta_arr = np.zeros(n)

for i, t in enumerate(t_arr):
    tau_g = m*g*r_cg*np.sin(theta)  # gravity torque
    v = omega
    tau_f = -tau_coulomb*np.sign(v) if abs(v)>1e-4 else -tau_coulomb*(v/1e-4)
    # Equation: I*omega_dot = tau_drive - tau_g - c*omega - tau_f - k*theta
    omega_dot = (tau_drive - tau_g - c*omega - tau_f - k*theta)/I
    omega += omega_dot*dt
    theta += omega*dt
    theta_arr[i] = theta

# Save for plotting / analysis (example filename)
np.savetxt('deployment_log.csv', np.vstack((t_arr, theta_arr)).T, delimiter=',')