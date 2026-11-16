import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Square object vertices in 2D space (columns are [x, y] points, closed loop)
square = np.array([
    [0.0, 2.0, 2.0, 0.0, 0.0],
    [0.0, 0.0, 2.0, 2.0, 0.0]
])

# 2D Rotation Matrix for theta = 45 degrees (pi/4 radians)
theta = np.radians(45)
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# Scaling Matrix (stretch x by 1.5, y by 0.8)
S = np.array([
    [1.5, 0.0],
    [0.0, 0.8]
])

# Composite transformation: Rotate first, then Scale (M = S @ R)
rotated_square = R @ square
transformed_square = (S @ R) @ square

print("Rotation matrix determinant (area preservation):", round(np.linalg.det(R), 4))
print("Composite matrix determinant (area scale factor):", round(np.linalg.det(S @ R), 4))

plt.figure(figsize=(7, 7))
plt.plot(square[0], square[1], "k-o", label="Original Square")
plt.plot(rotated_square[0], rotated_square[1], "b--o", label="Rotated (45°)")
plt.plot(transformed_square[0], transformed_square[1], "r-o", label="Rotated + Scaled")
plt.axhline(0, color="gray", linewidth=0.8)
plt.axvline(0, color="gray", linewidth=0.8)
plt.gca().set_aspect("equal")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Modified Case (Task 5): 2D CAD Matrix Transformations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_05_rotation_case_graph.png", dpi=150)
plt.close()