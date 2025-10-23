# Compute raw data rate and storage needs for ADC streams
def adc_data_requirements(bits_per_sample, sample_rate_hz, channels, duration_s,
                          coding_overhead=1.1):
    # bits_per_sample: integer bits per sample
    # sample_rate_hz: per-channel sampling frequency
    # channels: number of parallel ADC channels
    raw_rate_bps = bits_per_sample * sample_rate_hz * channels
    # include protocol/ID/ECC overhead
    total_rate_bps = raw_rate_bps * coding_overhead
    storage_bytes = total_rate_bps * duration_s / 8.0
    return total_rate_bps, storage_bytes

# Example: 12-bit, 20 MSPS, 4 channels, 600 s collection
rate, storage = adc_data_requirements(12, 20e6, 4, 600)
print("Required link rate (bps):", rate)        # inline comment: check downlink capacity
print("Storage required (MiB):", storage / (1024**2))  # inline comment: on-board buffer sizing