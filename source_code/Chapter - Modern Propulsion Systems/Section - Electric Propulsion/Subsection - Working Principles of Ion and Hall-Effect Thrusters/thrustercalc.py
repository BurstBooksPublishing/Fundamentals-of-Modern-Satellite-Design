# Simple calculator: compute thrust, Isp for given input power and accel voltage
import math
e = 1.602e-19            # elementary charge, C
m_xe = 2.18e-25          # xenon atom mass, kg (~131 u)
g0 = 9.80665             # m/s^2

P = 2000.0               # input power, W (example GEO electric orbit-raise)
eta = 0.65               # overall efficiency (typical gridded ion)
V_acc = 20000.0          # acceleration voltage, V
# exhaust velocity from acceleration (ideal)
v_e = math.sqrt(2*e*V_acc/m_xe)
Isp = v_e/g0
# thrust from P and eq (7)
T = 2*eta*P / v_e
# beam current from eq (2) rearranged
I_b = (T/math.sqrt(2*m_xe*V_acc/e))  # A
print(f"v_e={v_e:.0f} m/s, Isp={Isp:.0f} s, Thrust={T:.3f} N, Beam current={I_b:.3f} A")
# # Comments: use these outputs to size propellant feed and power conditioning.