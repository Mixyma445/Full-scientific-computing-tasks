import os
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Hourly temperature measurements (8:00 to 14:00)
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate every 10 minutes = 1/6 hour
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

# Baseline target time (10:30) and modified target time (12:30)
for target_time, label in [(10.5, "10:30"), (12.5, "12:30")]:
    print(f"[{label}] Linear estimate: {float(linear(target_time)):.2f} C | Cubic estimate: {float(cubic(target_time)):.2f} C")

plt.figure(figsize=(8, 5))
plt.scatter(hours, temperature, color="black", zorder=5, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, "--", label="Linear interpolation")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Task 13: Hourly Temperature Interpolation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_13_interpolation_graph.png", dpi=150)
plt.close()