#include <stdint.h>
#include "hw_timer.h"     // hardware timer API
#include "dram_ecc.h"     // ECC hw assist API
#include "watchdog.h"     // watchdog API

#define SCRUB_INTERVAL_MS 2000U   // set from Eq.(3) sizing
#define DRAM_REGION_ADDR   0x80000000U
#define DRAM_REGION_WORDS  (32*1024*1024/4) // 32 MiB region

void scrub_region(void) {
    volatile uint32_t *p = (uint32_t *)DRAM_REGION_ADDR;
    for (uint32_t i=0;i<DRAM_REGION_WORDS;i++) {
        uint32_t w = p[i];                  // read word (may trigger ECC)
        if (dram_ecc_error_detected()) {   // hw ECC flag
            dram_ecc_correct(i);           // attempt hardware correction
            log_event("ECC corrected", i); // minimal telemetry
        }
        watchdog_kick();                   // keep WDT happy during long ops
    }
}

void scrub_task(void *arg) {
    (void)arg;
    while (1) {
        scrub_region();                    // scrub pass
        hw_timer_sleep_ms(SCRUB_INTERVAL_MS);
    }
}

int main(void) {
    system_init();                         // clocks, power, peripherals
    watchdog_start(10000);                 // 10 s watchdog window
    hw_timer_create_task(scrub_task);      // start scrub in RTOS
    scheduler_start();
    return 0;
}