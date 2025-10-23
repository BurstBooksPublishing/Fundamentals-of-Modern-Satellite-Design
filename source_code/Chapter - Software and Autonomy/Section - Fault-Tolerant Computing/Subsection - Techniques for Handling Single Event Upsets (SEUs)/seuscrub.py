import time
# read_ecc_status(), scrub_block(), reboot_system() are platform APIs

SCRUB_INTERVAL = 60  # seconds, chosen from Eq. (2)
ERROR_THRESHOLD = 5   # persistent corrections before escalation

def scrub_loop():
    persistent_count = 0
    while True:
        for block in iterate_memory_blocks():             # iterate DDR regions
            status = read_ecc_status(block)              # returns corrected/uncorrected counts
            if status.uncorrected > 0:
                log_event('UNCORRECTED', block, status)  # record for telemetry
                trigger_failover(block)                  # switch to redundant region
                reboot_system()                          # last-resort recovery
            if status.corrected > 0:
                persistent_count += 1
                log_event('CORRECTED', block, status)
                scrub_block(block)                       # proactively rewrite corrected data
            else:
                persistent_count = 0
            if persistent_count >= ERROR_THRESHOLD:
                log_event('PERSISTENT_ERRORS', block, persistent_count)
                trigger_redundancy()                     # move critical tasks to backup
        time.sleep(SCRUB_INTERVAL)                        # background interval control

# start scrub daemon
if __name__ == '__main__':
    scrub_loop()