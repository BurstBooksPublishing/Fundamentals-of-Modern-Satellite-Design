import numpy as np
# predictor: previous pixel in scanline (simple causal predictor)
def predict(tile):
    # tile: HxW numpy array, dtype=int16 for radiometric fidelity
    pred = np.zeros_like(tile)
    pred[:,1:] = tile[:,:-1]  # left neighbor
    return tile - pred        # residuals

def golomb_rice_encode(residuals, k=2):
    # encode non-negative mapped residuals using Rice parameter k
    # residuals mapped to non-negative via signed-to-unsigned mapping
    u = (residuals << 1) ^ (residuals >> 15)  # small trick: map signed to unsigned
    q = u >> k
    r = u & ((1<<k)-1)
    # serialize unary for q and binary for r (conceptual; not bit-packed here)
    bits = []
    for qi, ri in zip(q.flat, r.flat):
        bits.append('0'*qi + '1')         # unary quotient
        bits.append(format(ri, f'0{k}b')) # remainder
    return ''.join(bits)                 # simple string payload (replace with bitstream)
# usage on a single band tile
tile = np.array([[100,101,103],[98,100,102]], dtype=np.int16)
res = predict(tile)
payload = golomb_rice_encode(res, k=2)  # payload ready for packetization