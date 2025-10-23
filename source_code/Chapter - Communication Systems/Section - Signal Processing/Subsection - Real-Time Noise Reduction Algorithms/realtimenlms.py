import numpy as np

def nlms_cancel(rx, ref, mu=0.8, eps=1e-6, M=16):
    # rx: received complex baseband samples (numpy array)
    # ref: interference reference of same length
    N = len(rx)
    w = np.zeros(M, dtype=np.complex64)   # filter coefficients
    out = np.zeros(N, dtype=np.complex64)
    buf = np.zeros(M, dtype=np.complex64) # delay line
    for k in range(N):
        # update buffer (most recent at index 0)
        buf[1:] = buf[:-1]
        buf[0] = ref[k]
        y_hat = np.vdot(w, buf)           # filter output (conj-dot)
        e = rx[k] - y_hat                 # error = desired - estimate
        norm = eps + np.vdot(buf, buf).real
        w += (mu / norm) * e.conjugate() * buf  # NLMS update
        out[k] = e                         # cleaned sample
    return out, w