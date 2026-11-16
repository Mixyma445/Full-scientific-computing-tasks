import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Simplified steady-state temperature model for five interior grid points (PDF Baseline)
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary influence: left boundary = 100 C, right boundary = 20 C
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i + 1:] @ old[i + 1:]
            ) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b, tol=1e-8)
x_gs, err_gs = gauss_seidel(A, b, tol=1e-8)
x_exact = np.linalg.solve(A, b)

# Parameter Modification (Item C): Relax stopping tolerance to 1e-3
x_j_coarse, err_j_coarse = jacobi(A, b, tol=1e-3)
x_gs_coarse, err_gs_coarse = gauss_seidel(A, b, tol=1e-3)

print("Jacobi temperatures (tol=1e-8):      ", np.round(x_j, 4), f"({len(err_j)} iters)")
print("Gauss-Seidel temperatures (tol=1e-8):", np.round(x_gs, 4), f"({len(err_gs)} iters)")
print("Direct exact solution:               ", np.round(x_exact, 4))
print(f"\nParameter Mod (tol=1e-3) -> Jacobi: {len(err_j_coarse)} iters, Gauss-Seidel: {len(err_gs_coarse)} iters")

plt.figure(figsize=(8, 5))
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change (Infinity Norm)")
plt.title("Task 8: Convergence of Iterative Temperature Solution")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_08_iterative_linear_graph.png", dpi=150)
plt.close()