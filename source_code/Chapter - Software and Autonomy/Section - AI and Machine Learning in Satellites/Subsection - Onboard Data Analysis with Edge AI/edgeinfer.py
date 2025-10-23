import onnxruntime as ort  # runtime; in flight use C++ runtime binding
import numpy as np
# load quantized model (signed and verified beforehand)
sess = ort.InferenceSession("model_quant.onnx")
input_name = sess.get_inputs()[0].name

def preprocess(raw_image):  # crop, resize, normalize
    img = raw_image[::2,::2]  # downsample as low-cost preproc
    img = (img / 255.0).astype(np.float32)
    return img[np.newaxis, ...]  # add batch dim

def run_inference(image):  # bounded-time call
    x = preprocess(image)
    out = sess.run(None, {input_name: x})
    return out[0]

def decision_logic(raw_image, energy_budget_j, dl_budget_bytes):
    if energy_budget_j < 0.5:  # reserve threshold
        return False, None  # skip heavy processing
    logits = run_inference(raw_image)
    score = float(logits[0,0])  # confidence for target class
    if score > 0.85 and dl_budget_bytes >= 1e5:
        # prepare reduced product for downlink (metadata + ROI)
        payload = {"score": score, "roi": raw_image[100:500,100:500].tolist()}
        return True, payload
    return False, None