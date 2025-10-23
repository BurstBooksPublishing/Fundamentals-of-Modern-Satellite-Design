import numpy as np

# constants
sigma = 5.670374419e-8  # W/m^2/K^4
F_sun = 1361.0          # W/m^2 at 1 AU

def equilibrium_temperature(alpha, eps, Fsun=F_sun, A=0.3, S=1.0, Q_ir=237.0):
    # net absorbed solar per unit area (incl. albedo fraction)
    q_solar = (1.0 - A) * S * Fsun * alpha
    # solve epsilon*sigma*T^4 = q_solar + Q_ir
    T4 = (q_solar + Q_ir) / (eps * sigma)
    return T4 ** 0.25

# example: high-emissivity paint vs gold-coated reflector
T_paint = equilibrium_temperature(alpha=0.25, eps=0.85)  # high-e paint
T_gold  = equilibrium_temperature(alpha=0.05, eps=0.02)  # gold-like
print("T_paint = {:.1f} K, T_gold = {:.1f} K".format(T_paint, T_gold))
# -- use these outputs to check component temperature limits