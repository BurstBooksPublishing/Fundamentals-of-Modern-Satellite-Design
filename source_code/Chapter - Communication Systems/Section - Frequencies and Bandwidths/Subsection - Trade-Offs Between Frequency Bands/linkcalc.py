import math

# Physics constants
c = 299792458.0               # m/s
R = 3.6e7                     # GEO slant range (m)
eta = 0.6                     # aperture efficiency

# frequencies to compare (Hz)
freqs = {'L':1.6e9, 'X':8.0e9, 'Ka':20e9}

# target antenna gain (dBi)
G_target = 40.0               # dBi

def fspl(f,R):
    return 20*math.log10(4*math.pi*R*f/c)

def dish_diameter_for_gain(G_dbi,f,eta):
    # from eq (gain): G_linear = 10^(G_dbi/10)
    G_lin = 10**(G_dbi/10.0)
    lam = c/f
    A = G_lin * lam**2 / (eta * math.pi)  # aperture area
    D = math.sqrt(4*A/math.pi)
    return D

for name,f in freqs.items():
    L_fs = fspl(f,R)
    D = dish_diameter_for_gain(G_target,f,eta)
    print(f"{name}-band: f={f/1e9:.2f} GHz, FSPL={L_fs:.1f} dB, D_for_{G_target}dBi={D:.2f} m")
# small comments: use these outputs to balance EIRP vs dish size in design