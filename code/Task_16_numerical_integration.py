import numpy as np
from scipy.integrate import simpson

# Baseline: Smart-meter readings taken every 2 hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print("=== Baseline (2-Hour Intervals) ===")
print(f"Trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Simpson's rule:   {energy_simpson:.3f} kWh")
print(f"Difference:       {abs(energy_simpson - energy_trapezoid):.3f} kWh\n")

# Parameter Change (Item C): Peak midday surge from 1.8 kW to 2.6 kW
power_kw_modified = np.array([0.8, 1.0, 1.4, 2.6, 1.6, 1.2, 0.9])
mod_trap = np.trapezoid(power_kw_modified, time_hours)
mod_simp = simpson(power_kw_modified, x=time_hours)

print("=== Parameter Change (Peak Load = 2.6 kW at t=6h) ===")
print(f"Trapezoidal rule: {mod_trap:.3f} kWh")
print(f"Simpson's rule:   {mod_simp:.3f} kWh")
print(f"Difference:       {abs(mod_simp - mod_trap):.3f} kWh")