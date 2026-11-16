import numpy as np

# Adjacency matrix for a small undirected network (PDF Baseline)
# Node order: A, B, C, D
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Dominant eigenvalue / eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]
print("Dominant eigenvalue:", round(dominant_value, 6))
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda * v
v = np.real(eigenvectors[:, index])
print("Verification error:", np.linalg.norm(A @ v - dominant_value * v))

# Parameter Modification (Item C): Add an edge between Node A and Node D
A_mod = A.copy()
A_mod[0, 3] = 1.0
A_mod[3, 0] = 1.0
eig_mod, vec_mod = np.linalg.eig(A_mod)
idx_mod = np.argmax(np.real(eig_mod))
dom_vec_mod = np.abs(np.real(vec_mod[:, idx_mod]))
centrality_mod = dom_vec_mod / dom_vec_mod.sum()

print("\nModified network (with A-D link) dominant eigenvalue:", round(np.real(eig_mod[idx_mod]), 6))
print("Modified importance scores:", dict(zip(nodes, np.round(centrality_mod, 4))))