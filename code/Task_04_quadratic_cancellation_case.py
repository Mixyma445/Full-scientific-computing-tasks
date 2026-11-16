import numpy as np

# Quadratic equation with b^2 >> 4ac: x^2 + 10^8 * x + 1 = 0
a = 1.0
b = 1e8
c = 1.0

discriminant = np.sqrt(b**2 - 4 * a * c)

# Standard textbook formula suffers catastrophic cancellation for the smaller root
root_naive = (-b + discriminant) / (2 * a)

# Numerically stable formulation: r2 = (2 * c) / (-b - sqrt(b^2 - 4ac))
root_stable = (2 * c) / (-b - discriminant)

rel_err = abs(root_naive - root_stable) / abs(root_stable)

print("=== Near-Singular Quadratic Root Solver ===")
print(f"Standard formula smaller root: {root_naive:.16e}")
print(f"Stable formula smaller root:   {root_stable:.16e}")
print(f"Relative error from cancellation: {rel_err:.2%}")