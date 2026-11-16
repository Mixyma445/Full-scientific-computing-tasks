# Task 11: Root Finding — Newton-Raphson and Secant Methods

## B. Input Values and Mathematical Operation
- **Inputs:** Initial investment cash flow `-10,000` followed by annual inflows `[3000, 3500, 4000, 2500]`[cite: 17].
- **Operation:** Evaluates Net Present Value function $NPV(r) = 0$ and its analytical derivative $NPV'(r)$ to find the Internal Rate of Return ($r$) using **Newton-Raphson** ($x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$) and the **secant method**[cite: 17, 18].

## C. Parameter Modification & Effect on Result
- **Change:** Increased the final year (Year 4) cash inflow from `2500` to `4500`.
- **Result Change:** Higher cash inflows raise project profitability, shifting the IRR upward from $\approx 18.92\%$ to $\approx 27.45\%$.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** Both Newton-Raphson and secant algorithms converge rapidly to the exact root where $NPV(r) = 0$ ($< 10^{-12}$ residual), outperforming bracketed bisection by requiring fewer iterations once inside the basin of attraction.

## E. Modified Real-World Case: Nonlinear Diode-Resistor Circuit Analysis
- **Scenario & Assumptions:** Solving the transcendental Shockley diode equation combined with a series DC voltage source (`code/Task_11_nonlinear_circuit_case.py`) to find the exact operating diode voltage.
- **Output & Interpretation:** Newton-Raphson computes the operating voltage ($\approx 0.655\text{ V}$) in just a few iterations, demonstrating how derivative-based solvers handle exponential nonlinearities in hardware circuit design.