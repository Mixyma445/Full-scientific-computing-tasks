import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# Concurrent users and measured server response time (milliseconds) (PDF Baseline)
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

# A simple quadratic model for increasing delay: y = a*x^2 + b*x + c
def model(x, a, b, c):
    return a * x**2 + b * x + c

parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted) ** 2))

print(f"Fitted quadratic model: y = {a:.6f}*x^2 + {b:.4f}*x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")

# Parameter Modification (Item C): Fit an exponential growth model y = a * exp(b * x) + c
def exp_model(x, a, b, c):
    return a * np.exp(b * x) + c

exp_params, _ = curve_fit(exp_model, users, response_ms, p0=[50, 0.005, 50])
rmse_exp = np.sqrt(np.mean((response_ms - exp_model(users, *exp_params)) ** 2))
print(f"Exponential model RMSE: {rmse_exp:.2f} ms")

x_plot = np.linspace(users.min(), 400, 300)
plt.figure(figsize=(8, 5))
plt.scatter(users, response_ms, color="black", zorder=5, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), "b-", linewidth=2, label="Fitted Quadratic Curve")
plt.xlabel("Concurrent Users")
plt.ylabel("Response Time (ms)")
plt.title("Task 14: Server Response-Time Curve Fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_14_curve_fitting_graph.png", dpi=150)
plt.close()