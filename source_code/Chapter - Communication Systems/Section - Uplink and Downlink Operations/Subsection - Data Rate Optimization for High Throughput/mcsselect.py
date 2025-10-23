# mcs_table: list of tuples (name, snr_threshold_dB, spectral_efficiency_bits_per_Hz)
mcs_table = [("QPSK-1/2", -1.0, 1.0), ("8PSK-3/4", 4.0, 2.25), ("16QAM-3/4", 8.0, 3.0)]
def select_mcs(snr_dB, bandwidth_Hz):
    # choose highest-efficiency MCS with snr requirement met
    valid = [m for m in mcs_table if snr_dB >= m[1]]
    if not valid:
        return 0.0, "OUTAGE"  # no usable MCS
    best = max(valid, key=lambda x: x[2])
    throughput = best[2] * bandwidth_Hz  # bits per second
    return throughput, best[0]

# Example: estimate throughput for SNR time series during a 600s LEO pass
snr_samples_dB = [5.0, 7.0, 3.0, 9.5, 8.0]  # from link prediction model
bandwidth = 40e6  # 40 MHz per carrier
total_bits = 0.0
for snr in snr_samples_dB:
    tput, mcs = select_mcs(snr, bandwidth)
    total_bits += tput * 120.0  # 120 second sub-intervals
# total_bits is useful payload delivered during the pass