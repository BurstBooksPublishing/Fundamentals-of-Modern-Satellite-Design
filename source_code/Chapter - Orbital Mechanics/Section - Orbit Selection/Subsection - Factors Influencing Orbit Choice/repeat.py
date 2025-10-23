import math
# Constants
mu = 3.986004418e14        # Earth's GM, m^3/s^2
T_sidereal = 86164.0905    # sidereal day, s

def orbital_period(a_m):
    return 2*math.pi*math.sqrt(a_m**3/mu)  # Eq. (1)

# Example: LEO at 700 km altitude
R_earth = 6371000.0
alt = 700000.0
a = R_earth + alt
T = orbital_period(a)  # seconds

# Check repeat track for n orbits in m sidereal days
n = 15  # candidate orbits per repeat
m = 1   # days
repeat_error = abs(n*T - m*T_sidereal)  # seconds
print(f"Period: {T/60:.2f} min, repeat error: {repeat_error:.1f} s")
# If repeat_error small relative to T, a repeat-ground-track is feasible.