import math

# Inputs: mission scenario (example values)
m0 = 3000.0            # kg, initial dry+prop mass
delta_v = 1500.0      # m/s, required delta-v GTO->GEO (approx)
Isp = 1600.0          # s, ion thruster specific impulse
g0 = 9.80665          # m/s^2, standard gravity
T0 = 0.25             # N, nominal thrust per thruster
n_thrusters = 4       # number of parallel thrusters
T_total = T0 * n_thrusters

# Nominal propellant mass from rocket equation (eq.1)
m_prop = m0 * (1.0 - math.exp(-delta_v / (Isp * g0)))

# Nominal burn time (eq.2)
t_nominal = (Isp * g0 * m0 / T_total) * (1.0 - math.exp(-delta_v / (Isp * g0)))

# Time-stepped simulation with exponential thrust decay
tau_e = 5.0 * 365*24*3600  # s, erosion timescale (5 years)
dt = 24*3600               # s, 1-day timestep
t = 0.0
v = 0.0
m = m0
T = T_total
prop_used = 0.0

while v < delta_v and t < 20*365*24*3600:  # limit 20 years
    # instantaneous mass flow
    mdot = T / (Isp * g0)
    # delta-v for this timestep (simple euler)
    dv = (T / m) * dt
    v += dv
    prop_used += mdot * dt
    m -= mdot * dt
    t += dt
    T = T0 * n_thrusters * math.exp(-t / tau_e)  # decaying thrust

# Print results (would be returned/recorded in engineering use)
# prop_used, t provide simulation-based margins beyond nominal predictions