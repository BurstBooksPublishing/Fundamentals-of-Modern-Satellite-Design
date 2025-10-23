import socket, time, struct
# connect to flight computer endpoint (HUT) -- emulated serial over TCP
HOST, PORT = '192.168.1.10', 5000
sock = socket.create_connection((HOST, PORT), timeout=1.0)

def generate_gyro_sample(t):
    # simple sinusoid representing spacecraft rotation rates (rad/s)
    import math
    return 0.01 * math.sin(2*math.pi*0.2*t)  # slow tumble

T_s = 0.05  # 20 Hz sample rate for ADCS
next_time = time.time()
try:
    while True:
        now = time.time()
        if now >= next_time:
            gyro = generate_gyro_sample(now)
            # send as 4-byte float, little-endian -- HUT expects this format
            sock.sendall(struct.pack('<f', gyro))
            # minimal latency measurement: request echo and time RTT
            t0 = time.time()
            echo = sock.recv(4)  # blocking; HUT must echo
            rtt = time.time() - t0
            # write log to disk or telemetry system (omitted)
            next_time += T_s
        else:
            time.sleep(max(0, next_time - now))
finally:
    sock.close()