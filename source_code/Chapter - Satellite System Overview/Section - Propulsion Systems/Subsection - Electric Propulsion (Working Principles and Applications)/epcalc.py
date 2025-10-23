import math

# Inputs: mission parameters (SI units)
m0 = 1000.0        # initial dry mass + propellant, kg
delta_v = 1500.0   # required delta-v, m/s
P = 2000.0         # available electric power to thruster, W
Isp = 3000.0       # specific impulse, s
eta = 0.6          # thruster efficiency (fraction)
g0 = 9.80665       # gravity, m/s^2

ve = Isp * g0                      # exhaust velocity, m/s
# propellant mass from rocket eqn
mp = m0 * (1.0 - math.exp(-delta_v / ve))
# thrust from power-limited relation
T = 2.0 * eta * P / ve
# burn time to deliver delta-v assuming constant thrust and instantaneous mass change
# use integral T = m(t) * dv/dt -> approximate with average mass
m_avg = m0 - 0.5 * mp
t_burn = (m_avg * delta_v) / T     # seconds

print(f"ve={ve:.1f} m/s, propellant={mp:.1f} kg, thrust={T*1e3:.3f} mN, burn_time={t_burn/3600:.2f} h")
# (comments above quantify design outputs for system trades)