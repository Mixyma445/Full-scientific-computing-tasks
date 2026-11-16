import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Random demand scenarios (PDF Baseline)
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

# Parameter Modification (Item C): Increase demand standard deviation from 120 to 180
std_high = 180.0
demand_high = rng.normal(mean_demand, std_high, N)
overloaded_high = demand_high > capacity
print(f"Modified overload probability (std=180): {overloaded_high.mean():.4%}")

plt.figure(figsize=(8, 5))
plt.semilogx(
    indices + 1,
    running_probability[indices],
    color="darkblue",
    linewidth=2,
    label="Monte Carlo Convergence"
)
plt.xlabel("Number of Simulations (N)")
plt.ylabel("Estimated Overload Probability")
plt.title("Task 20: Monte Carlo Estimate of Server-Overload Risk")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_20_monte_carlo_graph.png", dpi=150)
plt.close()