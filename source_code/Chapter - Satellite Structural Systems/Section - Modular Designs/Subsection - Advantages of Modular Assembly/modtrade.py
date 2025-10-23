import numpy as np

# Parameters (example values)
Cu = 200000.0        # unit manufacturing cost per module (USD)
Cint = 50000.0       # integration overhead per module interface (USD)
Cl = 20000.0         # launch cost per kg (USD)
m_base = 50.0        # base module mass (kg)
m_if = 5.0           # mass penalty per interface (kg)

def total_cost(N):
    # module mass grows slightly due to interface hardware
    m_modules = N * (m_base + (N-1)*m_if/N)
    # cost: manufacturing + integration + launch
    return N*Cu + (N-1)*Cint + m_modules*Cl

Ns = np.arange(1,13)
costs = [total_cost(N) for N in Ns]

for N,c in zip(Ns,costs):
    print(f"Modules={N:2d}, TotalCost=${c:,.0f}")  # brief output