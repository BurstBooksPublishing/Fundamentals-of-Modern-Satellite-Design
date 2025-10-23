import math

def R_exp(mtbf, t):
    return math.exp(-t/mtbf)  # basic exponential model

def series_reliability(mtbf_list, t):
    # product of component reliabilities
    r = 1.0
    for m in mtbf_list:
        r *= R_exp(m, t)
    return r

def cold_spare_reliability(mtbf_primary, mtbf_spare, t):
    # primary runs until fail, spare starts after fail (simple approximation)
    r_primary = R_exp(mtbf_primary, t)
    r_spare = (1 - R_exp(mtbf_primary, t)) * R_exp(mtbf_spare, t)  # spare success if primary failed then spare survives remaining time approx
    return r_primary + r_spare

# Example: GEO comms chain: power amp (primary+spare), modulator, antenna pointing
t_hours = 131400  # 15 years
mtbf_amp_primary = 1.2e5
mtbf_amp_spare = 1.2e5
mtbf_mod = 2.0e5
mtbf_point = 1.5e5

r_amp = cold_spare_reliability(mtbf_amp_primary, mtbf_amp_spare, t_hours)
r_chain = r_amp * R_exp(mtbf_mod, t_hours) * R_exp(mtbf_point, t_hours)
print("Subsystem reliability over 15 yr:", r_chain)  # # printed to console during analysis