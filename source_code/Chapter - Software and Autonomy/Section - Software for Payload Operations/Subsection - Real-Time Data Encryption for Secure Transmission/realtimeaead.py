from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os

# Device long‑term key (secure element would hold this in flight)
priv = X25519PrivateKey.generate()
peer_pub_bytes = ...  # received from ground during contact (cert validated)

# ECDH to derive shared secret
peer_pub = X25519PrivateKey.from_public_bytes(peer_pub_bytes).public_key()
shared = priv.exchange(peer_pub)

# Derive symmetric AEAD key with HKDF
hkdf = HKDF(length=32, algorithm=hashes.SHA256(), salt=None, info=b"sat_payload_stream")
key = hkdf.derive(shared)              # 256-bit key
aead = ChaCha20Poly1305(key)

# Streaming encryption loop: chunk producer yields bytes objects
frame_counter = 0
for chunk in chunk_producer():         # chunk_producer yields MTU‑sized payloads
    nonce = frame_counter.to_bytes(12, 'big')  # 96-bit nonce
    aad = b"hdr:" + frame_metadata(chunk)      # authenticated header
    ct = aead.encrypt(nonce, chunk, aad)       # returns ciphertext||tag
    tx_buffer.write(nonce + ct)                # send nonce + AEAD output
    frame_counter += 1