import numpy as np

# compute equilibrium temperature (K) for surface parameters
def eq_temperature(alpha, epsilon, S=1361.0, theta_deg=0.0):
    theta = np.radians(theta_deg)
    # balance: alpha*S*cos(theta) = epsilon*sigma*T^4
    sigma = 5.670374419e-8  # Stefan-Boltzmann constant
    power = alpha * S * np.cos(theta)
    T = (power / (epsilon * sigma))**0.25
    return T

# example: sun-facing panel
print(eq_temperature(0.9, 0.85, theta_deg=0.0))  # ~394 K