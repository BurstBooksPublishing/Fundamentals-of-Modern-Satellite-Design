import numpy as np
# Parameters: mission_days, MTBFs in days, detection_delay in hours
mission_days=365.0
mtbf_transponder=2000.0
mtbf_rw=5000.0
detection_delay_hours=2.0
ntrials=20000

def sample_failure_time(mtbf):
    # exponential lifetime
    return np.random.exponential(mtbf)

def simulate_one():
    t_trans=sample_failure_time(mtbf_transponder)
    t_rw=sample_failure_time(mtbf_rw)
    # FDIR: if transponder fails, switch to backup instantly within detection_delay
    # If both transponders fail before detection, mission fails
    # Here we model single active + one backup (parallel redundancy)
    if t_trans>mission_days:
        return True  # no active failure
    # active trans failed at t_trans; assume backup has same MTBF; check backup lifetime
    t_backup=t_trans + sample_failure_time(mtbf_transponder)  # backup time since activation
    # detect and switch after delay
    if t_backup > t_trans + detection_delay_hours/24.0:
        # successful switchover if backup still alive until end of mission
        return t_backup > mission_days
    return False

# Monte Carlo loop
success=np.mean([simulate_one() for _ in range(ntrials)])
print("Estimated mission success probability:", success)