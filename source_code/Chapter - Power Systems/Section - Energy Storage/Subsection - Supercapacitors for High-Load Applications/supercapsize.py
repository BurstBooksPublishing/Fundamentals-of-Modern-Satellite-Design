# Inputs: mission pulse and cell spec
E_pulse = 2000.0        # J, pulse energy required
V1 = 32.0               # V, charge voltage
V2 = 24.0               # V, minimum allowed voltage after pulse
I_peak = 100.0          # A, peak pulse current
deltaV_allowed = 2.0    # V, acceptable bus sag due to ESR
cell_cap = 500.0        # F, single cell capacitance (example)
cell_volt = 2.7         # V, single cell nominal voltage
cell_esr = 0.005        # ohm, single cell ESR

# Compute required capacitance
C_req = 2.0*E_pulse/(V1*V1 - V2*V2)
ESR_max = deltaV_allowed / I_peak

# Series cells to reach V1
n_series = int((V1 + cell_volt - 1e-9) // cell_volt)  # ceil without math.ceil for clarity
# Parallel strings to get required C and meet ESR
C_per_string = cell_cap / n_series
n_parallel = int((C_req + C_per_string - 1e-9) // C_per_string)  # ceil
ESR_string = cell_esr * n_series / n_parallel

print("# Results (approx):")
print("C_required (F):", C_req)            # capacitance needed
print("ESR_max (ohm):", ESR_max)           # allowable ESR
print("n_series:", n_series, "n_parallel:", n_parallel)
print("Estimated ESR (ohm):", ESR_string)  # estimated ESR of bank