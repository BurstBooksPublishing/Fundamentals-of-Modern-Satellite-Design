import math

def min_redundancy(r, R_target):
    # r: reliability of single module (0<r<1)
    # R_target: desired system reliability (0<R_target<1)
    if r <= 0 or r >= 1:
        raise ValueError("r must be between 0 and 1")
    if R_target <= 0 or R_target >= 1:
        raise ValueError("R_target must be between 0 and 1")
    n = math.ceil(math.log(1 - R_target) / math.log(1 - r))
    return n

# Example parameters for a LEO comms payload
r = 0.92             # per-module one-year reliability
R_target = 0.995     # target one-year reliability
m_mod = 8.0          # kg per module
unit_cost = 120e3    # USD per module

n = min_redundancy(r, R_target)            # minimal modules
mass_penalty = (n - 1) * m_mod             # extra mass due to redundancy
cost_penalty = n * unit_cost               # procurement cost proxy

print(n, mass_penalty, cost_penalty)       # outputs for engineering trade