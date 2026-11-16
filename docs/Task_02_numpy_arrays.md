# Task 2: NumPy Arrays and Numerical Computation

## B. Input Values and Mathematical Operation
- **Inputs:** 24 hourly floating-point sensor readings stored in a 1D NumPy array.
- **Operation:** Vectorized statistical reductions (`np.mean`, `np.min`, `np.max`) and linear transformation ($F = 1.8C + 32$) applied across all array elements simultaneously.

## C. Parameter Modification & Effect on Result
- **Change:** Shifting dataset scale from ambient temperatures to industrial motor vibration telemetry.
- **Result Change:** Instead of thermal metrics, array indexing and boolean masks (`vibration_mms > 4.0`) isolate critical operational hours exceeding safety thresholds.

## D. Output Meaning & Graph Interpretation
- **Output Meaning:** Provides instant aggregate statistics without expensive Python `for` loops, crucial for real-time edge devices.

## E. Modified Real-World Case: IoT Motor Vibration Monitoring
- Applied to industrial machinery sensor streams to track wear-and-tear thresholds over a 24-hour manufacturing shift.