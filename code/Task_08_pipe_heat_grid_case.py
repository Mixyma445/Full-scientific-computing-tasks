import os
import numpy as np
import matplotlib.pyplot as plt
from Task_08_iterative_linear import jacobi, gauss_seidel

os.makedirs("../docs", exist_ok=True)

# 20 interior spatial nodes along a heated industrial pipe (N = 20)
N = 20
# Diagonally dominant matrix including convective heat-loss term (+0.2 on diagonal)
main_diag = 2.2 * np.ones(N)
off_diag = -1.0 * np.ones(N - 1)
A_pipe = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)

# Left flange held at 250 C (boiler), right flange at 40 C (ambient sink), ambient = 20 C
b_pipe = 0.2 * 20.0 * np.ones(N)
b_pipe[0] += 250.0
b_pipe[-1] += 40.0

T_jacobi, err_j = jacobi(A_pipe, b_pipe, tol=1e-8, max_iter=1000)
T_gs, err_gs = gauss_seidel(A_pipe, b_pipe, tol=1e-8, max_iter=1000)

print(f"20-Node Pipe Grid -> Jacobi converged in {len(err_j)} iterations")
print(f"20-Node Pipe Grid -> Gauss-Seidel converged in {len(err_gs)} iterations")

# Full temperature profile including both boundary flanges
full_temps = np.concatenate(([250.0], T_gs, [40.0]))
positions = np.linspace(0, 2.0, N + 2)  # 2-meter pipe length

plt.figure(figsize=(8, 5))
plt.plot(positions, full_temps, "r-o", linewidth=2, label="Steady-State Pipe Temp (Gauss-Seidel)")
plt.xlabel("Pipe Position (m)")
plt.ylabel("Temperature (°C)")
plt.title("Modified Case (Task 8): 20-Node Steam Pipe Thermal Profile")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_08_pipe_heat_case_graph.png", dpi=150)
plt.close()