import time
from hil_api import GNSSReplayer, RFChannel, TelemetryClient  # test harness APIs

replayer = GNSSReplayer('/data/flight/gnss_record.rrt')  # replay file
rf = RFChannel()  # RF emulator
tm = TelemetryClient()  # telemetry interface

replayer.start()  # begin GNSS replay
rf.set_fade_profile('eclipse_fade', depth_db=20)  # simulate fade # short comment
time.sleep(5)  # allow system to react
rv = tm.get_param('nav_solution_status')  # read telemetry
assert rv == 'DEGRADED'  # expected degraded mode during fade
replayer.stop()  # end replay