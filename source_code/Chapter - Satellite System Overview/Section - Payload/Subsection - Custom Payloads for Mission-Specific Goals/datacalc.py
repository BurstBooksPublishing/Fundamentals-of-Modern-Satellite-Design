# early sizing script: compute raw and compressed data rates
H = 600e3                # orbit altitude in meters
pixel_pitch = 5e-6       # pixel pitch in meters
focal_length = 1.2       # focal length in meters
bpp = 12                 # bits per pixel
lines_per_frame = 10000  # pushbroom lines per second equivalent
pixels_per_line = 2048   # detectors across track
compression = 4.0        # expected compression ratio

# compute GSD (meters)
GSD = (H * pixel_pitch) / focal_length
# raw data rate (bits/s)
raw_rate = pixels_per_line * lines_per_frame * bpp
# compressed rate (bits/s)
compressed_rate = raw_rate / compression

print("GSD (m):", GSD)                # to confirm eq. (1)
print("Raw data rate (Mbps):", raw_rate/1e6)
print("Compressed rate (Mbps):", compressed_rate/1e6)
# use these outputs to size RF link and ground station contact time