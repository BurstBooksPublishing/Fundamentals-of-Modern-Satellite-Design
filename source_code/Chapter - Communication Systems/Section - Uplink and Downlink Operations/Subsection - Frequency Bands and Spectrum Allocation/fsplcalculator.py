import math

c = 299792458.0  # speed of light (m/s)

def fspl_db(range_m, freq_hz):
    # free-space path loss in dB
    return 20*math.log10(4*math.pi*range_m*freq_hz/c)

def required_bandwidth(data_rate_bps, spectral_eff_bits_per_hz):
    # required RF bandwidth in Hz
    return data_rate_bps / spectral_eff_bits_per_hz

def dish_gain_db(diameter_m, freq_hz, eff=0.6):
    # aperture gain (dBi) for circular dish
    wavelength = c/freq_hz
    gain = eff*(math.pi*diameter_m/wavelength)**2
    return 10*math.log10(gain)

# Example: LEO downlink 1 Gbps at 20 GHz, 600 km slant
R = 600e3
f = 20e9
print("FSPL (dB):", fspl_db(R, f))
print("Required BW (MHz):", required_bandwidth(1e9, 4)/1e6)  # 4 b/s/Hz efficiency
print("Dish gain (dBi) 0.6 eff, 0.5 m dia:", dish_gain_db(0.5, f))