import math

k_db = -228.6                          # Boltzmann constant in dB W/K/Hz
def db(x): return 10*math.log10(x) if x>0 else -999
def linear(dbv): return 10**(dbv/10)

def link_budget(EIRP_dBW, G_over_T_dBK, path_loss_dB, data_rate_hz, bandwidth_hz=1.0):
    # Compute C/N0 (dB-Hz) using eq. (2)
    cn0_dBHz = EIRP_dBW + G_over_T_dBK - path_loss_dB - k_db
    # Eb/N0 in dB
    ebno_dB = cn0_dBHz - 10*math.log10(data_rate_hz)
    return cn0_dBHz, ebno_dB

# Example: GEO downlink, EIRP 40 dBW, G/T 10 dB/K, path loss 200 dB, data 100 Mbps
cn0, ebno = link_budget(40, 10, 200, 1e8)
print(f"C/N0 = {cn0:.1f} dB-Hz, Eb/N0 = {ebno:.1f} dB")  # simple output