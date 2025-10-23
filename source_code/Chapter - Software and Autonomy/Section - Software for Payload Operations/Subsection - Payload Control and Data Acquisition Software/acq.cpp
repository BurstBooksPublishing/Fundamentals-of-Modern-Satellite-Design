#include <cstdint>
// Simplified RTOS task pseudocode for payload acquisition.
struct Packet { uint8_t header[16]; uint8_t *payload; size_t len; uint32_t crc; };

void acquisition_task() {
  while (true) {
    wait_for_schedule();             // blocking until next exposure time
    trigger_instrument();           // toggle FPGA line to start capture
    auto frame = read_frame_dma();  // non-blocking DMA into buffer
    if (!frame_valid(frame)) {      // quick integrity check
      log_event("frame_invalid");   // health telemetry
      attempt_recover();            // try reinit, up to N times
      continue;
    }
    auto compressed = compress_frame(frame); // FPGA or CPU compress
    Packet p = packetize_ccsds(compressed);  // add headers, seq, CRC
    enqueue_for_storage(p);         // write to ring buffer/flash
  }
}

// Telemetry manager sends stored packets during contact.
void telemetry_task() {
  while (communicating_with_ground()) {
    auto p = dequeue_for_downlink(); // CFDP aware
    send_packet(p);                  // driver-level send
    confirm_ack_or_schedule_retx(p);
  }
}