import numpy as np

# Four corners of a square: each row is [x, y] (PDF Baseline)
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

angle = np.deg2rad(45)
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combined transformation
transformation = rotation @ scale
transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))

# Parameter Modification (Item C): Change rotation angle to 90 degrees
angle_90 = np.deg2rad(90)
rot_90 = np.array([[np.cos(angle_90), -np.sin(angle_90)], [np.sin(angle_90), np.cos(angle_90)]])
print("\nTransformed points at 90 deg:\n", np.round(points @ (rot_90 @ scale).T, 4))