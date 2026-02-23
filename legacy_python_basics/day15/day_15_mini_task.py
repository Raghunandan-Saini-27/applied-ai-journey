# 🎯 DAY 15 MINI TASK (DO THIS)

#1️⃣ Create a NumPy array of marks

import numpy as np

marks=np.array([[87,83,96]])

#2️⃣ Print mean, max, min

print("Avg Marks :",marks.mean())
print("Highest Marks :",marks.max())
print("Lowest Marks :",marks.min())

#3️⃣ Add 5 marks to everyone

marks=marks+5
print("Updated marks :\n",marks)

#4️⃣ Create a 2D array and calculate subject-wise average

marks_2D=np.array([[56,67,78],[67,76,79]])
print('Sub Wise Mean :',marks_2D.mean(axis=0))