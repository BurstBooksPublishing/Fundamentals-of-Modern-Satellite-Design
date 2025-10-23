# Simple electric propulsion trade calculator (example values)
import math

g0 = 9.81             # m/s^2
DeltaV = 1500.0       # m/s required (GTO->GEO)
Isp = 3000.0          # s (ion engine)
eta = 0.6             # overall thruster efficiency
T = 0.25              # N, thrust level
m_dry = 2000.0        # kg, spacecraft dry mass estimate

# propellant fraction (of initial mass)
f_p = 1.0 - math.exp(-DeltaV/(Isp*g0))

# required power from equation (2): P = T * Isp * g0 / (2*eta)
P_req = T * Isp * g0 / (2.0 * eta)

# approximate transfer time using mean mass
m_prop_guess = f_p * (m_dry + 0.0)  # initial approximation
m_avg = m_dry + 0.5 * m_prop_guess
t_seconds = DeltaV * m_avg / T
t_days = t_seconds / 86400.0

print(f"Propellant fraction (initial mass): {f_p:.3%}")
print(f"Required electric power: {P_req/1000:.2f} kW")
print(f"Approx transfer time: {t_days:.1f} days")