# Simple HIL control script (pseudocode) for test automation
from instruments import Shaker, ThermalChamber, TelemetryRecorder  # test-bench APIs

shaker = Shaker('/dev/shaker')               # connect to shaker controller
chamber = ThermalChamber('192.168.0.10')     # connect to thermal chamber
recorder = TelemetryRecorder('/data/test1')  # telemetry capture

try:
    chamber.set_profile([-40, 20, 60], dwell=3600)   # survival->operational cycle
    recorder.start()                                  # start telemetry logging
    for freq, level, duration in [(5, 2.0, 60), (50, 5.0, 300)]:  # sine then random
        shaker.ramp_to(freq, level)                   # frequency and g-level
        shaker.run(duration)                           # run for duration (s)
        if recorder.detect_anomaly():                  # quick health check
            shaker.abort(); chamber.abort()            # abort both systems
            raise RuntimeError('Anomaly detected during vibration')
    chamber.execute_profile()                          # run thermal profile
    recorder.stop()
except Exception as e:
    recorder.mark_failure(str(e))                      # annotate test record
    raise
finally:
    shaker.disconnect(); chamber.shutdown(); recorder.close()