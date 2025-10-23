# Simple satellite power flow evaluator (replace with vendor data)
loads = [120.0, 250.0, 5000.0]   # watts: comm, avionics, payload
Vbus = 100.0                     # bus voltage volts
R_run = 0.01                     # feed resistance ohms
eff_dict = {120:0.95,250:0.92,5000:0.90}  # converter efficiencies

P_total = sum(loads)
I_bus = P_total / Vbus           # total bus current
P_loss_conduct = (P_total / Vbus)**2 * R_run  # I^2R loss

conv_losses = 0.0
for P in loads:
    eta = eff_dict[P]
    P_loss = (1.0/eta - 1.0) * P  # eq. (2)
    conv_losses += P_loss

# print results (replace with logging in production tools)
print(f"Bus current: {I_bus:.2f} A")
print(f"Distribution loss: {P_loss_conduct:.1f} W")
print(f"Converter losses: {conv_losses:.1f} W")
print(f"Total delivered+loss: {P_total+P_loss_conduct+conv_losses:.1f} W")