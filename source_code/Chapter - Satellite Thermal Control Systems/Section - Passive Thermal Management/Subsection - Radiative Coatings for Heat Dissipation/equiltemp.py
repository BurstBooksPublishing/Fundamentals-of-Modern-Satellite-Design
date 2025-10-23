import numpy as np

sigma = 5.670374419e-8  # Stefan-Boltzmann constant

def equilibrium_temperature(S=1361.0, alpha=0.2, eps=0.85,
                            A_sun=0.0, A_emit=1.0, Q_int=50.0,
                            albedo_flux=0.0, ir_flux=240.0,
                            f_albedo=0.0, f_ir=0.0):
    # Compute incident solar and albedo power (W)
    P_sun = alpha * S * A_sun
    P_albedo = alpha * albedo_flux * f_albedo * A_sun
    P_ir = ir_flux * f_ir * A_emit  # Earth IR incident on radiator
    P_in = P_sun + P_albedo + P_ir + Q_int
    # Solve for T in Kelvin from sigma*eps*A_emit*T^4 = P_in
    T = (P_in / (eps * sigma * A_emit))**0.25
    return T

# Example: LEO radiator partly exposed, A_sun=0.2 m^2, Q_int=100 W
print(equilibrium_temperature(A_sun=0.2, A_emit=1.0, Q_int=100.0,
                              f_albedo=0.1, f_ir=0.3))