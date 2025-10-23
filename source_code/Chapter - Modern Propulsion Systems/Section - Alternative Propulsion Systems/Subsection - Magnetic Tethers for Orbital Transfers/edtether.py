import numpy as np
# inputs (SI)
B=50e-6         # magnetic field (T)
v=7700.0        # orbital speed (m/s)
L=5000.0        # tether length (m)
R_tether=100.0  # tether+system resistance (ohm) conservative
I = (B*v*L)/(R_tether)  # current (A) from emf/R
F = I*L*B        # Lorentz force magnitude (N) approx
m=500.0          # spacecraft mass (kg)
a_acc = F/m      # acceleration (m/s^2)
mu=3.986004418e14
a_orbit=6771000.0 # semimajor axis (m) example 400 km altitude
da_dt = (2*a_orbit*a_orbit/mu)*(F*v/m) # from dE/dt relation
# print results (simple)
print("I (A)=",I,"F (N)=",F,"a_acc (m/s2)=",a_acc,"da/dt (m/s)=",da_dt)