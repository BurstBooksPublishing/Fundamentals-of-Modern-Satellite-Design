import math
# design inputs
mtbf = 200000.0             # hours (converter)
t_mission = 5*365*24       # hours
target = 0.999             # required system reliability

# component reliability
R1 = math.exp(-t_mission/mtbf)

# find minimal n
n = 1
while 1 - (1-R1)**n < target:
    n += 1
print(n, R1, 1-(1-R1)**n)   # prints n, single reliability, system reliability