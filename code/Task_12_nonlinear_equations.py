import numpy as np
from scipy.optimize import root

# Find intersections of circle (x^2 + y^2 = 4) and parabola (y = x^2 - 1) (PDF Baseline)
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 4.0,
        y - (x**2 - 1.0)
    ]

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", np.round(solution.x, 6))
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()

# Parameter Modification (Item C): Expand circle radius squared from 4.0 to 6.25 (r = 2.5)
def equations_mod(z):
    x, y = z
    return [
        x**2 + y**2 - 6.25,
        y - (x**2 - 1.0)
    ]

print("=== Parameter Modification (Radius r = 2.5) ===")
sol_mod = root(equations_mod, [1.5, 1.5])
print("Modified Intersection:", np.round(sol_mod.x, 6))
print("Modified Residuals:", equations_mod(sol_mod.x))