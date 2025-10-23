import numpy as np

# Parameters: MTBF (hours), mean repair time (hours), sim time (hours)
MTBF = 10000.0          # mean time between failures (exponential)
MTTR = 72.0             # mean time to repair (hours)
Tsim = 365*24.0         # simulate one year
ntrials = 10000         # Monte Carlo trials

def simulate_once():
    t = 0.0
    uptime = 0.0
    while t < Tsim:
        # time to next failure (exponential)
        tf = np.random.exponential(MTBF)
        if t + tf >= Tsim:
            uptime += Tsim - t
            break
        uptime += tf
        t += tf
        # repair time (exponential)
        tr = np.random.exponential(MTTR)
        t += tr
    return uptime / Tsim

availabilities = [simulate_once() for _ in range(ntrials)]
print("Mean availability:", np.mean(availabilities))  # fraction of time operational