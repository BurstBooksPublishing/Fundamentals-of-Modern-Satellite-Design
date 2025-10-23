import math
# input parameters (SI units)
H = 500e3         # altitude (m)
p = 4.0e-6        # pixel pitch (m)
f = 2.0           # focal length (m)
D = 0.5           # aperture diameter (m)
lambda_c = 0.5e-6 # wavelength (m)

# computations
GSD = H * p / f                       # eq. (1)
theta = 1.22 * lambda_c / D          # rad, diffraction limit
R_diff = H * theta                   # ground resolution from optics
swath = (10240 * p / f) * H         # approximate swath for array of 10240 pixels

# print results (engineering units)
print(f"GSD = {GSD:.3f} m")           # pixel-limited resolution
print(f"Optical diffraction-limited R = {R_diff:.3f} m")
print(f"Approx. swath (10240 px) = {swath/1000:.1f} km")  # convert to km