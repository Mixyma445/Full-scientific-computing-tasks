from scipy.optimize import minimize
import numpy as np

# Logistics cost minimization: Hub 1 and Hub 2 truck dispatch counts (x, y)
# Objective: Minimize 250*x + 320*y (fuel and driver wages)
# Constraints: Total deliveries >= 85 packages, driver hours <= 40 hours
def transport_cost(z):
    x, y = z
    return 250.0 * x + 320.0 * y

def delivery_constraint(z):
    x, y = z
    return (15.0 * x + 25.0 * y) - 85.0  # Must deliver at least 85 packages

def hour_constraint(z):
    x, y = z
    return 40.0 - (2.0 * x + 3.0 * y)     # Total driver hours <= 40

constraints = [
    {"type": "ineq", "fun": delivery_constraint},
    {"type": "ineq", "fun": hour_constraint}
]
bounds = [(0, None), (0, None)]

sol_logistics = minimize(transport_cost, x0=[1.0, 1.0], method="SLSQP", bounds=bounds, constraints=constraints)

print("=== Warehouse Logistics Transport Optimization ===")
print(f"Optimization success: {sol_logistics.success}")
print(f"Optimal dispatch from Hub 1 (x): {sol_logistics.x[0]:.2f} trucks")
print(f"Optimal dispatch from Hub 2 (y): {sol_logistics.x[1]:.2f} trucks")
print(f"Minimum transportation cost: KES {sol_logistics.fun:.2f}")