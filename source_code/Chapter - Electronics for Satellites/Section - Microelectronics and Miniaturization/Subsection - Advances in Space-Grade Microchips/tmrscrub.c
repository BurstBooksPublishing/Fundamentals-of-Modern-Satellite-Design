#include <stdint.h>
#define SCRUB_INTERVAL_MS 10000  // scrub every 10 s (example)

// simple majority vote for 32-bit words
uint32_t tmr_vote(uint32_t a, uint32_t b, uint32_t c){
    // return bitwise majority; protects against single-bit upsets
    return (a & b) | (b & c) | (a & c);
}

// stub: check and correct memory with ECC (implementation hardware-assisted)
void scrub_memory_region(uint32_t *addr, size_t words){
    for(size_t i=0;i<words;i++){
        // read word, check ECC, correct if single-bit error detected
        // hardware ECC routine assumed; minimal software fallback present
        uint32_t word = addr[i]; // read (may trigger cached ecc check)
        // perform ECC check/correct via hw or SW routine (omitted)
        addr[i] = word; // write-back corrected word
    }
}

int main(void){
    uint32_t core1, core2, core3; // outputs from three redundant pipelines
    while(1){
        // compute control decision across three redundant instances
        core1 = compute_pipeline_instance(1); // // instance 1
        core2 = compute_pipeline_instance(2); // // instance 2
        core3 = compute_pipeline_instance(3); // // instance 3
        uint32_t voted = tmr_vote(core1, core2, core3);
        actuate(voted); // send to ADCS actuator controller

        if(time_since_last_scrub() >= SCRUB_INTERVAL_MS){
            scrub_memory_region(ground_truth_section(), ground_words());
            reset_scrub_timer();
        }
    }
}