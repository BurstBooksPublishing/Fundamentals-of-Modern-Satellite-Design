# Simple plasma thruster sizing (SI units)
import math

g0 = 9.80665
def thrust_from_power(P, eta, ve):  # P (W), eta, ve (m/s)
    return 2*eta*P/ve           # from eq. (1)

def mdot_from_T_ve(T, ve):      # T (N), ve (m/s)
    return T/ve                 # mass flow rate (kg/s)

def burn_time_for_deltaV(m0, mf, T): # m0 initial, mf final, T constant (N)
    # integrate ideal rocket equation assuming constant thrust and variable mass
    # approximate using average mass for small delta-v, or solve numerically for accuracy
    return (m0 - mf) * ( (m0 + mf) / (2*T) ) # simple trapezoid mass-to-time estimate

# Example: 200 kW, 70% eff, ve=50 km/s
P = 200e3; eta=0.7; ve=50e3
T = thrust_from_power(P, eta, ve)    # N
mdot = mdot_from_T_ve(T, ve)         # kg/s
# outputs are used to size propellant tanks and radiators