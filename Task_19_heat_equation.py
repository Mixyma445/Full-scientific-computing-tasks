import numpy as np
import matplotlib.pyplot as plt

# Spatial domain and grid
L = 1.0
nx = 50
dx = L / (nx - 1)
x = np.linspace(0, L, nx)

# Time domain and stability constraint
alpha = 0.01  # Thermal diffusivity
dt = 0.4 * (dx**2) / alpha  # Ensure stability criterion dt <= dx^2 / (2*alpha)
total_time = 0.5
nt = int(total_time / dt)

# Initial temperature profile (e.g., ambient with a hot spot in the middle)
u = np.zeros(nx)
u[int(nx * 0.4):int(nx * 0.6)] = 100.0

# Time-stepping loop (explicit finite difference)
for n in range(nt):
    u_new = u.copy()
    for i in range(1, nx - 1):
        u_new[i] = u[i] + (alpha * dt / dx**2) * (u[i+1] - 2*u[i] + u[i-1])
    # Boundary conditions: fixed at 0 C
    u_new[0] = 0.0
    u_new[-1] = 0.0
    u = u_new

print(f"Max temperature at t={total_time}s: {u.max():.2f} C")

plt.plot(x, u, label=f"Temperature at t={total_time}s")
plt.xlabel("Position along bar (m)")
plt.ylabel("Temperature (C)")
plt.title("Transient 1D Heat Conduction (PDE)")
plt.legend()
plt.grid(True)
plt.show()