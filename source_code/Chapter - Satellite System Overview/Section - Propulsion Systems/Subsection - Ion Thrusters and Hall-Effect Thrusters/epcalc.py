import math

# Inputs (replace with mission values)
m0 = 3000.0           # initial mass, kg
delta_v = 1500.0      # required delta-V, m/s
Isp = 3000.0          # specific impulse, s
thrust = 0.1          # thrust per thruster, N

g0 = 9.80665
Ve = Isp * g0         # effective exhaust velocity, m/s

# Propellant mass from rocket equation
mp = m0 * (1.0 - math.exp(-delta_v / Ve))

# Time to deliver delta-v at constant thrust
burn_time_s = (m0 * delta_v) / thrust

print(f"Ve = {Ve:.1f} m/s")
print(f"Propellant mass = {mp:.1f} kg")
print(f"Burn time = {burn_time_s/3600/24:.1f} days")  # convert to days