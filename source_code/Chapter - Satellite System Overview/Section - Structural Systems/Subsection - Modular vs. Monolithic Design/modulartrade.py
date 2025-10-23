import math

# Parameters (example values)
m_bus = 200.0            # kg, baseline bus
m_payload = 150.0        # kg, payload total
m_iface = 3.0            # kg per interface
C_launch = 20000.0       # $/kg
C_prod_per_module = 500000.0  # $ per module build
R_unit = 0.92            # reliability per module
V_ops = 1e7              # $ valuation per unit reliability

def reliability_parallel(k):
    return 1.0 - (1.0 - R_unit)**k  # eq. (3)

def cost_metric(k):
    m_total = m_bus + m_payload + k*m_iface
    C_launch_tot = C_launch * m_total
    C_prod = C_prod_per_module * k
    R_sys = reliability_parallel(k)
    return C_prod + C_launch_tot - V_ops * R_sys

# Evaluate 1..6 modules
for k in range(1,7):
    print(f"k={k}, cost_metric=${cost_metric(k):,.0f}, R_sys={reliability_parallel(k):.4f}")
    # yields design insight on diminishing returns