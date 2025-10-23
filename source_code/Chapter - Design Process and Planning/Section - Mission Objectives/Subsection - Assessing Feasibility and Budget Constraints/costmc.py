import numpy as np
# distributions: dev, hw, launch, ops, contingency (in USD millions)
dev = np.random.normal(30, 6, 10000)   # dev N(30,6)
hw  = np.random.normal(40, 10, 10000)  # hw N(40,10)
launch = np.random.normal(20, 5, 10000) # launch N(20,5)
ops = np.random.normal(15, 4, 10000)   # ops N(15,4)
cont = np.random.uniform(5, 15, 10000) # contingency uniform
total = dev + hw + launch + ops + cont
# compute risk metric: probability of exceeding baseline budget
budget = 100.0
prob_over = np.mean(total > budget)
print(f'P(total>{budget}M) = {prob_over:.2%}')  # probability output