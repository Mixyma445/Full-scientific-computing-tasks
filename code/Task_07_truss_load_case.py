import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Fixed 3-node structural truss stiffness matrix K (in kN/m)
K = np.array([
    [1200.0, -400.0,    0.0],
    [-400.0, 1000.0, -400.0],
    [   0.0, -400.0,  800.0]
])

# Three distinct external load cases (in kN)
load_cases = {
    "Wind Load":    np.array([50.0, 20.0, 10.0]),
    "Snow Load":    np.array([30.0, 60.0, 30.0]),
    "Traffic Load": np.array([15.0, 45.0, 85.0])
}

# Factor stiffness matrix K once (O(n^3) cost paid once)
lu, piv = lu_factor(K)

print("=== Structural Truss Displacement Under Multiple Load Cases ===")
for name, F in load_cases.items():
    displacements_m = lu_solve((lu, piv), F)
    displacements_mm = displacements_m * 1000.0
    print(f"{name:12s} -> Node displacements (mm): {np.round(displacements_mm, 3)}")