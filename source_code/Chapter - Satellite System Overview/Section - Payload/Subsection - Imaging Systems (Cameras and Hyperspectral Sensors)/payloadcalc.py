import math
# constants
h = 6.62607015e-34  # Planck constant (J*s)
c = 299792458.0     # speed of light (m/s)

def compute_gsd(H, pixel_pitch, focal_length):
    # H: orbit height (m); pixel_pitch,focal_length: (m)
    return H * pixel_pitch / focal_length

def exposure_for_snr(L, A, delta_lambda, T_sys, eta_qe, wavelength, snr_req, read_noise, dark_rate):
    # L: spectral radiance (W/m2/sr/m), A: aperture area (m2)
    # delta_lambda: bandpass (m); T_sys: throughput; eta_qe: QE (0-1)
    # wavelength: central wavelength (m); snr_req: desired SNR
    # read_noise: electrons RMS; dark_rate: e-/s
    photon_energy = h * c / wavelength
    # photons per second per pixel -> convert radiance to flux assuming unit solid angle and pixel field
    # simplified: assume pixel IFOV integrated into effective radiance factor = 1
    signal_rate = L * A * delta_lambda * T_sys * eta_qe / photon_energy
    # solve for integration time from SNR ≈ Ne / sqrt(Ne + Ndark + Read^2)
    # quadratic in t: (signal_rate * t)^2 / (signal_rate * t + dark_rate * t + read_noise^2) = snr_req^2
    # rearrange to at^2 - b t - c = 0
    a = signal_rate**2
    b = snr_req**2 * (signal_rate + dark_rate)
    c = snr_req**2 * read_noise**2
    # solve at^2 - b t - c = 0 for positive root
    t = (b + math.sqrt(b**2 + 4*a*c)) / (2*a)
    return t

# example: 500 km, 5.5 micron pixel, 1.2 m focal length
print(compute_gsd(500e3, 5.5e-6, 1.2))
# exposure example requires mission radiance inputs (placeholder)