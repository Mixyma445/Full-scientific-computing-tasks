import numpy as np

# 24 hourly vibration readings from an industrial motor (mm/s)
vibration_mms = np.array([
    1.2, 1.1, 1.0, 1.0, 1.3, 1.8, 2.5, 3.4,
    4.1, 4.8, 5.2, 5.0, 4.6, 4.2, 3.8, 3.1,
    2.4, 1.9, 1.5, 1.3, 1.2, 1.1, 1.0, 1.1
])

mean_vib = np.mean(vibration_mms)
peak_vib = np.max(vibration_mms)
warning_threshold = 4.0

# Count hours exceeding safe operating threshold
over_limit_hours = np.sum(vibration_mms > warning_threshold)

print(f"Mean Vibration: {mean_vib:.2f} mm/s")
print(f"Peak Vibration: {peak_vib:.2f} mm/s")
print(f"Hours exceeding 4.0 mm/s warning threshold: {over_limit_hours}")