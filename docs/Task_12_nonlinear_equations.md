# Task 12: Polynomial and Nonlinear Equation Solving

## B. Input Values and Mathematical Operation
- **Inputs:** Two simultaneous nonlinear equations representing a circle ($x^2 + y^2 = 4$) and a parabola ($y = x^2 - 1$)[cite: 18, 19].
- **Operation:** Uses `scipy.optimize.root` with multiple initial guesses ([1.0, 1.0], [-1.0, 1.0]) to search for coordinate pairs $(x, y)$ that reduce all equation residuals to zero[cite: 18, 19].

## C. Parameter Modification & Effect on Result
- **Change:** Expanded the circle radius squared parameter from `4.0` to `6.25` ($r = 2.5$).
- **Result Change:** The intersection points shift outward along the parabola, modifying the coordinate solutions from $\pm(1.3229, 0.7485)$ to $\pm(1.5811, 1.5000)$ while preserving convergence success.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** Multidimensional nonlinear solvers successfully locate multiple valid geometric intersections by iteratively updating Jacobian approximations starting from distinct basin guesses.

## E. Modified Real-World Case: Gas-Phase Chemical Equilibrium
- **Scenario & Assumptions:** Solving nonlinear mass-action equations (`code/Task_12_chemical_equilibrium_case.py`) for a chemical dissociation network governed by equilibrium constants.
- **Output & Interpretation:** The solver computes steady-state reactant conversion levels with residual errors near machine zero ($\approx 10^{-14}$), demonstrating how multivariate nonlinear solvers model chemical process engineering systems.