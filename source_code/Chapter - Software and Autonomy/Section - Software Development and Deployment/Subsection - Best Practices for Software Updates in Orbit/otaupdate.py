def activate_update(manifest_path, inactive_bank, timeout=300):
    # load manifest (contains image_hash and signature)
    manifest = load_manifest(manifest_path)
    # verify manifest signature with root public key
    if not verify_signature(manifest.signature, manifest.payload):
        raise SecurityError("Manifest signature failed")
    # validate full image hash after all chunks written
    image_hash = compute_hash(inactive_bank.image_path)  # flash readback
    if image_hash != manifest.image_hash:
        raise IOError("Image hash mismatch")
    # set new boot pointer atomically (update metadata with checksum)
    write_boot_metadata(inactive_bank.id, metadata_checksum=True)
    # start watchdog and monitor health for timeout seconds
    start_time = time.time()
    while time.time() - start_time < timeout:
        if system_health_ok():  # checks sensors, comms, attitude control
            return True  # update active and healthy
        time.sleep(5)  # poll interval
    # if health criteria not met, revert boot metadata atomically
    write_boot_metadata(inactive_bank.previous_id, metadata_checksum=True)
    return False  # activation failed, rollback initiated