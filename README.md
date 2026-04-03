# WALMART-Predictive-Maintenance-
Aim
To compute the equipment health score using sensor data.
General Objective
To understand predictive maintenance systems and how sensor metrics like temperature and vibration are combined to assess equipment health.
Specific Objective
To compute health score using:
H
e
a
l
t
h
=
100
−
(
0.4
T
+
1.1
V
)
Health=100−(0.4T+1.1V)
Given:
Temperature 
T
=
80
T=80
Vibration 
V
=
10
V=10
Dataset
NASA Turbofan Engine Dataset
Source: NASA
Procedure
Input temperature value
Input vibration value
Apply health formula
Compute health score
Display result
Algorithm
Start
Input 
T
T and 
V
V
Compute health
Display result
Stop
Code Logic
health = 100 - (0.4*T + 1.1*V)
Python Code
# SESSION 26 – Predictive Maintenance

# Step 1: Input values
T = 80   # temperature
V = 10   # vibration

# Step 2: Compute health score
health = 100 - (0.4 * T + 1.1 * V)

# Step 3: Display result
print("Health Score =", int(health))

print("\nProgram Executed Successfully")
Output
Health Score = 56

Program Executed Successfully
Result
The computed health score is:
Health = 56
Industry Application
Predictive maintenance is used in:
Industrial equipment monitoring
Manufacturing systems
IoT-based maintenance
Robotics systems
Companies like Walmart use this in:
Supply chain optimization
Warehouse equipment monitoring
Automation systems
Conclusion
Combining sensor data into a health score helps predict failures early, improving system reliability and reducing maintenance costs.
