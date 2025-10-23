def monitor_and_heal():
    # read condensed telemetry; low cpu, low memory
    telem = read_telemetry()                      # currents, temps, RF power
    flags = anomaly_detect(telem)                 # fast thresholds + EWMA
    if flags['critical']:                         # immediate hardware watchdog
        hw_watchdog.reset()                       # preserve control if possible
    if flags['sensor_drift']:
        adjust_operating_point()                  # reduce bias, lower power
        log_event('adjust')                       # tiny event log
    if flags['persistent_fault']:
        switch_to_redundant_path()                # hardware switch; safe check
        schedule_ground_contact(priority='high')  # request telemetry dump
    if flags['fpga_seu']:
        partial_reconfigure_fpga()                # atomic operation, idempotent
    # keep counters for recurrence; escalate to ground when threshold exceeded