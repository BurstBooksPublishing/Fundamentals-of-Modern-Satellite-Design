# compute junction temperature given ambient and layered Rth (simple model)
# units: W, K, m, W/mK
P = 3.0            # power dissipation in watts (actual SoC point)
Tamb = 300.0       # ambient/case temperature [K]
# layer properties: list of (thickness[m], conductivity[W/mK], area[m^2])
layers = [
    (0.0001, 200.0, 1e-4),   # AuSn die attach (thin, high k)
    (0.001, 150.0, 1e-4),    # ceramic substrate
    (0.002, 100.0, 5e-5)     # thermal interface material (worse conductivity)
]
Rth_total = 0.0
for L, k, A in layers:
    Rth_total += L/(k*A)   # series thermal resistances
Tj = Tamb + P * Rth_total  # steady-state junction temperature
print("Total Rth (K/W):", Rth_total)  # thermal design output
print("Junction temp (K):", Tj)