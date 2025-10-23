import math, itertools
# exponential reliability model
def R_exp(lam, t):
    return math.exp(-lam*t)

# k-of-n reliability (identical components)
def R_k_of_n(R, n, k):
    # cumulative binomial probability of >= k successes
    prob = 0.0
    for i in range(k, n+1):
        prob += math.comb(n, i) * (R**i) * ((1-R)**(n-i))
    return prob

# TMR with imperfect voter reliability Rv
def R_TMR_with_voter(R, Rv):
    # system = voter AND (at least two of three modules agree)
    # reliability of module majority = 3R^2 - 2R^3
    maj = 3*R**2 - 2*R**3
    return Rv * maj

# example usage
lam = 1e-6       # per hour
t = 43800        # 5 years in hours
R = R_exp(lam, t)
Rv = 0.9999      # voter reliability
print("Single R:", R)
print("TMR w/ voter:", R_TMR_with_voter(R, Rv))