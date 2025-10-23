def validate_hmac(tc_frame, key):                   # validate MAC
    # return True if HMAC valid
    return hmac_sha256(key, tc_frame.payload) == tc_frame.mac

def schedule_command(tc, uplink_manager):           # schedule or immediate
    if tc.time_tag:                                 # time-tagged execution
        uplink_manager.queue_timed(tc)
    else:
        uplink_manager.send_now(tc)

def uplink_and_confirm(tc, uplink_manager, telem_db):# send and await ack
    uplink_manager.send(tc)                         # send TC to station
    # wait for link-layer ACK (short timeout)
    if not uplink_manager.wait_for_ack(tc.id, timeout=30):
        raise RuntimeError("Uplink failed")
    # wait for execution confirmation telemetry (longer timeout)
    return telem_db.wait_for_confirmation(tc.id, timeout=600)

# Example usage
tc = compose_command('ANT_POINT', params)           # compose pointing TC
if validate_syntax(tc) and validate_constraints(tc):# ground-side checks
    sign_tc(tc, ground_key)                         # MAC/sign
    schedule_command(tc, uplink_mgr)                # schedule to uplink manager
    ok = uplink_and_confirm(tc, uplink_mgr, telem_db)
    if not ok:
        retry_with_backoff(tc)                      # simple retry strategy