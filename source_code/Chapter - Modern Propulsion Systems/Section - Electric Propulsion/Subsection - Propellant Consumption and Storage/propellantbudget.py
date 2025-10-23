import math

# Inputs (engineering units)
m0 = 1800.0           # initial spacecraft mass [kg]
delta_v = 1500.0     # total required delta-v [m/s]
Isp = 3000.0         # specific impulse [s]
P_available = 6e3    # electrical power available to thruster [W]
eta = 0.65           # thruster efficiency (fraction)
M_max = 50.0         # thruster cumulative throughput limit [kg]

g0 = 9.80665
ve = Isp * g0                         # effective exhaust velocity [m/s]
# Propellant mass from Tsiolkovsky
mp = m0 * (1.0 - math.exp(-delta_v / ve))

# Select a nominal thrust from power and eq. (solve T = 2*eta*P/ve)
T = 2.0 * eta * P_available / ve     # thrust [N]
mdot = T / ve                         # mass flow rate [kg/s]
burn_time = mp / mdot                 # total thrusting time [s]
t_max = M_max / mdot                  # life-limited operating time [s]

# Print key results (designer uses these in trade-offs)
print(f"Required propellant mp = {mp:.2f} kg")
print(f"Nominal thrust T = {T:.3f} N, mdot = {mdot:.6f} kg/s")
print(f"Total burn time = {burn_time/3600.:.2f} hr")
print(f"Thruster-limited op time t_max = {t_max/3600.:.2f} hr")