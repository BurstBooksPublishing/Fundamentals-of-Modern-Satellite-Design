import numpy as np
# params (example values)
C0 = 1e6                # fixed launch & integration ($)
c_kg = 20000            # $/kg launch marginal cost
unit_cost_per_kg = 5000 # $/kg manufacturing
lambda_base = 1e-4      # base failure rate per hour
beta_complex = 5e-6     # failure increase per complexity unit
T_mission = 3*365*24    # mission hours (3 years)

payload_masses = np.linspace(10,200,40) # kg sweep
results = []
for mp in payload_masses:
    m_bus = 100.0                    # baseline bus dry mass
    m_total = m_bus + mp
    C_launch = C0 + c_kg*m_total    # Eq. launch_cost
    C_manufacture = unit_cost_per_kg*m_total
    # simple complexity metric: unique parts ~ payload mass factor
    complexity = 50 + 0.2*mp        # arbitrary scaling
    lambda_tot = lambda_base + beta_complex*complexity
    R = np.exp(-lambda_tot * T_mission)
    C_total = C_launch + C_manufacture
    results.append((mp, m_total, C_total, R))
# results used to build Pareto front for decision analysis