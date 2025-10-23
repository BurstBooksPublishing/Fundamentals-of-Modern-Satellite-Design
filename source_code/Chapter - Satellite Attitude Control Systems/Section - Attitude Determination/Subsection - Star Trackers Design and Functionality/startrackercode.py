import numpy as np
# image: 2D numpy array; catalog: list of inertial star vectors
def centroid(image, x0, y0, window=7):
    # extract small patch and compute intensity-weighted centroid
    w = image[y0-window//2:y0+window//2+1, x0-window//2:x0+window//2+1]
    Y, X = np.indices(w.shape)
    I = w.clip(0) + 1e-6
    cx = (X*I).sum()/I.sum() + x0-window//2
    cy = (Y*I).sum()/I.sum() + y0-window//2
    return cx, cy

def pix2vec(cx, cy, fx, fy, cx0, cy0):
    # simple pinhole mapping to body-frame unit vector
    x = (cx - cx0)/fx
    y = (cy - cy0)/fy
    v = np.array([x, y, 1.0])
    return v / np.linalg.norm(v)

def identify(star_vecs, catalog_kd):
    # fast nearest-neighbor in inertial-angle space (tracking mode)
    ids = []
    for v in star_vecs:
        _, idx = catalog_kd.query(v, k=1)  # kd-tree lookup
        ids.append(idx)
    return ids

# main loop (simplified)
# detect peaks -> compute centroids -> map to vectors -> identify -> solve Wahba