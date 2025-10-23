import math
# Basic parameters (nominal values)
orbit_minutes = 95                   # orbit period
sunlit_minutes = 60                  # sunlit arc
payload_power = 150.0                # W when imaging
bus_power = 50.0                     # W baseline bus
solar_power_gen = 220.0              # W when sunlit at current attitude
batt_capacity_Wh = 200.0             # Wh
dod_max = 0.6                        # allowable DoD fraction
eta_dis = 0.9

# time discretization
dt_min = 1
soc = batt_capacity_Wh               # start fully charged (Wh)
reserve_Wh = batt_capacity_Wh*(1-dod_max)

for minute in range(orbit_minutes):
    sunlit = minute < sunlit_minutes
    # payload schedule: image only in sunlit arc, duty cycle 0.7
    payload_on = sunlit and ( (minute % 10) < 7 )  # simple duty pattern
    load_W = bus_power + (payload_power if payload_on else 0.0)
    gen_W = solar_power_gen if sunlit else 0.0
    net_W = gen_W - load_W
    # update SoC (convert W*min to Wh)
    soc += net_W*(dt_min/60.0)
    # simulate charge/discharge inefficiency
    if net_W < 0:
        soc -= ( -net_W*(dt_min/60.0) )*(1-eta_dis)  # account ineff loss
    # clamp SoC
    soc = max(0.0, min(batt_capacity_Wh, soc))
    if soc < reserve_Wh:
        print(f"Warning: SoC below reserve at minute {minute}, SoC={soc:.1f}Wh")
        break
else:
    print(f"Orbit complete. End SoC={soc:.1f}Wh")
# end of simulation