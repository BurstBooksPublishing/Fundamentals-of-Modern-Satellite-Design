#include "soc_hal.h" // HAL for SoC/FPGA interfaces (space-qualified)
#define FRAME_SIZE      1024*1024  /* bytes per frame */
#define FLASH_SLOT_BASE 0x10000000 /* flash partition base address */
volatile dma_desc_t *dma = DMA_DESC_BASE; // DMA descriptor table (hw)
uint32_t frame_idx = 0;
while (mission_active()) {
    // Kick FPGA to start streaming into RAM via DMA (non-blocking).
    dma_start_transfer(dma, FRAME_SIZE);
    // Poll or wait on interrupt for DMA completion.
    if (!dma_wait_complete(dma, TIMEOUT_MS)) { handle_error(); continue; } // # SEE handling
    // Minimal integrity check: CRC (hardware accelerator).
    if (!crc_verify(dma->dest_addr, FRAME_SIZE)) { mark_bad(frame_idx); continue; }
    // Copy to flash with ECC-aware write; asynchronous write uses QoS.
    flash_async_write(FLASH_SLOT_BASE + frame_idx*FRAME_SIZE, dma->dest_addr, FRAME_SIZE);
    frame_idx++;
    // Manage storage wrap and telemetry summary every N frames.
    if ((frame_idx & 0xFF) == 0) telemetry_report(frame_idx);
}