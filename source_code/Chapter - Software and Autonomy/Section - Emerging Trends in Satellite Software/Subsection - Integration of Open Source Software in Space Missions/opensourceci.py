import math
# input parameters
N = 200            # number of satellites in constellation
lambda_vuln = 0.02 # vulnerabilities per satellite per month
t_patch = 1.5      # patch latency in months

# expected number of affected satellites before patch
p_exposed = 1 - math.exp(-lambda_vuln * t_patch)  # exposure probability
expected_affected = N * p_exposed                 # expected count

print(f"Exposure probability per satellite: {p_exposed:.4f}")
print(f"Expected affected satellites: {expected_affected:.1f}")

# sensitivity sweep for design trade-offs
for t in [0.5, 1.0, 2.0, 3.0]:                      # months
    p = 1 - math.exp(-lambda_vuln * t)
    print(f"t_patch={t:0.1f} mo -> affected={N*p:.1f}")  # brief results