# SESSION 26 – Predictive Maintenance

# Step 1: Input values
T = 80   # temperature
V = 10   # vibration

# Step 2: Compute health score
health = 100 - (0.4 * T + 1.1 * V)

# Step 3: Display result
print("Health Score =", int(health))

print("\nProgram Executed Successfully")
