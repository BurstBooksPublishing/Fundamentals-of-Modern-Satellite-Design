# Simple buck sizing and loss estimate (engineering tool)
Vin = 28.0           # bus voltage V
Vout = 5.0           # output voltage V
Iout = 10.0          # load current A
fs = 300e3           # switching frequency Hz
dI_frac = 0.2        # ripple fraction of Iout
dI = dI_frac * Iout  # ripple A
D = Vout / Vin
L = (Vin - Vout) * D / (fs * dI)  # from eq:inductor
# Estimate conduction loss (synchronous MOSFETs)
Rds_on_high = 20e-3  # high-Rds radiation-tolerant MOSFET ohm
D_sync = 1.0 - D
P_cond = Iout**2 * (Rds_on_high * (D + D_sync))  # crude
# Estimate switching loss
E_sw = 0.5 * Vin * 100e-9  # assume 100 ns effective transition energy J
P_sw = E_sw * fs
# Output capacitor estimate
dV = 50e-3
Cout = dI / (8 * fs * dV)
print(f"L = {L*1e6:.2f} uH, Cout = {Cout*1e3:.1f} mF")
print(f"P_cond ~ {P_cond:.2f} W, P_sw ~ {P_sw:.2f} W, Efficiency ~ {Vout*Iout/(Vout*Iout+P_cond+P_sw):.3f}")
# Note: refine with real device data, core loss models, and thermal analysis.