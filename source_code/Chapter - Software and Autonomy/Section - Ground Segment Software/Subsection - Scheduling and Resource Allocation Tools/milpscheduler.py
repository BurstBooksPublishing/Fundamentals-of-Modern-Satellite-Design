import pulp
# sets: contacts C, slots S, resources R; inputs: w[c], feasible[c][r], bitrate[c], cap[r]
prob = pulp.LpProblem('sched', pulp.LpMaximize)
x = {(c,s,r): pulp.LpVariable(f"x_{c}_{s}_{r}", cat='Binary')
     for c in C for s in S for r in R}
# objective: maximize total utility (weight assigned to any slot for contact)
prob += pulp.lpSum(w[c]*x[c][s][r] for c in C for s in S for r in R)
# capacity: one resource per slot
for r in R:
    for s in S:
        prob += pulp.lpSum(x[c][s][r] for c in C) <= 1  # antenna exclusivity
# contact continuity: if contact uses k slots require >= k_min slots contiguous (simplified)
for c in C:
    # ensure assignment only in allowed slots and resources
    for s in S:
        for r in R:
            if not feasible[c][r][s]:
                prob += x[c][s][r] == 0  # SNR or visibility check
# bitrate constraint per resource per slot
for r in R:
    for s in S:
        prob += pulp.lpSum(bitrate[c]*x[c][s][r] for c in C) <= cap[r]
# solve and parse schedule
prob.solve(pulp.PULP_CBC_CMD(msg=False))