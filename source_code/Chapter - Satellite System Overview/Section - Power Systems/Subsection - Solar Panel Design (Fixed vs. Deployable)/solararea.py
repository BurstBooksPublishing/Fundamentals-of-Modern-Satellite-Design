# Simple solar array sizing (conceptual) -- use mission ephemeris for final design
def required_area(P_avg, eta_bol, degradation_fraction, mu=0.9, S0=1361.0, battery_margin=0.2):
    # P_avg: average required power (W)
    # eta_bol: BOL cell efficiency (fraction)
    # degradation_fraction: fractional loss to EOL (0..1)
    # mu: average cosine losses (0..1)
    eta_eol = eta_bol * (1.0 - degradation_fraction)      # EOL efficiency
    if eta_eol <= 0:
        raise ValueError("EOL efficiency non-positive")
    # area from steady-state energy balance
    A = P_avg * (1.0 + battery_margin) / (eta_eol * S0 * mu)
    return A  # m^2

# Example: 500 W average load, 0.28 BOL eff, 20% EOL loss
print(required_area(500, 0.28, 0.20))  # returns area in m^2