import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Sequential reactions: A -> B -> C
# dA/dt = -k1 * A
# dB/dt = k1 * A - k2 * B
def batch_reactor(t, y):
    A, B = y
    k1 = 0.8
    k2 = 0.3
    dA_dt = -k1 * A
    dB_dt = (k1 * A) - (k2 * B)
    return [dA_dt, dB_dt]

t_span = (0, 6)
t_eval = np.linspace(0, 6, 200)
initial_concentrations = [1.0, 0.0]  # Initial pure reactant A (1.0 mol/L)

sol_chem = solve_ivp(batch_reactor, t_span, initial_concentrations, t_eval=t_eval, rtol=1e-8, atol=1e-10)

# Concentration of C can be inferred by mass conservation: C = 1.0 - A - B
A_conc = sol_chem.y[0]
B_conc = sol_chem.y[1]
C_conc = 1.0 - A_conc - B_conc

print("=== Chemical Reactor Species Concentrations (t = 6s) ===")
print(f"Reactant A: {A_conc[-1]:.4f} mol/L")
print(f"Product B:  {B_conc[-1]:.4f} mol/L")
print(f"Product C:  {C_conc[-1]:.4f} mol/L")

plt.figure(figsize=(8, 5))
plt.plot(sol_chem.t, A_conc, label="Reactant A", color="blue")
plt.plot(sol_chem.t, B_conc, label="Intermediate B", color="orange")
plt.plot(sol_chem.t, C_conc, label="Product C", color="green")
plt.xlabel("Time (Seconds)")
plt.ylabel("Concentration (mol/L)")
plt.title("Modified Case (Task 18): Sequential Chemical Kinetics via SciPy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_18_chemical_reactor_graph.png", dpi=150)
plt.close()