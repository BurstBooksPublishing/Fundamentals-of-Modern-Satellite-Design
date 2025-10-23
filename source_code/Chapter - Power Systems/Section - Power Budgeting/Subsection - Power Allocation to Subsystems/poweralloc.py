import numpy as np
from scipy.optimize import linprog

# Example data (replace with mission numbers)
P_gen = 120.0          # W available from arrays
E_batt_usable = 200.0  # Wh usable (account for DOD)
P_batt_max = 100.0     # W max discharge rate
# Subsystems: [ADCS, Comms, Payload, OBC, Thermal]
P_min = np.array([5.0,  0.0,  0.0,  2.0,  0.0])   # W minimum keep-alive
P_max = np.array([20.0, 60.0, 80.0, 10.0, 30.0]) # W max capability
weights = np.array([10.0, 8.0, 6.0, 9.0, 5.0])   # priority weights

# Objective: maximize w^T P  => linprog minimizes, so negate
c = -weights

# Inequality: sum(P_i) <= P_gen + P_batt_max
A = np.ones((1, len(P_min)))
b = np.array([P_gen + P_batt_max])

# Bounds per variable
bounds = [(P_min[i], P_max[i]) for i in range(len(P_min))]

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
if res.success:
    P_alloc = res.x
    print("Allocated power (W):", P_alloc)    # printed during integration testing
    print("Total allocated (W):", P_alloc.sum())
else:
    print("Allocation failed:", res.message)