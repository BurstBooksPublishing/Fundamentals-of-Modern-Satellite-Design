# tasks: list of dicts with keys id,power,priority,requires_pointing
def select_tasks(tasks, P_avail, pointing_locked):
    # sort by descending priority, then lower power
    tasks_sorted = sorted(tasks, key=lambda t: (-t['priority'], t['power']))
    selected = []
    P_used = 0.0
    for t in tasks_sorted:
        # skip if pointing conflict
        if pointing_locked and t['requires_pointing']:
            continue
        # enforce power constraint
        if P_used + t['power'] <= P_avail:
            selected.append(t['id'])
            P_used += t['power']
    return selected

# example usage
tasks = [{'id':'cam', 'power':25.0, 'priority':10, 'requires_pointing':True},
         {'id':'xmit', 'power':40.0, 'priority':8,  'requires_pointing':False},
         {'id':'rad', 'power':10.0, 'priority':5,  'requires_pointing':False}]
active = select_tasks(tasks, P_avail=50.0, pointing_locked=False)
# active now lists scheduled tasks for the time slot