import os
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Photovoltaic diode equation: I_solar - I_0 * (exp(V / (n * V_t)) - 1) - V / R_sh = I_load
# Solving for terminal voltage V given a load current of 3.0 Amps
def pv_voltage_residual(V):
    I_solar = 5.0      # Photocurrent (A)
    I_0 = 1e-9         # Reverse saturation current (A)
    n_vt = 0.026       # Thermal voltage constant * ideality factor (V)
    R_sh = 500.0       # Shunt resistance (ohms)
    I_load = 3.0       # Required load current (A)
    
    diode_current = I_0 * (np.exp(V / n_vt) - 1.0)
    shunt_current = V / R_sh
    return I_solar - diode_current - shunt_current - I_load

# Bracket voltage between 0.0V and 1.0V
sol_pv = root_scalar(pv_voltage_residual, bracket=[0.0, 1.0], method="bisect", xtol=1e-8)

print("=== PV Solar Cell Operating Voltage ===")
print(f"Computed terminal voltage: {sol_pv.root:.4f} V")
print(f"Residual check: {pv_voltage_residual(sol_pv.root):.2e} A")

voltages = np.linspace(0.0, 0.8, 200)
currents = [pv_voltage_residual(v) for v in voltages]

plt.figure(figsize=(8, 5))
plt.plot(voltages, currents, color="darkorange", linewidth=2, label="PV Residual Function")
plt.axhline(0, color="gray", linestyle=":")
plt.axvline(sol_pv.root, color="blue", linestyle="--", label=f"Operating V = {sol_pv.root:.3f}V")
plt.xlabel("Terminal Voltage (V)")
plt.ylabel("Current Residual (A)")
plt.title("Modified Case (Task 10): Solar Cell Operating Point Root Finding")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_10_pv_voltage_case_graph.png", dpi=150)
plt.close()