import math

def required_active_units(A_comp, A_target):
    # Solve 1-(1-A_comp)^N >= A_target for N.
    if A_comp <= 0 or A_target <= 0: return None
    N = math.log(1 - A_target) / math.log(1 - A_comp)
    return math.ceil(N)

def k_of_n_availability(A_comp, N, k):
    # Compute binomial sum for k-out-of-N availability.
    from math import comb
    return sum(comb(N, i) * (A_comp**i) * ((1-A_comp)**(N-i)) for i in range(k, N+1))

# Example: component availability 0.99, target 0.9999
print(required_active_units(0.99, 0.9999))  # -> 2
print(k_of_n_availability(0.99, 3, 2))      # 2-of-3 availability