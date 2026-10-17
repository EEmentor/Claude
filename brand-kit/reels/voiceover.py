import soundfile as sf
from kokoro_onnx import Kokoro
k=Kokoro('kokoro-v1.0.onnx','voices-v1.0.bin')
L=["Power cut? Your home keeps running.",
"Meet the all-in-one E S S: battery and inverter, in a single system.",
"A built-in five-kilowatt inverter, with M P P T solar input,",
"stores your surplus solar energy for later.",
"It runs on solar, grid, or battery power, and monitors the grid for you.",
"From five to twenty kilowatt-hours, with plug-in modules for easy installation.",
"Order yours today. The link is below."]
for i,t in enumerate(L):
    a,sr=k.create(t,voice='af_heart',speed=1.1,lang='en-us'); sf.write(f'aio_{i}.wav',a,sr); print(i,round(len(a)/sr,2))
