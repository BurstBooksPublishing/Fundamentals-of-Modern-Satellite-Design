# Simple CRC-16-CCITT implementation (suitable for onboard telemetry checks).
POLY = 0x1021
def crc16_ccitt(data: bytes, init: int = 0xFFFF) -> int:
    crc = init
    for b in data:
        crc ^= (b << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) & 0xFFFF) ^ POLY
            else:
                crc = (crc << 1) & 0xFFFF
    return crc
# Example: attach CRC to frame before downlink.
# frame_with_crc = frame + crc16_ccitt(frame).to_bytes(2,'big')