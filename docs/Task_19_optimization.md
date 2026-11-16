# Task 19: Numerical Optimization

## B. Input Values and Mathematical Operation
- **Inputs:** Unit operating costs ($C_A = 12$, $C_B = 18$), unit processing capacities ($P_A = 100$, $P_B = 170$), and minimum required total capacity ($1,000$ units)[cite: 27, 28].
- **Operation:** Uses `scipy.optimize.minimize` (Sequential Least Squares Programming method, SLSQP) to find non-negative resource allocations $(x, y)$ that minimize total cost while satisfying inequality constraints[cite: 27, 28].

## C. Parameter Modification & Effect on Result
- **Change:** Increased the minimum capacity demand threshold from $1,000$ to $1,400$ units.
- **Result Change:** Higher resource demands scale up the optimal allocation amounts, increasing the minimum planning cost proportionally.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** The optimizer successfully identifies the cost-optimal continuous server blend that satisfies capacity bounds with zero slack.

## E. Modified Real-World Case: Warehouse Distribution Fleet Optimization
- **Scenario & Assumptions:** Minimizing fuel and labor expenses for dispatching freight trucks across two regional warehouse hubs (`code/Task_19_warehouse_logistics_case.py`) subject to minimum delivery quotas and driver hour limits.
- **Output & Interpretation:** The optimizer computes fractional truck dispatch numbers, providing baseline economic targets for logistics dispatch managers.