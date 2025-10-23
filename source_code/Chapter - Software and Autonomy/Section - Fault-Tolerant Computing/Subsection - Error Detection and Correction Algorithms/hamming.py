# Encode 4-bit data into 7-bit Hamming(7,4) word.
def encode(data):              # data: 4-bit list [d3,d2,d1,d0]
    d = data
    p1 = d[0] ^ d[1] ^ d[3]    # parity bit 1
    p2 = d[0] ^ d[2] ^ d[3]    # parity bit 2
    p3 = d[1] ^ d[2] ^ d[3]    # parity bit 3
    return [p1,p2,d[0],p3,d[1],d[2],d[3]]

# Decode and correct single-bit errors using syndrome lookup.
def decode(rx):               # rx: 7-bit list
    # parity checks
    s1 = rx[0] ^ rx[2] ^ rx[4] ^ rx[6]
    s2 = rx[1] ^ rx[2] ^ rx[5] ^ rx[6]
    s3 = rx[3] ^ rx[4] ^ rx[5] ^ rx[6]
    syndrome = (s3<<2) | (s2<<1) | s1
    if syndrome != 0:
        pos = syndrome - 1    # position to flip (0-indexed)
        rx[pos] ^= 1          # correct single-bit error
    # extract data bits
    return [rx[2], rx[4], rx[5], rx[6]]
# Note: production code must handle multiple errors, logging, and CRC.