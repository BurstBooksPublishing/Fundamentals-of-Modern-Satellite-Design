import math
# constants
h = 6.62607015e-34  # Planck constant (J s)
c = 299792458       # speed of light (m/s)

def received_photons(E_pulse, wavelength, theta, R, A_r, T_sys):
    E_ph = h*c/wavelength                     # photon energy
    N_tx = E_pulse / E_ph                     # transmitted photons
    frac = A_r / (math.pi * (theta*R)**2)     # geometric fraction
    return N_tx * T_sys * max(0.0, frac)      # photons at detector

# example parameters (realistic engineering values)
E_pulse = 1e-9         # 1 nJ per pulse
wavelength = 810e-9    # 810 nm band
theta = 1e-6           # divergence (rad)
R = 500e3              # range 500 km
A_r = math.pi*(0.5)**2 # 1 m diameter receiver area
T_sys = 0.1            # 10% combined transmission and QE

print(received_photons(E_pulse,wavelength,theta,R,A_r,T_sys))