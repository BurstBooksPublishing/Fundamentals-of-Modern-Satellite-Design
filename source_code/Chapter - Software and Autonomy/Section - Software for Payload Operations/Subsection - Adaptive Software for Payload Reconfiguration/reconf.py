# state: s dict with keys 'E', 'T', 'attitude_ok', 'queued_data'
# actions: list of action dicts with keys 'id','power','thermal_delta','reward','duration'
def feasible(s, a, dt=60):
    # energy check
    E_next = s['E'] - a['power']*dt + s['solar_power']*dt
    if E_next < s['E_min']: return False
    # thermal check
    T_next = s['T'] + a['thermal_delta']
    if T_next < s['T_min'] or T_next > s['T_max']: return False
    # attitude check
    if a.get('requires_attitude') and not s['attitude_ok']: return False
    # downlink check (simple heuristic)
    if s['queued_data'] + a.get('data_generated',0) > s['downlink_capacity']*s['next_window_hours']: return False
    return True

def select_action(s, actions):
    # compute utility per joule
    cand = [(a['reward']/(a['power']+1e-6), a) for a in actions if feasible(s,a)]
    if not cand: return None
    return max(cand, key=lambda x: x[0])[1]

# main loop (executed periodically)
while True:
    s = read_state()              # sensor fusion
    actions = get_candidate_actions()
    a = select_action(s, actions)
    if a:
        execute(a)                # apply and start telemetry logging
    sleep(30)                     # periodic cycle