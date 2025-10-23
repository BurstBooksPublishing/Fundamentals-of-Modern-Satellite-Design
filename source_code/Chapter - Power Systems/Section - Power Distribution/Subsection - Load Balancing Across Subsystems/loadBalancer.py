import numpy as np

def allocatePower(demands, priorities, aMin, aMax, Pbus):
    # demands, priorities, aMin, aMax: numpy arrays length N
    # Step 1: ensure minima to critical loads
    allocations = np.copy(aMin)
    remaining = Pbus - allocations.sum()
    if remaining <= 0:
        return allocations  # only minima can be supplied

    # Step 2: identify flexible loads (not at max)
    flexible = (allocations < aMax)
    # Step 3: compute weight-share (use inverse priority => lower priority gets scaled)
    weights = 1.0 / (priorities + 1e-6)
    weights *= flexible  # zero weight for saturated loads

    # Step 4: target extra = demand - current allocation, non-negative
    targets = np.maximum(demands - allocations, 0.0)

    # Step 5: iterative proportional distribution with capping
    while remaining > 1e-3 and flexible.any():
        share = weights * targets
        if share.sum() == 0:
            break
        share = remaining * (share / share.sum())
        # cap at max increments
        increment = np.minimum(share, aMax - allocations)
        allocations += increment
        remaining -= increment.sum()
        # update flexible, weights, targets
        flexible = (allocations < aMax) & (allocations < demands)
        weights = 1.0 / (priorities + 1e-6) * flexible
        targets = np.maximum(demands - allocations, 0.0)

    return allocations  # final allocations to apply to power switches