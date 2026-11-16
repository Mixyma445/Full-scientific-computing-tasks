import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# 100,000 acoustic hydrophone samples over 0.5 seconds (200 kHz sample rate)
t = np.linspace(0, 0.5, 100_000)

# Real-world sonar pulse: exponential water attenuation + frequency-modulated chirp
attenuation = np.exp(-6.0 * t)
chirp_freq = 40 + 120 * t  # Frequency sweeps from 40 Hz up to 100 Hz
sonar_pulse = attenuation * np.cos(2 * np.pi * chirp_freq * t)

# Vectorized root-mean-square (RMS) voltage calculation
rms_amplitude = np.sqrt(np.mean(sonar_pulse**2))
print(f"Sonar Pulse RMS Amplitude: {rms_amplitude:.4f} V")

plt.figure(figsize=(8, 5))
plt.plot(t[:20_000], sonar_pulse[:20_000], color="teal", label="Attenuated Chirp Pulse")
plt.xlabel("Time (s)")
plt.ylabel("Hydrophone Voltage (V)")
plt.title("Modified Case (Task 3): Vectorized Acoustic Sonar Pulse")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_03_sonar_case_graph.png", dpi=150)
plt.close()