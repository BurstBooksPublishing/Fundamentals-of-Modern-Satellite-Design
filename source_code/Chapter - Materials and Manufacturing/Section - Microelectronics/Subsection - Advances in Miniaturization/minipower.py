# Simple SoC power and thermal estimator (for early design trades)
def soc_power(C, V, f, I_leak):
    # dynamic + static power (Watts)
    return C*(V**2)*f + I_leak*V

def junction_temp(P, theta_ja, T_ambient):
    # steady-state junction temperature (degC)
    return T_ambient + P*theta_ja

# Example parameters: LEO image-processing SoC
C = 1e-9         # switched capacitance (F)
V = 1.0          # supply voltage (V)
f = 500e6        # clock freq (Hz)
I_leak = 1e-3    # leakage current (A)
theta_ja = 25.0  # thermal resistance (degC/W)
T_ambient = -20  # panel-facing ambient temp in LEO (degC)

P = soc_power(C, V, f, I_leak)               # compute power
Tj = junction_temp(P, theta_ja, T_ambient)   # compute junction temp

print(f"Power: {P:.2f} W  Junction temp: {Tj:.1f} °C")  # brief output