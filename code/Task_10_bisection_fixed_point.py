import os
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Heat-balance model: f(T) = 0 means heat gain equals heat loss (PDF Baseline)
def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

# Bisection: bracket a sign change
solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

# Fixed-point form: T = 25 + 10 * exp(-T / 20)
def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]
for _ in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10:
        break
    T = T_new

print(f"Bisection equilibrium temperature: {solution.root:.6f} °C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} °C")
print(f"Fixed-point iterations: {len(history) - 1}")

# Parameter Modification (Item C): Widen bisection bracket interval to [10, 60]
solution_wide = root_scalar(
    heat_balance,
    bracket=[10, 60],
    method="bisect",
    xtol=1e-10
)
print(f"Modified bracket [10, 60] bisection result: {solution_wide.root:.6f} °C (Evaluations: {solution_wide.function_calls})")

temps = np.linspace(20, 40, 300)
plt.figure(figsize=(8, 5))
plt.plot(temps, heat_balance(temps), label="f(T) Heat Balance")
plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(solution.root, color="r", linestyle="--", label=f"Equilibrium Root ({solution.root:.2f}°C)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Heat-balance function f(T)")
plt.title("Task 10: Equilibrium Temperature via Bisection")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_10_bisection_graph.png", dpi=150)
plt.close()