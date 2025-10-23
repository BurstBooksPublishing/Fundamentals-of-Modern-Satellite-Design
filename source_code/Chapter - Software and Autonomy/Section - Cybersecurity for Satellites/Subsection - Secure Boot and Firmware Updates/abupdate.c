int verify_and_activate(uint8_t *image, size_t len, uint8_t *sig) {
    // 1) Verify signature (returns 0 on success)
    if (ecdsa_verify(root_pubkey, sha256(image, len), sig) != 0) return -1;
    // 2) Check manifest monotonic counter (hardware-protected)
    if (read_monotonic() >= manifest_counter) return -2; // anti-rollback
    // 3) Write to inactive bank with ECC and CRC
    if (write_bank(INACTIVE_BANK, image, len) != 0) return -3;
    // 4) Set boot pointer to inactive bank and arm watchdog
    set_boot_bank(INACTIVE_BANK);
    arm_watchdog(WATCHDOG_TIMEOUT_MS); // revert if no commit
    // 5) Reboot to new image
    system_reboot();
    // After boot, code must call commit_update() to persist counter.
    return 0;
}