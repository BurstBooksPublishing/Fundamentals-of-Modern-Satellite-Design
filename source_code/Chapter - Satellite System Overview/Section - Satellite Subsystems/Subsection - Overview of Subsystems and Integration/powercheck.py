import numpy as np
# nominal consumptions (W) for modes: idle, imaging, downlink
P = {'avionics': np.array([20, 25, 22]),
     'payload':  np.array([5, 120, 30]),
     'comms':    np.array([2, 5, 150]),
     'aocs':     np.array([10, 12, 11])}
Pgen = np.array([200, 200, 200])        # solar gen per mode (W)
Pbatt_allowed = 100                     # battery discharge allowance (W)
# compute totals and margins
total = sum(v for v in P.values())
margin = Pgen + Pbatt_allowed - total
print('Mode totals (W):', total)         # prints per-mode totals
print('Margins (W):', margin)            # positive=OK, negative=violation
# dependency matrix (1=depends on)
deps = np.array([[0,1,0,0],              # avionics depends on payload?
                 [0,0,0,0],
                 [1,0,0,0],
                 [0,1,0,0]])
# quick reachability check (transitive closure)
reach = np.linalg.matrix_power((deps>0).astype(int)+np.eye(4),4) > 0
print('Dependency reachability:\n', reach)  # True indicates indirect dependency