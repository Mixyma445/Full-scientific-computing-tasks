import os
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Battery discharge log recorded every 30 minutes (0.0 to 3.0 hours)
time_hr = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
voltage_v = np.array([4.20, 4.02, 3.89, 3.78, 3.66, 3.49, 3.25])

linear_v = interp1d(time_hr, voltage_v, kind="linear")
cubic_v = CubicSpline(time_hr, voltage_v)

# Resample every 5 minutes (1/12 hour)
fine_time = np.linspace(0.0, 3.0, 37)
lin_curve = linear_v(fine_time)
cub_curve = cubic_v(fine_time)

# Compare estimates at t = 1.75 hr (1 hr 45 min) and t = 2.25 hr (2 hr 15 min)
for t_query in [1.75, 2.25]:
    print(f"t = {t_query:.2f} hr -> Linear: {float(linear_v(t_query)):.3f} V | Cubic Spline: {float(cubic_v(t_query)):.3f} V")

plt.figure(figsize=(8, 5))
plt.scatter(time_hr, voltage_v, color="red", zorder=5, label="30-min BMS readings")
plt.plot(fine_time, lin_curve, "--", label="Linear interpolation")
plt.plot(fine_time, cub_curve, label="Cubic spline")
plt.axhline(3.65, color="gray", linestyle=":", label="Low-battery threshold (3.65 V)")
plt.xlabel("Discharge Time (hours)")
plt.ylabel("Terminal Voltage (V)")
plt.title("Modified Case (Task 13): Li-Ion Battery Discharge Resampling")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_13_battery_case_graph.png", dpi=150)
plt.close()