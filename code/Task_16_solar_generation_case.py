import os
import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Hourly solar PV power output (kW) from 06:00 to 18:00
hours = np.arange(6, 19, 1, dtype=float)
solar_kw = np.array([0.0, 0.45, 1.35, 2.50, 3.45, 4.10, 4.35, 4.05, 3.30, 2.25, 1.10, 0.30, 0.0])

yield_trap = np.trapezoid(solar_kw, hours)
yield_simp = simpson(solar_kw, x=hours)

print(f"Total Daily Solar Yield (Trapezoidal): {yield_trap:.3f} kWh")
print(f"Total Daily Solar Yield (Simpson's):   {yield_simp:.3f} kWh")
print(f"Method Discrepancy:                    {abs(yield_simp - yield_trap):.4f} kWh")

plt.figure(figsize=(8, 5))
plt.plot(hours, solar_kw, "o-", color="darkorange", label="Measured PV Output (kW)")
plt.fill_between(hours, solar_kw, color="orange", alpha=0.25, label=f"Integrated Yield = {yield_simp:.2f} kWh")
plt.xlabel("Time of Day (24-hr)")
plt.ylabel("Power Output (kW)")
plt.title("Modified Case (Task 16): Daily Rooftop Solar Energy Yield")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_16_solar_case_graph.png", dpi=150)
plt.close()