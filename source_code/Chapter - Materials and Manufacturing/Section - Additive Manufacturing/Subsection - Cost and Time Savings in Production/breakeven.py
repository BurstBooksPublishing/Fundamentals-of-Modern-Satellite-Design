import numpy as np
# input parameters (engineer to adjust per part)
C_tool = 200000.0        # tooling cost $ (traditional)
C_unit_trad = 3000.0     # unit cost $ (traditional)
C_unit_AM = 5000.0       # unit cost $ (additive)
N = np.arange(1,1001)    # production run sizes

C_trad = C_tool + N*C_unit_trad
C_AM = N*C_unit_AM

# compute break-even analytically and numerically
N_star = C_tool / (C_unit_AM - C_unit_trad)  # analytic break-even
# optional: cost at specific N (for program budget)
def program_cost(n):
    return C_trad[n-1], C_AM[n-1]            # costs for given n

# print summary (engineer to log)
print(f"Analytic break-even N*: {N_star:.1f}")
# (plotting code omitted; integrate into program dashboard)