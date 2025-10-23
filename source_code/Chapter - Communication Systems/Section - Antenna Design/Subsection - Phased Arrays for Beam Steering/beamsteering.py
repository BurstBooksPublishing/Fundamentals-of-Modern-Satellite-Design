import numpy as np
c=3e8
f=14e9
lam=c/f
d=lam/2
M=N=16
# element coordinates
xm = (np.arange(M)- (M-1)/2)*d
yn = (np.arange(N)- (N-1)/2)*d
# steering angles in radians
theta0 = np.deg2rad(10.0)   # steer 10 deg elevation
phi0 = 0.0
k = 2*np.pi/lam
# compute phase steering weights (uniform amplitude)
W = np.exp(-1j*k*(xm[:,None]*np.sin(theta0)*np.cos(phi0) + yn[None,:]*np.sin(theta0)*np.sin(phi0)))
# sample pattern over theta plane (phi=0)
thetas = np.linspace(-np.pi/2, np.pi/2, 1001)
AF = np.zeros_like(thetas, dtype=complex)
for i,th in enumerate(thetas):
    AF[i] = np.sum(W * np.exp(1j*k*(xm[:,None]*np.sin(th) + yn[None,:]*0.0)))
AFdB = 20*np.log10(np.abs(AF)/np.max(np.abs(AF)))
# AFdB contains pattern vs theta; analyze beamwidth and SLL externally.