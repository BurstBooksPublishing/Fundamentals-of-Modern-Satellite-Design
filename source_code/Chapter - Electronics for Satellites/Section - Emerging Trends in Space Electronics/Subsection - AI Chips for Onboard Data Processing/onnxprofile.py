import onnxruntime as ort
import numpy as np
# load model and create random input (shape matches payload preprocessing)
sess = ort.InferenceSession("model.onnx")
input_name = sess.get_inputs()[0].name
# warmup
x = np.random.rand(1,3,224,224).astype(np.float32)  # example image tensor
for _ in range(5):
    sess.run(None, {input_name: x})
# timed inference loop
import time, subprocess
N = 100
t0 = time.time()
for _ in range(N):
    sess.run(None, {input_name: x})
t = (time.time() - t0) / N  # s per inference (latency)
# read power sensor (replace with real sensor call) -> P_watts
P_watts = float(subprocess.check_output(["cat","/sys/devices/power_sensor"]))  # placeholder
E_inf = P_watts * t  # Joules per inference
print(f"latency={t:.4f}s, power={P_watts:.2f}W, E_inf={E_inf:.4f}J")