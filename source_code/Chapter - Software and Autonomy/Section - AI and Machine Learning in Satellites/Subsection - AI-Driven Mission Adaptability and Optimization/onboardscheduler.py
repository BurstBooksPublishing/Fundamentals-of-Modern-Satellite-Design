import cvxpy as cp
import numpy as np

# inputs: values, power_req, data_size for N tasks; E_avail and D_cap for current window
N = len(values)                     # number of candidate tasks
x = cp.Variable(N, boolean=True)    # select task or not
obj = values @ x                    # maximize total expected utility
constraints = [
    power_req @ x <= E_avail,       # power constraint (W or energy units)
    data_size @ x <= D_cap          # downlink capacity constraint (MB)
]
prob = cp.Problem(cp.Maximize(obj), constraints)
prob.solve(solver=cp.GLPK_MI)      # use a mixed-integer solver suitable for flight
# x.value yields selected tasks; proceed with plan execution