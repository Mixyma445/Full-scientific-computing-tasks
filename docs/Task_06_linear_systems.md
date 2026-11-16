# Task 6: Solution of Systems of Linear Equations

## B. Input Values and Mathematical Operation
- **Inputs:** Resource consumption matrix $A = \begin{bmatrix} 4 & 2 \\ 8 & 12 \end{bmatrix}$ (CPU units and GB memory per server type) and total observed usage vector $\mathbf{b} = [20, 72]^T$.
- **Operation:** Solves the linear system $A\mathbf{x} = \mathbf{b}$ using `np.linalg.solve()` to determine active server counts $(x, y)$ and verifies accuracy via the residual vector $\mathbf{r} = \mathbf{b} - A\mathbf{x}$.

## C. Parameter Modification & Effect on Result
- **Change:** Increased total observed resource usage vector $\mathbf{b}$ from `[20, 72]` to `[28, 104]` (28 CPU units and 104 GB memory).
- **Result Change:** Active server counts shift from `3 Type A, 4 Type B` to `4 Type A, 6 Type B`, demonstrating linear scaling of the solution vector with right-hand side demand.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** `np.linalg.solve()` recovers exact integer server allocations with a residual norm $\|\mathbf{r}\|_2 \approx 0$, proving the solution satisfies both hardware constraints simultaneously.

## E. Modified Real-World Case: DC Electrical Circuit Nodal Analysis
- **Scenario & Assumptions:** Solving a 3-node resistive DC network (`code/Task_06_circuit_nodal_case.py`) governed by Kirchhoff's Current Law ($G\mathbf{V} = \mathbf{I}$), assuming linear ohmic resistors and steady-state current injections.
- **New Input Data:** Symmetric conductance matrix $G$ (Siemens) and external current vector $\mathbf{I} = [2.5, 0.0, 1.2]^T\text{ A}$.
- **Output & Interpretation:** Yields steady-state node potentials ($V_1 \approx 9.01\text{ V}$, $V_2 \approx 4.65\text{ V}$, $V_3 \approx 7.83\text{ V}$), allowing direct computation of branch currents across internal components.