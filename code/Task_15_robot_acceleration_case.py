import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Autonomous robot velocity telemetry: time (s), forward velocity (m/s)
t_data = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], dtype=float)
v_data = np.array([0.0, 0.8, 1.9, 3.0, 3.1, 2.0, 0.0], dtype=float)

accel = np.zeros_like(v_data)
# Central difference interior acceleration estimation (dv/dt)
accel[0] = (v_data[1] - v_data[0]) / (t_data[1] - t_data[0])
for i in range(1, len(t_data) - 1):
    accel[i] = (v_data[i + 1] - v_data[i - 1]) / (t_data[i + 1] - t_data[i - 1])
accel[-1] = (v_data[-1] - v_data[-2]) / (t_data[-1] - t_data[-2])

print("=== Robot Kinematic Acceleration Analysis ==p")
for t, v, a in zip(t_data, v_data, accel):
    print(f"t={t:.1f}s | Velocity={v:.1f} m/s | Acceleration={a:.2f} m/s^2")

plt.figure(figsize=(8, 5))
plt.plot(t_data, v_data, "b-o", label="Velocity (m/s)")
plt.plot(t_data, accel, "g--s", label="Acceleration (m/s^2)")
plt.xlabel("Time (s)")
plt.ylabel("Kinematic Values")
plt.title("Modified Case (Task 15): Robot Acceleration from Velocity Logs")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_15_acceleration_case_graph.png", dpi=150)
plt.close()