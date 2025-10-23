import time
from heapq import heappush, heappop

# Task tuple: (deadline, -priority, est_compute_ms, task_id, func)
task_heap = []

def submit_task(deadline, priority, est_compute_ms, task_id, func):
    # push task; negative priority to make higher numbers run first
    heappush(task_heap, (deadline, -priority, est_compute_ms, task_id, func))

def run_scheduler(cpu_budget_ms):
    start = time.time()*1000  # ms
    while task_heap and (time.time()*1000 - start) < cpu_budget_ms:
        deadline, neg_prio, est_ms, tid, func = heappop(task_heap)
        now = time.time()*1000
        if now + est_ms > deadline:
            # preemptable safety action: defer or trigger supervisor action
            # minimal action: notify supervisor and skip task
            notify_supervisor(tid)  # small blocking call
            continue
        func()  # execute task; must be non-blocking and bounded
        # post-exec health check
        if not health_ok():
            trigger_safe_mode()  # immediate failover
            break

# example helper functions are mission-specific and validated