# Simple power scheduler: PV, battery SOC, priority loads
import math
# Parameters (representative values)
Vbus = 28.0           # bus voltage (V)
Pv_max = 2000.0       # PV array max power (W)
eclipse_duration = 35*60  # eclipse seconds (typical LEO)
soc = 0.8             # initial state of charge (fraction)
C_batt = 100.0        # battery capacity (Ah)
DoD_min = 0.2         # minimum allowed state-of-charge
eff_bms = 0.9         # round-trip efficiency
# Define loads as (name, power_W, priority)
loads = [("ADCS", 150.0, 1), ("COMMS", 800.0, 1), ("Payload", 900.0, 2),
         ("Housekeeping", 50.0, 0)]
# Simple loop across orbit phases: sunlit and eclipse
def schedule(pv_power, soc):
    # Compute available power: PV first, then battery support
    total_load = sum(l[1] for l in loads)
    if pv_power >= total_load:
        # All loads on, charge battery with surplus
        return {l[0]:True for l in loads}, min(1.0, soc + (pv_power-total_load)/(Vbus*C_batt*3600.0))
    else:
        # PV insufficient: shed lower-priority loads
        # Sort loads by priority desc
        sorted_loads = sorted(loads, key=lambda x: x[2])
        enabled = {}
        remaining = pv_power
        for name,power,prio in sorted_loads:
            if remaining >= power:
                enabled[name]=True
                remaining -= power
            else:
                enabled[name]=False
        # Use battery if needed for critical loads
        required = sum(p for n,p,pr in loads if enabled.get(n,False))
        # If critical loads exceed PV, draw from battery
        return enabled, max(DoD_min, soc - (required - pv_power)/(Vbus*C_batt*3600.0)/eff_bms)
# Example: simulate eclipse (pv_power=0)
enabled, soc_after = schedule(0.0, soc)
# Print decision brief (would be telemetry in flight)
print(enabled, soc_after)  # e.g., COMMS may be shed to preserve SOC