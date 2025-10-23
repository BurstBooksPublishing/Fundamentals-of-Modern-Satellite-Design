import numpy as np
# candidate designs: [throughput_Mbps, latency_ms, mass_kg, cost_kUSD]
candidates = np.array([[200, 50, 400, 12000],
                       [150, 30, 350, 10000],
                       [250, 80, 500, 15000]])
# normalization (nominal targets)
nom = np.array([200.0, 50.0, 400.0, 12000.0])
# metric directions: +1 for maximize, -1 for minimize
dirs = np.array([1, -1, -1, -1])
# weights for metrics (sum to 1)
w = np.array([0.5, 0.3, 0.1, 0.1])
# normalized metrics and utility
normed = (candidates / nom) ** dirs  # adjust maximize/minimize
utility = normed.dot(w) - 0.0001 * candidates[:,3]  # penalize cost slightly
rank = np.argsort(-utility)
print("Rank order (best->worst):", rank)  # prints indices of designs