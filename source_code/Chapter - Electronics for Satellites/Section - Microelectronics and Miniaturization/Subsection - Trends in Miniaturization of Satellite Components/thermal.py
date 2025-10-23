def min_area_for_deltaT(P, k, L, deltaT_allowed):
    # P: power dissipated [W], k: thermal conductivity [W/mK],
    # L: thermal path length [m], deltaT_allowed: [K]
    # returns minimum area [m^2]
    Rth_max = deltaT_allowed / P                   # max allowable thermal resistance
    A_min = L / (k * Rth_max)                       # from Rth = L/(kA)
    return A_min

# Example: GaN amplifier dissipating 2 W, k=150 W/mK (copper path), L=0.002 m, allow 20 K rise
P = 2.0
k = 150.0
L = 2e-3
deltaT = 20.0
area_min = min_area_for_deltaT(P, k, L, deltaT)
print("Minimum PCB area (cm^2):", area_min*1e4)     # convert m^2 to cm^2