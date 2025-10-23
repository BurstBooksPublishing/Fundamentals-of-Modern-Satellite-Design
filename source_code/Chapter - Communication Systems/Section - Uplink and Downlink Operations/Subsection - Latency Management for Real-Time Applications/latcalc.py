# compute one-way latency components (meters, seconds)
c = 3e8                       # speed of light
def prop_delay(km):           # km altitude to prop delay one-way approx
    d = (km+6371)*1000 - 6371000  # rough slant: altitude above ground (m)
    return d / c

def total_latency(km,proc_ms,frame_ms,handoffs,ho_ms):
    Lprop = prop_delay(km)
    Lproc = proc_ms/1000.0
    Lframe = frame_ms/1000.0
    Lhandover = handoffs * (ho_ms/1000.0)
    return Lprop + Lproc + Lframe + Lhandover

# Example: LEO 600 km, 5 ms processing, 10 ms frame, 2 handovers at 20 ms each
print("One-way latency (s):", total_latency(600,5,10,2,20))
# Use this in mission budgets to compare with L_req.