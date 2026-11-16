import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Experimental battery discharge telemetry: time in hours, voltage in volts
time_hrs = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
voltage_v = np.array([4.20, 4.05, 3.88, 3.65, 3.50, 3.38, 3.25, 3.00], dtype=float)

# Empirical discharge model: V(t) = a * exp(-b * t) + c
def discharge_model(t, a, b, c):
    return a * np.exp(-b * t) + c

# Initial parameter guesses
popt, _ = curve_fit(discharge_model, time_hrs, voltage_v, p0=[1.2, 0.2, 3.0])
a, b, c = popt

predicted_v = discharge_model(time_hrs, a, b, c)
rmse_batt = np.sqrt(np.mean((voltage_v - predicted_v) ** 2))

print("=== Lithium-Ion Battery Discharge Curve Fit ===")
print(f"Fitted Model: V(t) = {a:.4f} * exp(-{b:.4f} * t) + {c:.4f}")
print(f"Discharge Model RMSE: {rmse_batt:.4f} V")

t_plot = np.linspace(0.0, 7.0, 200)
plt.figure(figsize=(8, 5))
plt.scatter(time_hrs, voltage_v, color="darkred", zorder=5, label="Telemetry Data")
plt.plot(t_plot, discharge_model(t_plot, a, b, c), "r--", linewidth=2, label="Fitted Exponential Decay")
plt.xlabel("Discharge Time (Hours)")
plt.ylabel("Terminal Voltage (V)")
plt.title("Modified Case (Task 14): Battery Discharge Curve Fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_14_battery_case_graph.png", dpi=150)
plt.close()