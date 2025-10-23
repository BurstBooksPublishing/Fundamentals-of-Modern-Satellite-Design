# compute heater duty cycle for steady-state and PID correction
Q_loss = 50.0            # W, predicted heat loss (e.g., during eclipse)
P_heater_max = 20.0      # W, single heater maximum power
pid_output = 0.3         # normalized PID command (-1..1)
# steady duty cycle to balance average loss
D_base = min(max(Q_loss / P_heater_max, 0.0), 1.0)
# apply PID correction (positive warms, negative cools)
D = min(max(D_base + pid_output * 0.2, 0.0), 1.0)
print(f"heater duty cycle = {D:.2f}")  # duty cycle fraction