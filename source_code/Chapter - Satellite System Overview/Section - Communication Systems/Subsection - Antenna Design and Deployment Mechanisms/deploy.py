# Simplified pseudo-code for deployment sequence and telemetry checks
def deploy_antenna(hw, telemetry, timeout=600):
    # hw: hardware interface; telemetry: downlink object
    if not hw.power_on():                        # ensure power
        raise RuntimeError("Power failure")
    if hw.latch_status() == "released":
        return True                              # already deployed
    hw.enable_heaters()                          # prevent cold stiction
    hw.start_motor(speed=0.5)                    # slow start for safety
    start = time.time()
    while time.time() - start < timeout:
        pos = hw.encoder_read()                  # encoder feedback
        telemetry.report({'pos': pos})           # send minimal telemetry
        if hw.limit_switch():                    # reached end stop
            hw.motor_stop()
            hw.lock_clamp()
            # RF commissioning check
            s11 = hw.vna_measure(freq=hw.operating_freq)
            if s11 < -10:                        # example pass threshold
                telemetry.report({'deploy':'ok','s11':s11})
                return True
            else:
                telemetry.report({'deploy':'partial','s11':s11})
                # attempt tensioning retry
                hw.tension_boom(delta=0.1)
        if hw.motor_error():
            hw.motor_stop()
            telemetry.report({'error':'motor_fault'})
            return False
        time.sleep(1)
    hw.motor_stop()
    telemetry.report({'error':'timeout'})
    return False