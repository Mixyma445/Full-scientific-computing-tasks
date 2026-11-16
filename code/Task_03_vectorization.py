import numpy as np
import timeit

# Simulated network latency readings in milliseconds (PDF Baseline)
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version():
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()

print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")

# Parameter Modification (Item C): Increase upper latency bound to 1000 ms
latency_high = rng.uniform(5, 1000, 1_000_000)
result_high = (latency_high / 1000.0) ** 2
print("Modified max squared latency (1000 ms bound):", np.max(result_high))