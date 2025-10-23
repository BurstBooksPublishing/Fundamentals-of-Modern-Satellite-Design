# Simple model: compute avg power and energy per orbit (example values).
def avg_power(P_active, P_sleep, D):
    return P_active*D + P_sleep*(1-D)

def energy_per_orbit(Pavg, orbit_sec=5400):
    return Pavg * orbit_sec  # joules per orbit

# Example parameters (replace with mission-specific numbers)
P_active = 8.0   # W when processing/tx active
P_sleep = 0.05   # W in low-power sleep
D = 0.15         # duty cycle
Pavg = avg_power(P_active, P_sleep, D)
Eorbit = energy_per_orbit(Pavg)
# Print results (in real use, feed into solar array and battery sizing)
print("Avg power: {:.2f} W, Energy per orbit: {:.0f} J".format(Pavg, Eorbit))