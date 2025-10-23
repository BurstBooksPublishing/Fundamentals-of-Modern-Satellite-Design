import numpy as np
c = 299792458.0           # m/s
# input parameters (modify for scenario)
Pt = 1e6                  # transmitter power [W]
lambda_m = 1.06e-6        # wavelength [m]
Dt = 50.0                 # transmitter diameter [m]
A_sail = 100.0            # sail area [m^2]
m = 10.0                  # total mass [kg]
eta = 0.98                # reflectivity efficiency
# derived quantities
theta = 1.22*lambda_m/Dt                   # rad
r_beam = lambda z: z*theta                 # beam radius at z
Pr = lambda z: Pt * (A_sail / (np.pi*(r_beam(z))**2))  # received power approx
# integrate until sail fills small fraction of beam
z_vals = np.linspace(1.0,1e8,10000)        # m
a_vals = np.maximum(0.0, 2*eta*Pr(z_vals)/(m*c))
# cumulative delta-v (simple forward Euler)
dv = np.cumsum(a_vals * np.gradient(z_vals)/np.sqrt(c**2 + (np.gradient(z_vals))**2)) # approx time->space mapping
# print key results
imax = np.argmax(a_vals)
print("Peak acceleration (m/s^2):", a_vals[imax])
print("Range for significant acceleration (m):", z_vals[np.where(a_vals>0.01)[0][-1]])