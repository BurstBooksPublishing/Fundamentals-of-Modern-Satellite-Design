# mcs_table: list of tuples (name, spectral_efficiency, per_curve_fn)
# per_curve_fn(snr) returns estimated PER at given SNR (dB)
def select_mcs(snr_db, mcs_table, per_target=1e-3, margin_db=1.5):
    # choose highest efficiency MCS with PER <= target after margin
    best = mcs_table[0]
    for mcs in mcs_table:
        per = mcs[2](snr_db - margin_db)          # apply margin
        if per <= per_target and mcs[1] > best[1]:
            best = mcs
    return best

# Example usage in frame loop
for frame in frames_from_demod():                       # pilot-derived SNR per frame
    snr_db = frame.estimated_snr_db                     # fast SNR estimate
    selected_mcs = select_mcs(snr_db, mcs_table)        # choose MCS
    send_control_command(selected_mcs[0])               # signal to transmitter
    schedule_payload(selected_mcs)                      # set coder/modulator parameters