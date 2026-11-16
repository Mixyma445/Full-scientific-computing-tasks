import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("../docs", exist_ok=True)

rng = np.random.default_rng(100)
N_sims = 50_000

# Task duration estimates (optimistic, most likely, pessimistic) in weeks
# Task A: Design
a_des, m_des, b_des = 2.0, 3.0, 6.0
# Task B: Implementation
a_imp, m_imp, b_imp = 4.0, 7.0, 16.0
# Task C: Testing & Deployment
a_tst, m_tst, b_tst = 1.5, 3.0, 7.5

# Triangular distribution sampling for project phases
dur_des = rng.triangular(a_des, m_des, b_des, N_sims)
dur_imp = rng.triangular(a_imp, m_imp, b_imp, N_sims)
dur_tst = rng.triangular(a_tst, m_tst, b_tst, N_sims)

total_project_duration = dur_des + dur_imp + dur_tst

target_deadline = 15.0  # weeks
late_probability = np.mean(total_project_duration > target_deadline)

print("=== Monte Carlo Project Completion Risk Analysis ===")
print(f"Mean project duration: {np.mean(total_project_duration):.2f} weeks")
print(f"90th percentile duration: {np.percentile(total_project_duration, 90):.2f} weeks")
print(f"Probability of exceeding {target_deadline} weeks: {late_probability:.2%}")

plt.figure(figsize=(8, 5))
plt.hist(total_project_duration, bins=60, density=True, color="teal", edgecolor="black", alpha=0.7)
plt.axvline(target_deadline, color="red", linestyle="--", linewidth=2, label=f"Target Deadline ({target_deadline} wks)")
plt.xlabel("Project Completion Time (Weeks)")
plt.ylabel("Probability Density")
plt.title("Modified Case (Task 20): PERT Project Duration Monte Carlo Simulation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../docs/Task_20_project_completion_graph.png", dpi=150)
plt.close()