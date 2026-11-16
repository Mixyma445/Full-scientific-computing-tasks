from scipy.optimize import root
import numpy as np

# Chemical equilibrium system for reaction A + B <-> C
# Given equilibrium constant K_p = 4.0 and initial moles, solve for extent of reaction variables (x, y)
def equilibrium_equations(vars):
    x, y = vars
    # Mass action balance residuals
    eq1 = (1.0 - x) * (2.0 - x) - 4.0 * x * y
    eq2 = y - 0.5 * x**2
    return [eq1, eq2]

sol_chem = root(equilibrium_equations, [0.2, 0.1])

print("=== Chemical Reaction Equilibrium ===")
print(f"Solver success: {sol_chem.success}")
print(f"Reaction extents [x, y]: {np.round(sol_chem.x, 6)}")
print(f"Equation residuals: {equilibrium_equations(sol_chem.x)}")