# Task 18: Numerical Solution of ODEs Using SciPy

## B. Input Values and Mathematical Operation
- **Inputs:** Supply voltage $V_s = 5.0\text{ V}$, resistance $R = 1,000\,\Omega$, capacitance $C = 0.001\text{ F}$, initial voltage $V_0 = 0\text{ V}$, and evaluation time window from $0$ to $5$ seconds[cite: 25, 26].
- **Operation:** Uses `scipy.integrate.solve_ivp` (Runge-Kutta adaptive step-size solver) to numerically integrate the first-order ODE $\frac{dV}{dt} = \frac{V_s - V}{RC}$ across requested evaluation points[cite: 25, 26].

## C. Parameter Modification & Effect on Result
- **Change:** Doubled the capacitance parameter $C$ from $0.001\text{ F}$ to $0.002\text{ F}$.
- **Result Change:** Doubling capacitance doubles the time constant ($\tau = RC$), slowing the exponential charging curve so the capacitor reaches a lower terminal voltage ($3.93\text{ V}$ instead of $4.65\text{ V}$) at $t = 5\text{ s}$.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** The solver matches the exact analytical charging curve with maximum absolute error below $10^{-11}\text{ V}$, verifying high numerical fidelity[cite: 26, 27].
- **Graph Interpretation:** The slower charging trajectory for $C = 0.002\text{ F}$ rises more gradually than the baseline curve.

![Task 18 SciPy ODE Graph](Task_18_scipy_ode_graph.png)

## E. Modified Real-World Case: Sequential Chemical Reactor Kinetics
- **Scenario & Assumptions:** Simulating coupled multi-species mass conservation ODEs for a batch chemical reaction network ($A \rightarrow B \rightarrow C$) using `solve_ivp`[cite: 25, 27].
- **Output & Interpretation:** Accurately tracks reactant depletion alongside intermediate and final product accumulation over a 6-second window, demonstrating how adaptive SciPy solvers handle multivariate dynamic systems.

![Task 18 Chemical Reactor Graph](Task_18_chemical_reactor_graph.png)