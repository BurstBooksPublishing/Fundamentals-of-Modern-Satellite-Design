import math
sigma = 5.670374419e-8  # Stefan-Boltzmann
def size_heat_sink(Q_pulse, t_pulse, dT, c, eps, T_rad, steady_Q=0.0):
    # mass for transient storage (kg)
    m = (Q_pulse * t_pulse) / (c * dT)
    # radiator area for steady load + average pulse power (m^2)
    Q_avg = steady_Q + (Q_pulse * t_pulse) / (t_pulse + 1.0)  # simple avg over cycle
    A = Q_avg / (eps * sigma * T_rad**4)
    return m, A

# Example: 50 W, 600 s pulse; aluminum c=900 J/kgK; eps=0.85; T_rad=300 K
m_example, A_example = size_heat_sink(50.0, 600.0, 10.0, 900.0, 0.85, 300.0)
print(m_example, A_example)  # mass (kg), radiator area (m^2)