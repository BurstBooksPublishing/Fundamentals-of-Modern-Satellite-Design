import math
# mission parameters (example values to replace with measured data)
flux = 1e-3          # particles/cm^2/s incident on device
cross_section = 1e-6 # cm^2 per memory word
words = 1e6          # number of words in memory
target_prob = 1e-6   # allowable prob of uncorrected error per scrub

# compute upset rate per word and for whole memory (eq. R = Phi * sigma)
rate_per_word = flux * cross_section               # upsets/s/word
total_rate = rate_per_word * words                 # upsets/s memory-wide

# scrubbing interval to keep Poisson prob below target
# P(no. upsets >=1) = 1 - exp(-total_rate * T) <= target_prob
if total_rate > 0:
    scrub_interval = -math.log(1 - target_prob) / total_rate
else:
    scrub_interval = float('inf')

print("Total upset rate (per day):", total_rate * 86400)
print("Recommended scrub interval (s):", scrub_interval)