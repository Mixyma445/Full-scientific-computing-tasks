import numpy as np

# x = number of Type A servers, y = number of Type B servers (PDF Baseline)
# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total observed usage: 20 CPU units and 72 GB memory
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])
b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# Parameter Modification (Item C): Total observed usage rises to 28 CPU units and 104 GB memory
b_mod = np.array([28.0, 104.0])
sol_mod = np.linalg.solve(A, b_mod)
print(f"\nModified workload -> Type A: {sol_mod[0]:.0f}, Type B: {sol_mod[1]:.0f}")