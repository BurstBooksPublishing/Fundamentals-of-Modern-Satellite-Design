# compute converter losses and theta_ja requirement (simple model)
def converter_thermal(P_out, eta, T_j_max, T_amb):
    # P_out: output power (W), eta: efficiency (0-1)
    P_loss = P_out*(1.0/eta - 1.0)          # eq. (3)
    if P_loss <= 0:
        raise ValueError("Non-positive loss; check efficiency")
    theta_ja_req = (T_j_max - T_amb)/P_loss  # allowable thermal resistance (C/W)
    return P_loss, theta_ja_req

# Example: 50 W output, 92% efficiency, Tj_max 125 C, ambient 40 C
P_out = 50.0
eta = 0.92
T_j_max = 125.0
T_amb = 40.0
P_loss, theta_req = converter_thermal(P_out, eta, T_j_max, T_amb)
print(f"Loss {P_loss:.2f} W, max theta_ja {theta_req:.2f} C/W")  # inline comment: use to size heatsink