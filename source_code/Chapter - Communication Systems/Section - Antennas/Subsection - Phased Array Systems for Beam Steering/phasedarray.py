import numpy as np
# Parameters
N = 32                 # number of elements
lam = 0.03             # wavelength (m), e.g. 10 GHz -> 0.03 m
d = lam/2              # element spacing to avoid grating lobes
theta = np.linspace(-np.pi/2, np.pi/2, 2000)
k = 2*np.pi/lam
# Steering angle (radians)
theta0 = np.deg2rad(10)    # steer to 10 degrees
# Compute progressive phase for steering
beta = -k * d * np.sin(theta0)
n = np.arange(N)
w = np.exp(1j * n * beta)  # uniform amplitude, phased weights
# Array factor (normalized)
AF = np.abs(np.dot(w, np.exp(1j * k * n[:,None] * d * np.sin(theta))))
AF_db = 20*np.log10(AF / AF.max())
# AF_db now used for beamwidth and sidelobe analysis (plotting omitted).