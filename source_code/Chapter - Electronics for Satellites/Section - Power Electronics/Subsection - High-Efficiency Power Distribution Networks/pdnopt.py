import math
# Inputs (example GEO commsat): P_bus=2000 W, R_loop per meter, length, conv eff model
P_bus = 2000.0  # W delivered
length = 10.0   # m total harness length
R_per_m = 0.005 # ohm/m loop resistance
R_loop = R_per_m * length

def conv_eff(Vbus):
    # simple model: efficiency improves with Vbus due to lower switching current
    # values tuned to realistic converters (placeholder coefficients).
    base = 0.94
    gain = 0.02 * math.log(Vbus/28.0 + 1.0)
    return min(0.995, base + gain)

def total_loss(Vbus):
    I = P_bus / Vbus
    P_harness = (I**2) * R_loop
    eta_conv = conv_eff(Vbus)
    P_in = P_bus / eta_conv
    P_conv_loss = P_in - P_bus
    return P_harness + P_conv_loss

# sweep voltages
candidates = [28, 50, 100, 200, 400]
best = min(candidates, key=total_loss)
print(best, total_loss(best))  # best voltage and total loss in watts