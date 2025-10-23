/* main acquisition loop */
while (mission_running) {
  if (!health_check()) { enter_safe_mode(); continue; } // safety
  set_exposure_time(cfg.exposure_ms);                     // configure sensor
  trigger_exposure();                                     // hardware trigger
  wait_for_irq(EXPOSURE_COMPLETE);                        // deterministic wait
  dma_read(frame_buf, frame_size);                        // zero-copy read
  preprocess(frame_buf);                                  // dark/gain/cosmic removal
  compress(frame_buf, comp_buf, &comp_len, cfg.compression_mode); // adaptive
  packetize(comp_buf, comp_len, &pkt);                    // CCSDS-like packet
  pkt.crc = compute_crc(pkt.data, pkt.len);               // data integrity
  enqueue_telemetry(pkt);                                 // downlink queue
  log_metadata(&pkt.meta);                                // timestamp, attitude, temp
}