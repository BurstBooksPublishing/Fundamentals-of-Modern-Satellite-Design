import numpy as np

# Polynomials in octal (constraint length 7): 171,133 typical
G = (0o171, 0o133)
K = 7
N = len(G)  # output bits per input bit

def encode(bits):
    state = 0
    out = []
    for b in bits:
        state = ((state << 1) | (b & 1)) & ((1 << (K-1)) - 1)
        for g in G:
            # compute output bit = parity(state & g)
            out.append(bin(state & g).count("1") & 1)
    return np.array(out, dtype=int)

def viterbi_decode(rx_bits):  # rx_bits: hard decisions 0/1 for prototype
    nstates = 1 << (K-1)
    path_metric = np.full(nstates, 1e9)
    path_metric[0] = 0
    paths = {s: [] for s in range(nstates)}
    for i in range(0, len(rx_bits), N):
        rx = rx_bits[i:i+N]
        new_metric = np.full(nstates, 1e9)
        new_paths = {}
        for s in range(nstates):
            if path_metric[s] >= 1e9: continue
            for bit in (0,1):
                ns = ((s << 1) | bit) & (nstates-1)
                out = []
                tmp = ((s << 1) | bit)
                for g in G:
                    out.append(bin(tmp & g).count("1") & 1)
                metric = path_metric[s] + np.sum(np.abs(out - rx))  # Hamming metric
                if metric < new_metric[ns]:
                    new_metric[ns] = metric
                    new_paths[ns] = paths[s] + [bit]
        path_metric = new_metric
        paths = new_paths
    # choose best end state
    best_state = int(np.argmin(path_metric))
    return np.array(paths.get(best_state, []), dtype=int)

# Example use: encode, add bit flips, decode
msg = np.random.randint(0,2,100)
tx = encode(msg)
rx = tx.copy()
rx[::50] ^= 1  # inject sparse errors
dec = viterbi_decode(rx)
# compare msg and dec where lengths match
print("Bit errors:", np.sum(msg[:len(dec)] != dec))