import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

services = ["API_Gateway", "Auth_Svc", "Billing_Svc", "Inventory_Svc", "Notify_Svc", "Core_DB"]

# Symmetric weighted traffic adjacency matrix (normalized API call frequency)
W = np.array([
    [0.0, 0.9, 0.7, 0.8, 0.3, 0.2],  # API_Gateway
    [0.9, 0.0, 0.5, 0.4, 0.1, 0.8],  # Auth_Svc
    [0.7, 0.5, 0.0, 0.3, 0.6, 0.9],  # Billing_Svc
    [0.8, 0.4, 0.3, 0.0, 0.2, 0.9],  # Inventory_Svc
    [0.3, 0.1, 0.6, 0.2, 0.0, 0.2],  # Notify_Svc
    [0.2, 0.8, 0.9, 0.9, 0.2, 0.0]   # Core_DB
])

# Use eigh since W is real and symmetric
eigvals, eigvecs = np.linalg.eigh(W)
dominant_val = eigvals[-1]
dominant_vec = np.abs(eigvecs[:, -1])
importance_scores = dominant_vec / dominant_vec.sum()

print("=== Microservice Eigenvector Centrality Ranking ===")
print(f"Spectral Radius (Dominant Eigenvalue): {dominant_val:.4f}")
for svc, score in sorted(zip(services, importance_scores), key=lambda x: x[1], reverse=True):
    print(f"{svc:15s}: {score:.4f} ({score*100:.1f}%)")

plt.figure(figsize=(8, 5))
plt.bar(services, importance_scores, color="steelblue")
plt.xlabel("Microservice Node")
plt.ylabel("Normalized Eigenvector Centrality")
plt.title("Modified Case (Task 9): Microservice Network Criticality Ranking")
plt.xticks(rotation=20)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("../docs/Task_09_microservice_centrality_graph.png", dpi=150)
plt.close()