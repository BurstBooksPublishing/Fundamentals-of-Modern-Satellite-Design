void dsp_task(void *arg) {
    while (1) {
        wait_for_dma_buffer(&buf);            // block until buffer ready
        fix_scale_cplx(buf, &scaled, SCALE); // fixed-point normalization
        fft_execute(&scaled, &spec);         // spectrum for channel estimation
        eq_apply(&spec, &equalized);         // complex FIR equalizer
        demodulate(&equalized, &bits);       // symbol -> soft bits
        ldpc_decode(&bits, &payload);        // heavy FEC decode (iterative)
        package_and_send(payload);           // downlink or onboard routing
        telemetry_update_stats();            // CPU load, BER, temp
    }
}