from math import ceil
# passes: list of dicts with keys start,end,data_bits,priority,margin
passes = sorted(candidate_passes, key=lambda p: (-p['priority'], -p['data_bits']))  # priority first
schedule = []
current_time = day_start
min_gap = 30  # seconds for slew/reconfigure

for p in passes:
    if p['start'] < current_time:  # conflict with existing allocation
        continue
    if p['margin'] < required_margin:
        continue  # failed link-budget gate
    # allocate as much of the pass as available
    allocated_start = max(p['start'], current_time)
    allocated_end = p['end']
    if allocated_end - allocated_start <= 0:
        continue
    # compute transferable bits using predicted rate profile (simplified here)
    transferable = p['data_bits'] * ((allocated_end - allocated_start) / (p['end'] - p['start']))
    schedule.append({'pass_id': p['id'], 'start': allocated_start, 'end': allocated_end, 'bits': transferable})
    current_time = allocated_end + min_gap  # enforce inter-pass gap
# schedule now contains assigned blocks for the station