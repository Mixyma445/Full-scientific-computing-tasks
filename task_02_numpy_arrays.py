import numpy as np

# 24 hourly server rack temperature readings in degrees Celsius
temperatures_c = np.array([
    45.0, 46.2, 45.8, 44.5, 43.9, 45.0,
    48.5, 52.8, 58.6, 64.1, 68.3, 72.0,
    74.4, 73.1, 70.5, 67.6, 62.2, 58.8,
    53.4, 50.1, 48.0, 46.2, 45.6, 45.0
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Vectorized Celsius-to-Fahrenheit conversion
temperatures_f = 1.8 * temperatures_c + 32

# Thermal anomaly check (> 70 C)
overheat_indices = np.where(temperatures_c > 70.0)[0]

print(f"Server rack mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print(f"Hours exceeding 70 C threshold: {overheat_indices}")
print("First six Fahrenheit readings:", temperatures_f[:6])