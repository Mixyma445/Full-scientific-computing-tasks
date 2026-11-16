import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

# SIR Epidemic Model ODEs
# dS/dt = -beta * S * I / N
# dI/dt = beta * S * I / N - gamma * I
# dR/dt = gamma * I

N = 1000.0  # Total population
I_0 = 5.0   # Initial infected
R_0 = 0.0   # Initial recovered
S_0 = N - I_0 - R_0

beta = 0.3    # Transmission rate
gamma = 0.1   # Recovery rate

dt = 0.5      # Time step in days
days = 60.0
t_steps = np.arange(0, days + dt, dt)

S = np.zeros_like(t_steps)
I = np.zeros_like(t_steps)
R = np.zeros_like(t_steps)

S[0], I[0], R[0] = S_0, I_0, R_0

for i in range(len(t_steps) - 1):
    s, inf, r = S[i], I[i], R[i]
    dS = -beta * s * inf / N
    dI = (beta * s * inf / N) - (gamma * inf)
    dR = gamma * inf
    
    S[i+1] = s + dt * dS
    I[i+1] = inf + dt * dI
    R[i+1] = r + dt * dR

print("=== SIR Epidemic Simulation (Day 60) ===")
print(f"Susceptible: {S[-1]:.1f}")
print(f"Infected:    {I[-1]:.1f}")
print(f"Recovered:   {R[-1]:.1f}")

plt.figure(figsize=(8, 5))
plt.plot(t_steps, S, label="Susceptible", color="blue")
plt.plot(t_steps, I, label="Infected", color="red")
plt.plot(t_steps, R, label="Recovered", color="green")
plt.xlabel("Time (Days)")
plt.ylabel("Population Count")
plt.title("Modified Case (Task 17): SIR Epidemic Spread via Euler Method")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_17_sir_epidemic_graph.png", dpi=150)
plt.close()