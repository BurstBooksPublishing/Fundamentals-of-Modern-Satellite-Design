# node.run() - main loop (simplified)
import time, hashlib

def digest(state):                              # small digest to compare outputs
    return hashlib.sha256(repr(state).encode()).hexdigest()

def send_heartbeat(peers, node_id, state):      # broadcast heartbeat with digest
    msg = {'id': node_id, 'time': time.time(), 'digest': digest(state)}
    for p in peers: p.send(msg)                  # network send (authenticated)

def receive_peers(peers):                       # collect peer messages in window
    msgs = []
    start = time.time()
    while time.time() - start < WINDOW:
        msgs.extend(peers.poll())                # non-blocking poll
    return msgs

def local_isolation(node_id, state, peers):
    send_heartbeat(peers, node_id, state)
    msgs = receive_peers(peers)
    counts = {}                                  # digest -> count
    for m in msgs:
        counts[m['digest']] = counts.get(m['digest'],0) + 1
    myd = digest(state)
    # majority check
    if counts.get(myd,0) < (len(peers)+1)//2:    # +1 includes self
        suspect_node = detect_deviator(msgs)     # simple majority deviator detection
        quarantine(suspect_node)                 # isolate and notify ground
    # minimal inline comments; real code includes retries, auth, and logging.