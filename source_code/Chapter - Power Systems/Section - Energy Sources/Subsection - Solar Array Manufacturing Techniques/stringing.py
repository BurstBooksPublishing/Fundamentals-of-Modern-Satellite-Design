import numpy as np

# Input: cell data (I_sc [A], V_oc [V], P_bol [W]), mission params
cells = np.loadtxt('cell_list.csv', delimiter=',')  # columns: I_sc, V_oc, P_bol
P_required_EOL = 120.0  # W end-of-life required
r = 0.007  # annual degradation fraction
t_years = 15
# compute required BOL accounting for degradation
P_required_BOL = P_required_EOL / ((1 - r)**t_years)

# greedy pack cells into N_series strings to meet voltage and power
N_series = 36  # design choice for string voltage
strings = []
cells_sorted = cells[cells[:,2].argsort()[::-1]]  # sort by P_bol desc
while cells_sorted.size:
    s = cells_sorted[:N_series]
    strings.append(s)
    cells_sorted = cells_sorted[N_series:]

# compute delivered BOL power (approx)
P_bol_total = sum([s[:,2].sum() for s in strings])
print(f'BOL power: {P_bol_total:.1f} W, required: {P_required_BOL:.1f} W')
# further steps: simulate mismatch losses and add margin