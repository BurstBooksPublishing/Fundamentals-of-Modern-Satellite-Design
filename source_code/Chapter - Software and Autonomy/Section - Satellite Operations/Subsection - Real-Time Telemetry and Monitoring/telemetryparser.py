import struct, time, zlib
WINDOW=30  # seconds for rolling mean
THRESHOLD={'battery_voltage':11.5}  # V

# simple in-memory buffers; in production use async I/O and DB
buffers={'battery_voltage':[]}

def parse_packet(data):
    # header: 2B sync, 4B ts (uint32), 1B type, 2B len, payload..., 4B crc
    sync, ts, ptype, plen = struct.unpack('>2sI B H', data[:9])
    payload = data[9:9+plen]
    crc_recv = struct.unpack('>I', data[9+plen:13+plen])[0]
    if zlib.crc32(data[:9+plen]) & 0xFFFFFFFF != crc_recv:
        raise ValueError('CRC fail')
    return ts, ptype, payload

def demux_and_update(ts, ptype, payload):
    # example: ptype 1 -> battery telemetry: float32 voltage
    if ptype==1:
        voltage = struct.unpack('>f', payload)[0]
        buffers['battery_voltage'].append((ts, voltage))
        # prune old samples
        cutoff=ts-WINDOW
        buffers['battery_voltage']=[(t,v) for (t,v) in buffers['battery_voltage'] if t>=cutoff]

def check_alerts(now_ts):
    samples=buffers['battery_voltage']
    if not samples: return
    mean=sum(v for _,v in samples)/len(samples)
    if mean < THRESHOLD['battery_voltage']:
        print(f'ALERT {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now_ts))}: low battery mean={mean:.2f}V')

# main loop: replace with socket read in operations
while True:
    # data = recv_from_ground_station()
    # for demo, break
    break