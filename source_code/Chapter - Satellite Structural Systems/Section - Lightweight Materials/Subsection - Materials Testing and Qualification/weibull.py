import numpy as np
# Inputs (example values)
eta = 1e6       # scale parameter (cycles) -- life median
beta = 2.0      # shape parameter
R_target = 0.99 # required reliability at mission cycles
N_mission = 2e5 # mission cycles
# Reliability at N_mission
R = np.exp(- (N_mission/eta)**beta )
print("Reliability:", R)          # reliability estimate
# Required eta to meet R_target
eta_req = N_mission / (-np.log(R_target))**(1.0/beta)
print("Required eta:", eta_req)
# Binomial sample size to detect defect fraction p_def with confidence c
p_def = 0.01    # allowable defect rate
c = 0.95
# n solves (1-p_def)^n = 1-c -> n = log(1-c)/log(1-p_def)
n_req = int(np.ceil(np.log(1-c)/np.log(1-p_def)))
print("Sample size needed:", n_req)  # acceptance sampling