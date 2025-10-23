import math
# Inputs (example Ka band GEO)
freq = 30e9                   # Hz
c = 299792458.0               # m/s
lam = c / freq                # wavelength
alpha = 23e-6                 # 1/K for aluminum
Lpanel = 1.0                  # m panel length
deltaT = 5.0                  # K gradient across panel
d = 0.5 * lam                 # element spacing (m)
# Phase shift from expansion
deltaL = alpha * Lpanel * deltaT
deltaPhi = 2.0*math.pi*deltaL/lam
# Pointing error estimate for broadside
k = 2.0*math.pi/lam
deltaThetaRad = - deltaPhi / (k * d)   # approx eq (3)
deltaThetaDeg = math.degrees(deltaThetaRad)
# Ruze loss for assumed surface RMS (example)
sigma = 0.0005                # m surface RMS (0.5 mm)
ruzeLoss = math.exp(-(4.0*math.pi*sigma/lam)**2)
print("lambda (m):", lam)                  # diagnostic
print("phase shift (rad):", deltaPhi)
print("pointing error (deg):", deltaThetaDeg)
print("Ruze gain factor:", ruzeLoss)      # <1 is loss