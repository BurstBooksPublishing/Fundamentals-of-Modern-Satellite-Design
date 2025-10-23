import math
# Constants
eps0=8.854e-12      # F/m
e=1.602176634e-19   # C
m_xe=131.293/6.022e26  # kg per atom (Xenon)
rho_mo=10.28e3      # kg/m^3 (molybdenum)
M_xe=131.293e-3     # kg/mol
N_A=6.02214076e23

# Input design params
V=1000.0            # acceleration voltage (V)
d=0.003             # grid spacing (m)
ra=0.002            # aperture radius (m)
Y=0.05              # sputter yield atoms/ion (estimate)
tau=0.65            # transparency (fraction open area)

# Child-Langmuir current density (A/m^2)
J_CL=(4/9)*eps0*math.sqrt(2*e/m_xe)*(V**1.5)/(d**2)

# Aperture area and per-aperture current
A_ap=math.pi*ra**2
I_ap=J_CL*A_ap

# Thrust per aperture (N)
T_ap=I_ap*math.sqrt(2*m_xe*V/e)

# Erosion thickness rate (m/s) from Eq. (erosion)
h_dot=Y*J_CL*M_xe/(e*rho_mo*N_A)  # m/s

# Print compact results (inline comments show units)
print("J_CL (A/m^2) =", J_CL)
print("I_ap (A) =", I_ap)
print("T_ap (N) =", T_ap)
print("h_dot (m/yr) =", h_dot*3600*24*365)  # convert to m/yr