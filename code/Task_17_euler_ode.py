import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Newton's law of cooling: dT/dt = -k * (T - T_ambient) (PDF Baseline)
T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 1.0  # minutes
end_time = 30.0

def cooling_rate(T):
    return -k * (T - T_ambient)

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * cooling_rate(temperature[i])

# Exact solution for validation
exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

print(f"Euler temperature after 30 min (h=1.0): {temperature[-1]:.2f} °C")
print(f"Exact temperature after 30 min:          {exact[-1]:.2f} °C")
print(f"Final absolute error (h=1.0):            {abs(temperature[-1] - exact[-1]):.4f} °C")

# Parameter Modification (Item C): Halve step size h to 0.5 minutes
h_half = 0.5
time_half = np.arange(0, end_time + h_half, h_half)
temp_half = np.zeros_like(time_half)
temp_half[0] = T_initial
for i in range(len(time_half) - 1):
    temp_half[i + 1] = temp_half[i] + h_half * cooling_rate(temp_half[i])

exact_half = T_ambient + (T_initial - T_ambient) * np.exp(-k * time_half)
print(f"Euler temperature after 30 min (h=0.5): {temp_half[-1]:.2f} °C")
print(f"Final absolute error (h=0.5):            {abs(temp_half[-1] - exact_half[-1]):.4f} °C")

plt.figure(figsize=(8, 5))
plt.plot(time, temperature, marker="o", label="Euler (h=1.0 min)")
plt.plot(time_half, temp_half, marker="x", linestyle="--", label="Euler (h=0.5 min)")
plt.plot(time, exact, label="Exact Solution", color="black")
plt.xlabel("Time (Minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Task 17: Cooling of a Hot Object via Euler's Method")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_17_euler_graph.png", dpi=150)
plt.close()