# Minimal Keras-like pseudocode for edge inference. Inline comments brief.
import numpy as np
# load quantized model (already signed and verified) -> model
# x: normalized telemetry vector
def anomaly_score(x, model):
    x = np.clip(x, -5.0, 5.0)                 # bound inputs
    x_hat = model.predict(x.reshape(1,-1))   # edge infer
    r = np.linalg.norm(x - x_hat)            # reconstruction error
    return float(r)

# example usage:
# score = anomaly_score(telemetry_vector, onboard_model)
# if score > threshold: raise_alert()