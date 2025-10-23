/* Periodic MPPT tick (called at fixed dt) */
void mppt_tick(void) {
    // read sensors (radiation-hardened ADCs)
    float Vpv = adc_read(V_PV);     // PV voltage
    float Ipv = adc_read(I_PV);     // PV current
    float Vbat = adc_read(V_BAT);   // battery voltage
    float Tbat = adc_read(T_BAT);   // battery temp

    float Pnow = Vpv * Ipv;
    // MPPT perturb & observe
    static float Pprev=0, Vprev=0;
    float dP = Pnow - Pprev;
    float dV = Vpv - Vprev;

    if (fabs(dP) < P_NOISE_THRESH) {
        // small change: hold
    } else if ((dP>0 && dV>0) || (dP<0 && dV<0)) {
        duty += DUTY_STEP; // move further in same direction
    } else {
        duty -= DUTY_STEP; // reverse direction
    }
    // enforce duty limits for topology
    duty = clamp(duty, DUTY_MIN, DUTY_MAX);

    // battery safety and current limit
    float Ireq = (Pnow * efficiency_est - Pload()) / max(Vbat, Vbat_min);
    float Imax = batt_current_limit(Vbat, Tbat); // chemistry-specific
    float Icmd = fmin(Ireq, Imax);

    // translate current command to duty via converter model
    duty = map_current_to_duty(Icmd, Vpv, Vbat);

    // hardware update (redundant write and CRC)
    pwm_update(duty);
    telemetry_log(Pnow, Vbat, Icmd);

    Pprev = Pnow; Vprev = Vpv;
}