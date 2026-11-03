import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Cooling model: dT/dt = -k * (T - T_ambient)
k = 0.15
T_ambient = 20.0

def model(t, T):
    return -k * (T - T_ambient)

# Time span from t=0 to t=30 minutes, initial temperature = 90 C
t_span = (0, 30)
t_eval = np.linspace(0, 30, 300)
T0 = [90.0]

solution = solve_ivp(model, t_span, T0, t_eval=t_eval)

print(f"Final temperature at t=30 min: {solution.y[0][-1]:.2f} C")

plt.plot(solution.t, solution.y[0], label="Numerical (RK45)")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Newton's Law of Cooling (ODE Solution)")
plt.legend()
plt.grid(True)
plt.show()