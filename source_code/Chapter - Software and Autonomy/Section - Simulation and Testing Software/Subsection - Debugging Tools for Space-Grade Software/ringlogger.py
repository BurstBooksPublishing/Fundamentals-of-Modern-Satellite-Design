# Simple flight logger: circular buffer, checksum, monotonic counter.
import struct, time, zlib

class FlightLogger:
    def __init__(self, capacity_bytes):           # allocate raw buffer
        self.buf = bytearray(capacity_bytes)
        self.size = capacity_bytes
        self.head = 0
        self.tail = 0
        self.counter = 0

    def _write_raw(self, data):                  # low-level write with wrap
        n = len(data)
        end = (self.head + n) % self.size
        if end >= self.head:
            self.buf[self.head:end] = data
        else:
            part = self.size - self.head
            self.buf[self.head:] = data[:part]
            self.buf[:end] = data[part:]
        self.head = end

    def log_event(self, msg_type, payload):      # msg_type: 1 byte, payload: bytes
        ts = int(time.time() * 1e6)              # microsecond timestamp
        hdr = struct.pack('<BQI', msg_type, ts, self.counter)
        self.counter += 1
        chk = zlib.crc32(hdr + payload) & 0xffffffff
        record = hdr + struct.pack('<I', chk) + payload
        self._write_raw(record)                  # overwrite oldest if needed
        # minimal ISR-safe operation: avoid mallocs, use preallocated payloads