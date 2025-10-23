import cvxpy as cp
import numpy as np

# inputs (example): alpha per flow, weights, min/max bandwidths, total BW
alpha = np.array([1e6, 5e5, 2e5])    # effective power terms
w = np.array([3.0, 1.0, 1.5])        # mission priorities
Bmin = np.array([1e6, 0.5e6, 0.5e6]) # Hz
Bmax = np.array([200e6, 100e6, 50e6])
B_total = 300e6

# decision variables
B = cp.Variable(len(alpha))

# concave utility: B*log2(1+alpha/B) implemented via natural log
utility = cp.sum(cp.multiply(w, B * cp.log(1 + alpha / B) / cp.log(2)))

# constraints
constraints = [B >= Bmin, B <= Bmax, cp.sum(B) <= B_total]

# solve (use convex solver available on flight computer)
prob = cp.Problem(cp.Maximize(utility), constraints)
prob.solve(solver=cp.SCS)  # choose solver appropriate for processor

# result: B.value contains allocation per flow
print("Allocated bandwidths (Hz):", B.value)  # simple debug output