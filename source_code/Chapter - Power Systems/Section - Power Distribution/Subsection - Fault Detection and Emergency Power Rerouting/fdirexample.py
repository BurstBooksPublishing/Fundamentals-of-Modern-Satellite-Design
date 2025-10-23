# sample and buffers (Hall sensors, ADC)  # flight code uses RTOS timers
window = 50
threshold_gamma = 4.0
consec_limit = 3

def monitor_loop():
    buf = deque(maxlen=window)
    consec = 0
    while True:
        i = read_hall_current()            # read current (A)
        buf.append(i)
        mu = statistics.mean(buf)
        sigma = statistics.stdev(buf) if len(buf)>1 else 1e-3
        S = abs(i-mu)/sigma
        if S > threshold_gamma:
            consec += 1
        else:
            consec = 0
        if consec >= consec_limit:
            isolate_branch()               # open MOSFETs to suspected branch
            engage_reroute_template()      # enable alternate path via MOSFETs
            log_event("FDIR: reroute executed")
            consec = 0
        sleep(sample_interval)            # deterministic period