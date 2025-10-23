# contact: (start, end, rate_bps)
contacts = [(0, 60, 20e6), (300, 360, 15e6)]  # seconds, rate approximated
# bundles: (id, size_bytes, priority) higher value = higher priority
bundles = [('B1', 5_000_000, 10), ('B2', 15_000_000, 5), ('B3', 2_000_000, 8)]

def contact_capacity(contact):
    # simple trapezoid approx with constant rate here
    start, end, rate = contact
    return rate * (end - start) / 8.0  # convert bits to bytes (8 bits/byte)

schedule = {}  # contact index -> list of scheduled bundle ids
remaining = {b[0]: b[1] for b in bundles}

for i, c in enumerate(contacts):
    cap = contact_capacity(c)
    # pack by priority descending
    for bid, size, pr in sorted(bundles, key=lambda x: -x[2]):
        if remaining[bid] == 0:
            continue
        assign = min(remaining[bid], cap)
        if assign > 0:
            schedule.setdefault(i, []).append((bid, assign))
            remaining[bid] -= assign
            cap -= assign
            if cap <= 0:
                break

# schedule now maps contacts to assigned bundle segments
print(schedule)  # on real system, pass to link manager for transmission