import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

# Second-order ODE: d^2T/dx^2 = 0 (linear temperature distribution with no internal heat generation)
def fun(x, y):
    # y[0] is T, y[1] is dT/dx
    return np.vstack((y[1], np.zeros_like(x)))

def bc(ya, yb):
    # Left boundary T(0) = 40, Right boundary T(1) = 200
    return np.array([ya[0] - 40.0, yb[0] - 200.0])

x = np.linspace(0, 1, 5)
y_initial = np.zeros((2, x.size))

solution = solve_bvp(fun, bc, x, y_initial)

x_plot = np.linspace(0, 1, 100)
y_plot = solution.sol(x_plot)[0]

midpoint_val = solution.sol(0.5)
print(f"Temperature at midpoint x=0.5: {midpoint_val[0]:.2f} C")

plt.plot(x_plot, y_plot, label="BVP Solution")
plt.xlabel("Position along rod (m)")
plt.ylabel("Temperature (C)")
plt.title("Steady-state rod temperature (BVP)")
plt.legend()
plt.grid(True)
plt.show()