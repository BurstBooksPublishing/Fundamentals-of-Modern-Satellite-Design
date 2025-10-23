import math,random
# Parameters (tune per mission)
C0 = 2.0e6      # concept-phase cost (USD)
c_iter = 1.2e5  # average incremental cost per iteration
B_inf = 5.0e6   # asymptotic benefit (value units)
alpha = 0.6     # convergence rate
p_detect = 0.7  # probability change detected early
q_late = 3.0    # multiplier for late rework cost
# Simulation loop
def simulate(max_iter=12):
    total_cost = C0
    benefits = 0.0
    for n in range(1, max_iter+1):
        # Randomize iteration cost to reflect discovery severity
        c = c_iter * (1.0 + 0.5*random.random())
        total_cost += c
        # Early/late detection rework model
        if random.random() > p_detect:
            total_cost += c * q_late  # late rework penalty
        benefits = B_inf*(1.0 - math.exp(-alpha*n))
        # stop if marginal benefit small
        if (B_inf*alpha*math.exp(-alpha*n)) < c_iter:
            break
    return {'iterations':n,'cost':total_cost,'benefit':benefits}
# Run example
print(simulate(10))  # brief output for scheduling trade-off