import time
import heapq

# Token-bucket parameters for downlink shaping (bytes/sec)
TOKEN_RATE = 5_000_000  # sustained downlink bandwidth
BUCKET_CAP = 10_000_000  # max burst capacity

# Priority queue: lower number = higher priority
queue = []  # heap of tuples (priority, timestamp, packet)

tokens = BUCKET_CAP
last_time = time.time()

def produce_packet(source, size, priority):
    # push a packet into the router queue
    heapq.heappush(queue, (priority, time.time(), {'src': source, 'size': size}))

def try_transmit():
    global tokens, last_time
    now = time.time()
    # refill tokens
    tokens = min(BUCKET_CAP, tokens + TOKEN_RATE * (now - last_time))
    last_time = now
    if not queue:
        return
    prio, ts, pkt = queue[0]
    if pkt['size'] <= tokens:
        heapq.heappop(queue)
        tokens -= pkt['size']
        transmit(pkt)  # replace with RF driver call

def transmit(pkt):
    # minimal placeholder for RF driver; block until tx completed.
    # In flight SW, use DMA and non-blocking APIs.
    print(f"TX {pkt['src']} {pkt['size']} bytes")
# -- example producers --
produce_packet('star_tracker', 64, 1)  # high-priority control data
produce_packet('camera', 2_000_000, 4)  # bulk payload
# main loop for HIL
for _ in range(10):
    try_transmit()
    time.sleep(0.1)