import math
# simple thermal resistance calculator (for trades)
def R_layer(thickness, k, area):
    return thickness/(k*area)  # Eq. (2)

# parameters (SI units)
P = 10.0             # W, hotspot power
area = 0.01          # m^2, heat-spreading area
tim_thick = 0.0005   # m
tim_k = 2.0          # W/mK, TIM
spreader_thick = 0.002  # m
spreader_k = 400.0      # W/mK, copper
pcb_thick = 0.001     # m
pcb_k = 0.3           # W/mK, FR4 (through-plane)
via_count = 200
via_dia = 0.0006      # m
via_area = math.pi*(via_dia/2)**2
via_total_area = via_count * via_area
via_thick = 0.001     # m (via length)
via_k = 400.0         # W/mK

R_tim = R_layer(tim_thick, tim_k, area)
R_spreader = R_layer(spreader_thick, spreader_k, area)
# via parallel with PCB through-plane: compute combined conductance
G_vias = via_total_area * via_k / via_thick
G_pcb = (area * pcb_k) / pcb_thick
R_pcb_parallel = 1.0 / (G_vias + G_pcb)
R_total = R_tim + R_spreader + R_pcb_parallel
deltaT = P * R_total
print(f"R_total = {R_total:.4e} K/W, ΔT = {deltaT:.2f} K")
# tweak parameters to explore trade-offs