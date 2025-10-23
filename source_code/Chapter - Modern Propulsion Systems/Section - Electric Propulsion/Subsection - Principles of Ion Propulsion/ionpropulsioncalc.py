import math

# Inputs: mission and thruster parameters
m0 = 2000.0           # initial mass, kg (typical small GEO payload bus)
delta_v = 2500.0      # required delta-v, m/s (low-thrust orbit raising)
Isp = 3000.0          # specific impulse, s (NSTAR-class)
P = 3000.0            # available electrical power, W

g0 = 9.80665          # m/s^2

# Propellant mass via rocket equation
mp = m0*(1.0 - math.exp(-delta_v/(g0*Isp)))  # kg

# Exhaust velocity and power-limited thrust estimate
Ve = Isp * g0                               # m/s
T = 2.0 * P / Ve                            # approximate thrust from eq (3)
burn_time = (m0 * delta_v) / T              # rough time to deliver delta-v, s

print("Propellant mass (kg):", mp)           # engineering output
print("Exhaust velocity (m/s):", Ve)
print("Estimated thrust (N):", T)
print("Approx. burn time (days):", burn_time/86400.0)  # convert to days