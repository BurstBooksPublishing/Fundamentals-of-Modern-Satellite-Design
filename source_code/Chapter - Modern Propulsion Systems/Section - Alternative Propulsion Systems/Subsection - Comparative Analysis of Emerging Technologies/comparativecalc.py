# compute accelerations and delta-v per day for sail, laser-beam, tether example
c = 3e8                # m/s
I = 1361               # W/m^2 at 1 AU
def sail_acc(A_over_m): return 2*I*A_over_m/c  # m/s^2
def laser_acc(P, mass): return 2*P/(c*mass)   # perfect reflector approximation
def dv_per_day(a): return a*86400             # m/s per day

# example parameters
A_over_m = 10.0        # m^2/kg
P_beam = 1e5           # W
mass = 100.0           # kg

a_sail = sail_acc(A_over_m)         # sail acceleration
a_laser = laser_acc(P_beam, mass)   # laser-driven acceleration

print("Sail a (m/s^2):", a_sail, "dv/day (m/s):", dv_per_day(a_sail))
print("Laser a (m/s^2):", a_laser, "dv/day (m/s):", dv_per_day(a_laser))
# note: tether force needs magnetic field and current model; not included here.