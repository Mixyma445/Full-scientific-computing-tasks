import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# RC charging circuit: dV/dt = (Vs - V) / (R * C) (PDF Baseline)
Vs = 5.0      # supply voltage (V)
R = 1000.0    # resistance (ohms)
C = 0.001     # capacitance (farads)
V0 = 0.0      # initial capacitor voltage

def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

t_eval = np.linspace(0, 5, 200)
solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact RC charging curve for validation
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

print("Solver success:", solution.success)
print(f"Capacitor voltage at 5 s: {solution.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {np.max(np.abs(solution.y[0] - exact)):.3e} V")

# Parameter Modification (Item C): Double capacitance C to 0.002 F (slower charging time constant)
C_mod = 0.002
def rc_circuit_mod(t, V):
    return [(Vs - V[0]) / (R * C_mod)]

solution_mod = solve_ivp(rc_circuit_mod, (0, 5), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
print(f"Capacitor voltage at 5 s (C=0.002F): {solution_mod.y[0, -1]:.4f} V")

plt.figure(figsize=(8, 5))
plt.plot(solution.t, solution.y[0], label="solve_ivp (C=1mF)", linewidth=2)
plt.plot(solution.t, solution_mod.y[0], label="solve_ivp Modified (C=2mF)", linestyle="--", linewidth=2)
plt.plot(solution.t, exact, linestyle=":", color="black", label="Exact (C=1mF)")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor Voltage (V)")
plt.title("Task 18: RC Circuit Charging via SciPy solve_ivp")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_18_scipy_ode_graph.png", dpi=150)
plt.close()