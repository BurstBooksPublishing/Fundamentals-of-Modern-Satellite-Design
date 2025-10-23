import csv
# Load measured and reference frequencies; tolerance per mode.
meas = {}  # mode -> measured freq (Hz)
ref  = {}  # mode -> reference freq (Hz)
tol  = 0.02  # 2% tolerance

# parse CSV file with columns: mode, f_meas, f_ref
with open('modal_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        m = int(row['mode'])
        meas[m] = float(row['f_meas'])
        ref[m]  = float(row['f_ref'])

fails = []
for m in sorted(ref):
    rel_err = abs(meas[m]-ref[m])/ref[m]
    # flag if outside tolerance
    if rel_err > tol:
        fails.append((m,meas[m],ref[m],rel_err))
# print brief report (used in AIV meetings)
if fails:
    for m, fm, fr, re in fails:
        print(f"Mode {m}: FAIL measured={fm:.2f}Hz ref={fr:.2f}Hz err={re:.3f}")
else:
    print("All modes within tolerance.")