import math
# parameters: MTBF_hours for a radiation-hardened processor
MTBF = 5*365*24.0  # 5 years in hours
lambda_rate = 1.0/MTBF

def R(t_hours): return math.exp(-lambda_rate*t_hours)  # exponential model

def R_par(n, t): return 1 - (1 - R(t))**n  # parallel identical units

def R_TMR(t):
    r = R(t)
    # sum of probabilities for 2 or 3 working modules
    return 3*(r**2)*(1-r) + (r**3)

def R_dual_cold_spare(t):
    r = R(t)
    # two identical units used sequentially (cold spare)
    return 1 - (1-r)**2

# evaluate at mission end
t = 5*365*24.0
print("TMR reliability:", R_TMR(t))            # improved but consumes power
print("Dual cold spare reliability:", R_dual_cold_spare(t))  # lower power