import json

# load ICD snippet (produced from configuration management)
with open('icd_fragment.json') as f:
    icd = json.load(f)

# compute timing margin per Eq. (1)
t_margin = icd['deadline_ms'] - (icd['tx_ms'] + icd['prop_ms'] + icd['proc_ms'])
# compute current margin per Eq. (2)
Imax = icd['connector_I_max_A']
Inom = icd['nominal_I_A']
I_margin = (Imax - Inom) / Inom

# quick compliance checks (thresholds are project specific)
if t_margin < icd.get('jitter_budget_ms', 1.0):
    print('FAIL: timing margin insufficient', t_margin)  # CI fail
if I_margin < icd.get('current_margin_req', 0.2):
    print('FAIL: current margin insufficient', I_margin)  # CI fail

# emit summary for configuration manager
print('Timing margin (ms):', t_margin)
print('Current margin:', I_margin)