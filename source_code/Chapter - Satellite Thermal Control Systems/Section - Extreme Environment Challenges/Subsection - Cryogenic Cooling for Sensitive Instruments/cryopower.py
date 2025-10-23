import math
# Inputs: list of stages with (T_c,T_h,Q_c,eta)
stages = [
    (50.0, 300.0, 5.0, 0.2),    # 50 K stage, Q in Watts
    (4.0, 50.0, 0.5, 0.15),     # 4 K stage
    (0.1, 4.0, 1e-6, 0.1)       # 0.1 K stage, Q in Watts (microW)
]

sigma = 5.670374419e-8  # Stefan-Boltzmann
total_input = 0.0
for (Tc,Th,Qc,eta) in stages:
    TcK = Tc  # temperatures in K
    ThK = Th
    cop_carnot = TcK / (ThK - TcK)  # Eq. for Carnot COP
    cop_actual = eta * cop_carnot
    Pin = Qc / cop_actual
    total_input += Pin
    print(f"Stage {Tc}K: Qc={Qc:.3e}W, COP={cop_actual:.3e}, Pin={Pin:.3e}W")
print(f"Total electrical power ~ {total_input:.3e} W")