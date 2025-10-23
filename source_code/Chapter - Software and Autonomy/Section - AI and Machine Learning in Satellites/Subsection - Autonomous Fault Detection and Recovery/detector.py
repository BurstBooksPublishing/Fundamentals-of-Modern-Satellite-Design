# Minimal dependencies, integer-friendly ops for flight CPUs.
alpha = 0.2               # EWMA factor
h = 5.0                   # CUSUM threshold (tuned on-ground)
S = 0.0                   # cumulative statistic init
z = 0.0                   # EWMA init

def predict(sensor):      # simple physical predictor (placeholder)
    return sensor.prev_est  # use last good estimate

def recover(action_code):  # recovery action dispatcher
    if action_code == 1:
        # switch to redundant wheel, reduce torque commands
        send_cmd("switch_wheel")
    elif action_code == 2:
        # reduce payload duty cycle to save power
        send_cmd("payload_reduce")
    elif action_code == 3:
        # safe-hold orientation and notify ground
        send_cmd("enter_safe_hold")

def detect_and_recover(sensor):  # called at telemetry rate
    global S, z
    y = sensor.read()                    # current measurement
    y_hat = predict(sensor)              # model prediction
    r = y - y_hat                        # residual
    z = alpha * r + (1 - alpha) * z      # EWMA
    # approximate log-likelihood ratio with scaled residual
    llr = (r / sensor.sigma)**2 - 1.0
    S = max(0.0, S + llr)
    if S > h:
        # simple rule mapping residual to recovery
        if sensor.name == "reaction_wheel":
            recover(1)
        elif sensor.name == "battery_voltage":
            recover(2)
        else:
            recover(3)
        S = 0.0  # reset after action