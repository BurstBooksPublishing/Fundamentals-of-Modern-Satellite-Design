import pulp  # ILP solver
# sample data: passes list of (pass_id, sat, start, end, throughput)
passes = [('p1','satA',0,600,5e6),('p2','satB',300,900,3e6)]
antennas = ['A1','A2']
# decision variables
x = pulp.LpVariable.dicts('x', [(p,a) for p in range(len(passes)) for a in antennas],
                          0,1,cat='Binary')
prob = pulp.LpProblem('assign', pulp.LpMaximize)
# objective: maximize total bytes (throughput * duration)
prob += pulp.lpSum(x[(i,a)] * passes[i][4] * (passes[i][3]-passes[i][2])
                   for i in range(len(passes)) for a in antennas)
# non-overlap constraint per antenna (pairwise check)
for a in antennas:
    for i in range(len(passes)):
        for j in range(i+1,len(passes)):
            si,sj = passes[i][2],passes[j][2]
            ei,ej = passes[i][3],passes[j][3]
            if not (ei <= sj or ej <= si):  # overlap
                prob += x[(i,a)] + x[(j,a)] <= 1
# each pass assigned at most once
for i in range(len(passes)):
    prob += pulp.lpSum(x[(i,a)] for a in antennas) <= 1
prob.solve()
# results
for i in range(len(passes)):
    for a in antennas:
        if x[(i,a)].value() > 0.5:
            print('assign', passes[i][0], '->', a)