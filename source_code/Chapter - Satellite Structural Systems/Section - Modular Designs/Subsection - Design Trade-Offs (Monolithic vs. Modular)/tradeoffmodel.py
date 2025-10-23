# simple trade model for monolithic vs modular
import numpy as np

def trade(n, m_core=400, m_module=50, beta=10, gamma=1.1,
          C_fixed=40e6, C_module=1.2e6, C_int=0.5e6, delta=1.2,
          R_module=0.995, R_interface=0.999):
    # mass model (kg)
    m_interfaces = beta * n**gamma
    m_total = m_core + n*m_module + m_interfaces
    # cost model (USD)
    C_total = C_fixed + n*C_module + C_int * n**delta
    # reliability: assume independent module failures, interfaces multiplicative
    R_modules = 1 - (1 - R_module)**n
    R_total = R_modules * (R_interface**n)  # conservative multiplicative model
    return m_total, C_total, R_total

# sweep module count for a GEO commsat example
ns = np.arange(1,9)
for n in ns:
    m, c, r = trade(n)
    print(f"n={n:1d}  mass={m:6.1f} kg  cost=${c/1e6:5.2f}M  reliab={r:.6f}")
# adjust coefficients for CubeSat missions to compare results