import numpy as np

def estimate_seu_rate(energies, fluxes, cross_sections):
    """Compute SEU rate [events/sec] from discrete energies."""
    # energies: array of particle energies [MeV] (not used directly)
    # fluxes: array of differential flux [particles/cm2/s/MeV]
    # cross_sections: array of device cross-section [cm2] at each energy
    # integrate using simple trapezoidal rule over energy bins
    integrand = fluxes * cross_sections
    return np.trapz(integrand, energies)  # events per cm2 per sec

# Example usage with synthetic data (engineers replace with model spectrum).
E = np.array([1, 10, 100])          # MeV
phi = np.array([1e-3, 1e-4, 1e-6])  # particles/cm2/s/MeV
sigma = np.array([1e-6, 1e-5, 1e-4])# cm2
rate = estimate_seu_rate(E, phi, sigma)
print("Estimated SEU rate [events/cm2/s]:", rate)