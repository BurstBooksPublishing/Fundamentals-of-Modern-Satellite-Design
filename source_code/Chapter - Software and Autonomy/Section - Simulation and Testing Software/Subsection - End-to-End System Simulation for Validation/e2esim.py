# e2e_sim.py -- simplified example for validation pipelines
import numpy as np
from modules.orbit import Propagator            # orbital dynamics module
from modules.aocs import AttitudeSystem         # AOCS dynamics + control
from modules.rf import RFChannel                # link budget + PHY model
from modules.payload import ImageSensor         # sensor + compression
from modules.software import AutonomyStack      # onboard software tasks
from modules.hil import HILInterface            # optional HIL hooks

np.random.seed(42)                              # deterministic sampling

sim = Simulation()                              # event-driven sim controller
prop = Propagator(initial_state)                # J2, drag, etc.
aocs = AttitudeSystem(inertia, sensors)         # reaction wheels, magnetorquers
rf = RFChannel(antenna_pattern, gs_coords)      # path loss, fade models
payload = ImageSensor(resolution, frame_rate)   # produces frames
sw = AutonomyStack(task_set, scheduler)         # FDIR, compression decisions

for t in sim.time_iterator(duration):
    state = prop.step(t)                        # update orbit
    att = aocs.step(state, commands)            # AOCS dynamics
    frame = payload.capture(att)                # image capture
    decision = sw.execute(frame, att)           # onboard processing
    pkt_batch = sw.packetize(decision)          # create packets
    pr = rf.transmit(pkt_batch, att, t)         # PHY + link model
    sim.log_metrics(t, pr, decision)            # store metrics

    if HILInterface.enabled:                     # optional hardware calls
        HILInterface.sync_step(t)               # real-time hardware exchange