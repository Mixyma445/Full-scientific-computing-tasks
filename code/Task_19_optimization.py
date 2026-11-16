import numpy as np
from scipy.optimize import minimize

# x = capacity units of Type A server, y = capacity units of Type B server (PDF Baseline)
# Cost per unit: A = 12, B = 18
# Capacity per unit: A = 100, B = 170
# Required total capacity: at least 1000

def cost(z):
    x, y = z
    return 12.0 * x + 18.0 * y

def capacity_constraint(z):
    x, y = z
    return 100.0 * x + 170.0 * y - 1000.0

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}
bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[5.0, 3.0],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100.0 * x + 170.0 * y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# Parameter Modification (Item C): Increase required capacity from 1000 to 1400 units
def capacity_constraint_mod(z):
    x, y = z
    return 100.0 * x + 170.0 * y - 1400.0

constraints_mod = {"type": "ineq", "fun": capacity_constraint_mod}
solution_mod = minimize(cost, x0=[5.0, 5.0], method="SLSQP", bounds=bounds, constraints=constraints_mod)
x_m, y_m = solution_mod.x
print(f"\nModified Optimization (Capacity >= 1400) -> Cost: {solution_mod.fun:.2f} (A: {x_m:.2f}, B: {y_m:.2f})")