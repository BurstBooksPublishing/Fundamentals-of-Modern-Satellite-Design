# Simulate three compute lanes with voting and auto-replace
import random, time

def lane_result(fault_prob):
    return 0 if random.random() < fault_prob else 1  # 1=correct, 0=fault

def vote(results):
    # majority vote; returns voted outcome and indices disagreeing
    ones = [i for i,r in enumerate(results) if r==1]
    zeros = [i for i,r in enumerate(results) if r==0]
    voted = 1 if len(ones)>=2 else 0
    disagree = ones if voted==0 else zeros
    return voted, disagree

# parameters
fault_prob = 0.01
lanes = [True, True, True]  # True=operational
for t in range(1000):
    results = [lane_result(fault_prob) if lanes[i] else 0 for i in range(3)]
    voted, disagree = vote(results)
    # fault handling: replace failing lane if possible
    for idx in disagree:
        lanes[idx] = False   # mark failed
    # try warm start of a cold spare (simple probabilistic restart)
    for i in range(3):
        if not lanes[i] and random.random() < 0.05:
            lanes[i] = True   # successful restart
    # telemetry and brief delay
    # print(t, voted, lanes)
    time.sleep(0.001)