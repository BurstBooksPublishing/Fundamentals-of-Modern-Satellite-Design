import hashlib, json
from ecdsa import SigningKey, NIST256p

# build leaf hashes (telemetry list)  # compact sample
telemetry = [{'t':1620000000,'m':b'\x01\x02'}, {'t':1620000001,'m':b'\x03\x04'}]
leaves = [hashlib.sha256(json.dumps(t).encode()).digest() for t in telemetry]

# compute Merkle root (simple pairwise)
def merkle_root(nodes):
    if len(nodes)==1: return nodes[0]
    next_level=[]
    for i in range(0,len(nodes),2):
        a=nodes[i]
        b=nodes[i+1] if i+1<len(nodes) else nodes[i]  # duplicate last if odd
        next_level.append(hashlib.sha256(a+b).digest())
    return merkle_root(next_level)

root = merkle_root(leaves)

# sign root with on-board private key (HSM interface would be used in flight)
sk = SigningKey.generate(curve=NIST256p)  # placeholder; use HSM in production
signature = sk.sign(root)

# block payload to transmit/anchor (compact)
block = {'root': root.hex(), 'ts':1620000002, 'sig': signature.hex()}
# transmit block to ground or propose to validators  # via ISL or downlink