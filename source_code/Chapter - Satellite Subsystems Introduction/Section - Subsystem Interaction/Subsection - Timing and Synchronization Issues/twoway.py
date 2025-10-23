def compute_offset(t1, t2, t3, t4):
    # t1: master send time (master clock)
    # t2: slave receive time (slave clock)
    # t3: slave send time (slave clock)
    # t4: master receive time (master clock)
    # offset: slave_time - master_time
    offset = 0.5 * ((t2 - t1) - (t4 - t3))
    # round-trip delay estimate for diagnostics
    rtt = (t4 - t1) - (t3 - t2)
    return offset, rtt

# Example: apply correction to local clock control loop
off, rtt = compute_offset(t1, t2, t3, t4)
# apply small-step correction to avoid discontinuities
clock_adjust = lowpass_filter(off)  # hardware control loop
apply_dac_to_vco(clock_adjust)       # adjust oscillator control voltage