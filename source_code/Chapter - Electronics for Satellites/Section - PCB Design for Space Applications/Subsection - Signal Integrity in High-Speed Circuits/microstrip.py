import math
c = 299792458.0  # speed of light, m/s
def microstrip(Z_params):
    # Z_params: dict with keys w (m), h (m), t (m), eps_r, tand
    w, h, t = Z_params['w'], Z_params['h'], Z_params['t']
    eps_r, tand = Z_params['eps_r'], Z_params['tand']
    # effective permittivity approximate
    eps_eff = (eps_r + 1)/2 + (eps_r - 1)/2 * (1/math.sqrt(1 + 12*h/w))
    # characteristic impedance via Wheeler-like formula
    Z0 = 87.0/math.sqrt(eps_eff) * math.log(5.98*h/(0.8*w + t))
    # propagation delay per meter
    delay = 1.0/(c/math.sqrt(eps_eff))  # s/m
    # dielectric loss (neper/m) ~ (pi*f/c)*sqrt(eps_eff)*tan(delta)
    # return values
    return {'Z0': Z0, 'eps_eff': eps_eff, 'delay_s_per_m': delay, 'tand': tand}
# Example: Ka-band feedline trade (comments inline).
params = {'w':0.4e-3,'h':0.2e-3,'t':35e-6,'eps_r':2.2,'tand':0.0009}
print(microstrip(params))  # quick check for impedance and delay