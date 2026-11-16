import numpy as np

# DC Resistor Bridge Network (Kirchhoff's Current Law at 3 unknown nodes: V1, V2, V3)
# Conductance matrix G (in Siemens, where G_ij = 1 / R_ij) and current source vector I (in Amps)
G = np.array([
    [ 0.35, -0.10, -0.05],   # Node 1 equations
    [-0.10,  0.40, -0.15],   # Node 2 equations
    [-0.05, -0.15,  0.30]    # Node 3 equations
])
I_sources = np.array([2.5, 0.0, 1.2])  # External current injections (Amps)

# Solve G * V = I for node voltages [V1, V2, V3]
node_voltages = np.linalg.solve(G, I_sources)

# Calculate current flowing through the bridge resistor between Node 1 and Node 2 (R_12 = 10 ohms)
R_12 = 10.0
I_bridge = (node_voltages[0] - node_voltages[1]) / R_12

print("=== DC Circuit Nodal Analysis (G * V = I) ===")
for idx, v in enumerate(node_voltages, start=1):
    print(f"Node {idx} Voltage (V{idx}): {v:.4f} V")
print(f"Bridge current (Node 1 -> Node 2): {I_bridge:.4f} A")