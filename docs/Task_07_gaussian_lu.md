# Task 7: Gaussian Elimination and LU Decomposition

## B. Input Values and Mathematical Operation
- **Inputs:** A $3 \times 3$ tridiagonal coefficient matrix $A$ and three measurement vectors $\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3$.
- **Operation:** Factors $PA = LU$ once using `scipy.linalg.lu_factor` ($O(n^3)$ operations) and solves each right-hand side via forward/backward substitution using `scipy.linalg.lu_solve` ($O(n^2)$ operations per solve).

## C. Parameter Modification & Effect on Result
- **Change:** Increased diagonal element $A_{0,0}$ from `4.0` to `8.0`.
- **Result Change:** Increasing the leading diagonal entry reduces the first unknown $x_1$ from `5.0` to `2.238`, which in turn propagates smaller coupling adjustments into $x_2$ and $x_3$.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** Confirms that `lu_solve` reproduces the exact direct `np.linalg.solve` vector (`[5., 5., 5.]`) with residual norms near machine zero ($\approx 10^{-16}$), while avoiding redundant matrix factorizations when solving repeated time-step vectors.

## E. Modified Real-World Case: Structural Truss Multi-Load Simulation
- **Scenario & Assumptions:** Evaluating static nodal displacements $\mathbf{u}$ of a linear-elastic 3-node bridge truss (`code/Task_07_truss_load_case.py`) under wind, snow, and traffic loads without re-factoring the constant stiffness matrix $K$.
- **Output & Interpretation:** Factoring $K$ once yields rapid displacement profiles in millimeters across all three load regimes, demonstrating how finite-element solvers handle time-varying forces efficiently.