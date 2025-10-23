import numpy as np
# physical params (aluminum strut example)
L = 0.5                 # length (m)
nx = 50                 # nodes
dx = L/(nx-1)
k = 205.0               # W/(m*K)
rho = 2700.0            # kg/m3
cp = 900.0              # J/(kg*K)
alpha = k/(rho*cp)
dt = 0.5*dx*dx/alpha    # stability check for explicit scheme
t_final = 600.0         # simulate 10 minutes
nt = int(t_final/dt)
T = np.linspace(300.0, 100.0, nx)  # initial gradient: bus->instrument
# boundary: bus held at 300K, instrument at 100K (Dirichlet)
for n in range(nt):
    Tn = T.copy()
    # interior nodes explicit update
    T[1:-1] = Tn[1:-1] + alpha*dt/dx**2*(Tn[2:] - 2*Tn[1:-1] + Tn[:-2])
    # re-apply Dirichlet boundaries
    T[0] = 300.0
    T[-1] = 100.0
# report maximum gradient (K/m)
max_grad = np.max(np.abs(np.diff(T))/dx)
print("Max gradient (K/m):", max_grad)