from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# public key of operator (stored in secure element) -- load securely
pubkey_bytes = b'...'  # operator public key bytes
pubkey = Ed25519PublicKey.from_public_bytes(pubkey_bytes)

# received payload: signed_session = signature || session_info
signature = received[:64]               # Ed25519 signature bytes
session_info = received[64:]            # session metadata and salt

# verify signature (throws on failure)
pubkey.verify(signature, session_info)  # inline comment: signature check

# derive session key
salt = b'satellite-pass-2025'           # from session_info in practice
hk = HKDF(algorithm=hashes.SHA256(), length=16, salt=salt, info=b'cmd-session')
session_key = hk.derive(master_key)    # master_key in secure element

# verify an AES-GCM command
aesgcm = AESGCM(session_key)
nonce = cmd_packet[:12]                # 96-bit nonce
ciphertext = cmd_packet[12:-16]
tag = cmd_packet[-16:]
plaintext = aesgcm.decrypt(nonce, ciphertext+tag, associated_data=b'seq:123')
# process plaintext after monotonic seq verification