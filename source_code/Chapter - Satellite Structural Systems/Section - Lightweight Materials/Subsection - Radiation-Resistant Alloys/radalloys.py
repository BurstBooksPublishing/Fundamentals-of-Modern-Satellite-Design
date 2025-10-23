import numpy as np

# Empirical parameters (replace with irradiation test data)
sigma_y0 = 450.0  # MPa unirradiated yield
alpha = 0.15      # per DPA at reference temperature
T_ref = 293.0     # K

def residual_yield(dpa, alpha_local=alpha):
    # Exponential decay model (eq. \eqref{eq:sigma_decay})
    return sigma_y0 * np.exp(-alpha_local * dpa)

# Example: compute residual yield up to 1 DPA
dpa_vals = np.linspace(0, 1.0, 11)
res_yields = residual_yield(dpa_vals)
for d, s in zip(dpa_vals, res_yields):
    print(f"DPA={d:.2f}, Residual yield={s:.1f} MPa")  # inline comment