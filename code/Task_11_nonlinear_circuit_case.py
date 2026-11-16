from scipy.optimize import root_scalar
import numpy as np

# Circuit equation: 12V supply, 1k ohm series resistor, Shockley diode forward drop
# f(V_d) = V_d + 1000 * I_0 * (exp(V_d / 0.026) - 1) - 12.0 = 0
def circuit_equation(V_d):
    V_source = 12.0
    R = 1000.0
    I_s = 1e-12
    V_t = 0.026
    return V_d + R * I_s * (np.exp(V_d / V_t) - 1.0) - V_source

def d_circuit_equation(V_d):
    R = 1000.0
    I_s = 1e-12
    V_t = 0.026
    return 1.0 + (R * I_s / V_t) * np.exp(V_d / V_t)

sol_newton = root_scalar(circuit_equation, fprime=d_circuit_equation, x0=0.6, method="newton", xtol=1e-10)
sol_secant = root_scalar(circuit_equation, x0=0.5, x1=0.8, method="secant", xtol=1e-10)

print("=== Nonlinear Diode Circuit Operating Point ===")
print(f"Newton-Raphson Diode Voltage: {sol_newton.root:.6f} V")
print(f"Secant Method Diode Voltage:  {sol_secant.root:.6f} V")
print(f"Function iterations (Newton): {sol_newton.iterations}")