import numpy as np

# Inputs: temps (K) time series, dt (s), material dict with E, alpha, nu, basquin params
# (Use lab-characterized sigma_prime and b for the specific material.)
def thermal_damage(temps, dt, material):
    # simple peak-trough cycle count (placeholder for rainflow)
    peaks = np.concatenate(([temps[0]], temps[(1:-1)[(temps[1:-1]>temps[:-2])&(temps[1:-1]>temps[2:])]], [temps[-1]]))
    troughs = np.concatenate(([temps[0]], temps[(1:-1)[(temps[1:-1]<temps[:-2])&(temps[1:-1]<temps[2:])]], [temps[-1]]))
    # approximate cycle amplitudes from adjacent extrema (replace with rainflow)
    deltas = np.abs(np.diff(np.sort(np.concatenate((peaks,troughs)))))
    D = 0.0
    for dT in deltas:
        # thermal stress amplitude (constrained case)
        delta_sigma = material['E']*material['alpha']*dT/(1-material['nu'])
        # Basquin relation -> Nf estimate
        Nf = (material['sigma_prime'] / (delta_sigma/2.0))**(1.0/material['b'])
        n_cycles = 1  # count per observed amplitude; scale by repetition as needed
        D += n_cycles / Nf
    return D

# Example call uses measured material params from qualification tests.