import math

T_hours = 15*365*24                      # mission life hours
lambda_hr = 5e-8                         # component failure rate per hour
R_elem = math.exp(-lambda_hr * T_hours) # single element reliability

m = 100                                  # series elements
R_sys_series = R_elem**m                 # series system reliability

# required number of cold spares n for desired R_target
R_target = 0.90
n = 0
while True:
    R_with_spares = 1 - (1 - R_elem)**(n+1)
    if R_with_spares >= R_target:
        break
    n += 1

print("R_elem:", R_elem)                  # use in procurement specs
print("R_sys_series:", R_sys_series)      # informs architecture change
print("cold_spares_needed:", n)           # trade against mass and power