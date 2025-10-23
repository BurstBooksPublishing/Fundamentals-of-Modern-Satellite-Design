import pulp  # linear/integer programming
# Define tasks and windows (example numbers)
tasks = ["imgA","imgB","imgC"]
vol = {"imgA":200,"imgB":500,"imgC":300}  # MB per task
bw = {"imgA":2,"imgB":5,"imgC":3}        # Mbps requirement
windows = ["w1","w2"]
B = {"w1":6,"w2":5}  # Mbps capacity per window
avail = {("imgA","w1"):1,("imgA","w2"):0, # availability matrix
         ("imgB","w1"):1,("imgB","w2"):1,
         ("imgC","w1"):0,("imgC","w2"):1}

# Decision variables
x = pulp.LpVariable.dicts("x",(tasks,windows),lowBound=0,upBound=1,cat='Binary')

# Objective: maximize total volume transferred
prob = pulp.LpProblem("downlink_sched",pulp.LpMaximize)
prob += pulp.lpSum([vol[i]*x[i][w] for i in tasks for w in windows])

# Capacity constraints per window
for w in windows:
    prob += pulp.lpSum([bw[i]*x[i][w] for i in tasks]) <= B[w]

# Availability and single-schedule constraints
for i in tasks:
    prob += pulp.lpSum([x[i][w] for w in windows]) <= 1
    for w in windows:
        prob += x[i][w] <= avail[(i,w)]

prob.solve()  # solver selection via PuLP
# Results: print schedule (simple output)
for i in tasks:
    for w in windows:
        if x[i][w].value() > 0.5:
            print(f"Schedule {i} in {w}")  # short comment for operator