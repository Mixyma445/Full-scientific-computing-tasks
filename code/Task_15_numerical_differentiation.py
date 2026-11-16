import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# GPS samples: time in seconds and position in metres (PDF Baseline)
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0], dtype=float)

speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Central differences for interior points
for i in range(1, len(time) - 1):
    speed[i] = (position[i + 1] - position[i - 1]) / (time[i + 1] - time[i - 1])

# Backward difference at the end
speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed = {v:.2f} m/s")

# Parameter Modification (Item C): Inject ±0.5m random measurement noise into GPS positions
rng = np.random.default_rng(42)
noisy_position = position + rng.normal(0, 0.5, size=position.shape)
noisy_speed = np.zeros_like(noisy_position)
noisy_speed[0] = (noisy_position[1] - noisy_position[0]) / (time[1] - time[0])
for i in range(1, len(time) - 1):
    noisy_speed[i] = (noisy_position[i + 1] - noisy_position[i - 1]) / (time[i + 1] - time[i - 1])
noisy_speed[-1] = (noisy_position[-1] - noisy_position[-2]) / (time[-1] - time[-2])

print("\nSpeeds with noisy position data:", np.round(noisy_speed, 2))

plt.figure(figsize=(8, 5))
plt.plot(time, speed, marker="o", linestyle="-", linewidth=2, label="Clean GPS Speed")
plt.plot(time, noisy_speed, marker="x", linestyle="--", color="red", label="Noisy GPS Speed")
plt.xlabel("Time (s)")
plt.ylabel("Estimated Speed (m/s)")
plt.title("Task 15: Speed Estimated from GPS Position Data")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_15_differentiation_graph.png", dpi=150)
plt.close()