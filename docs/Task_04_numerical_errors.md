# Task 4: Floating-Point Arithmetic and Numerical Errors

## B. Input Values and Mathematical Operation
- **Inputs:** Floating-point sum `0.1 + 0.2` vs `0.3`, $\sqrt{2}$ vs its truncated approximation `1.414`, and small values $x \in \{10^{-4}, 10^{-8}, 10^{-12}, 10^{-16}\}$.
- **Operation:** Evaluates exact vs tolerance-based equality (`np.isclose`), computes absolute and relative errors, and compares the algebraically unstable formula $\frac{\sqrt{1+x}-1}{x}$ against its rationalized stable equivalent $\frac{1}{\sqrt{1+x}+1}$.

## C. Parameter Modification & Effect on Result
- **Change:** Swept $x$ down across four orders of magnitude from $10^{-4}$ to $10^{-16}$.
- **Result Change:** At $x = 10^{-4}$, both formulas agree (`0.499987500625`). By $x = 10^{-12}$, the direct formula loses significant digits (`0.500044450291`), and at $x = 10^{-16}$ (below `float64` machine epsilon), $\sqrt{1+x}$ rounds to `1.0`, collapsing the direct formula to `0.0` while the rationalized form stays exact at `0.5`.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** Binary floating-point representation cannot store base-10 fractions like `0.1` exactly, requiring `np.isclose()` for comparisons. Furthermore, subtracting nearly equal numbers ($\sqrt{1+x} - 1$) triggers catastrophic cancellation, which rationalizing the numerator eliminates.

## E. Modified Real-World Case: Quadratic Formula Precision Loss
- **Scenario & Assumptions:** Computing small characteristic roots in control systems or orbital mechanics where $b^2 \gg 4ac$ (`code/Task_04_quadratic_cancellation_case.py`).
- **New Input Data:** $a = 1.0$, $b = 10^8$, $c = 1.0$.
- **Output & Interpretation:** In $(-b + \sqrt{b^2 - 4ac}) / 2a$, $\sqrt{b^2 - 4ac} \approx b$, causing catastrophic cancellation in the numerator. Using the rationalized form $\frac{2c}{-b - \sqrt{b^2 - 4ac}}$ eliminates the subtraction of nearly equal terms and recovers the exact root $-1.0000000000000000 \times 10^{-8}$.