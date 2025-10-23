# tasks: list of (id, priority, power, downlinkSize, duration)
# availablePower: function of time; downlinkWindow boolean
def scheduleTasks(tasks, availablePower, downlinkWindow):
    schedule = []                 # chosen task ids
    # sort by priority per unit power to favor efficient science
    tasks.sort(key=lambda t: t[1]/t[2], reverse=True)
    for task in tasks:
        tid, prio, power, dsize, dur = task
        if power <= availablePower and (dsize==0 or downlinkWindow):
            schedule.append(tid)         # accept task
            availablePower -= power     # decrement budget
            # brief: mark expected downlink bandwidth usage (not shown)
    return schedule
# Example: used in-flight for short-horizon scheduling decisions.