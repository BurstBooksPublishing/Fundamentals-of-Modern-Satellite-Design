import math

def flex_trace_metrics(frequency, t_sub_m, t_film_m, w_m, sigma, mu=4*math.pi*1e-7, deltaT=0, alpha_sub=20e-6, alpha_film=19e-6, bend_R=0.02):
    # bending strain (eq.1)
    eps_bend = (t_sub_m + t_film_m) / (2.0 * bend_R)
    # thermal strain (eq.2)
    eps_th = (alpha_sub - alpha_film) * deltaT
    eps_total = eps_bend + eps_th
    # DC resistance per meter (eq.3)
    R_dc_per_m = 1.0 / (sigma * t_film_m * w_m)
    # skin depth (eq.4)
    omega = 2.0 * math.pi * frequency
    delta = math.sqrt(2.0 / (omega * mu * sigma))
    return {"eps_bend":eps_bend, "eps_th":eps_th, "eps_total":eps_total,
            "R_dc_per_m":R_dc_per_m, "skin_depth":delta}

# Example: 2.4 GHz, polyimide 50um, silver film 5um, width 1 mm, silver sigma=6.3e7 S/m
metrics = flex_trace_metrics(2.4e9, 50e-6, 5e-6, 1e-3, 6.3e7, deltaT=120, bend_R=0.03)
print(metrics)  # quick assessment for design trade-offs