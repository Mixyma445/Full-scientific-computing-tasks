import numpy as np
from scipy.optimize import minimize

# Objective: Maximize profit = Revenue - Cost
# Let x = units of Product A, y = units of Product B
# Profit function to minimize (negative profit):
def objective(vars):
    x, y = vars
    revenue = 45.0 * x + 60.0 * y
    cost = 20.0 * x + 30.0 * y + 0.1 * (x**2 + y**2)
    return -(revenue - cost)  # Negative because we minimize

# Constraints:
# 1. Labor hours: 2x + 3y <= 120
# 2. Raw material: x + y <= 50
constraints = (
    {"type": "ineq", "fun": lambda vars: 120 - (2.0 * vars[0] + 3.0 * vars[1])},
    {"type": "ineq", "fun": lambda vars: 50 - (vars[0] + vars[1])}
)

# Bounds: production must be non-negative
bounds = ((0, None), (0, None))

initial_guess = [10.0, 10.0]

result = minimize(
    objective,
    initial_guess,
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

optimal_x, optimal_y = result.x
max_profit = -result.fun

print(f"Optimal units of Product A: {optimal_x:.2f}")
print(f"Optimal units of Product B: {optimal_y:.2f}")
print(f"Maximum profit: ${max_profit:.2f}")
print(f"Optimization successful: {result.success}")