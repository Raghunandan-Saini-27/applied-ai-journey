# DAY 16 – MATPLOTLIB (FROM ZERO, APPLIED AI FOCUS)

#🔹 What Matplotlib is
'''
Matplotlib = drawing graphs from data

AI uses it to:

1) see data distribution

2) detect outliers

3) explain results in demos/hackathons
'''

import matplotlib.pyplot as plt

# Basic Line Plot

marks=[87,83,96]
plt.plot(marks)
plt.show()

'''🧠 This draws:

x-axis → index (0,1,2)

y-axis → marks'''

plt.plot(marks)
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Student Marks Line Plot")
plt.show()


# Bar Chart 

names=["A","B","C"]
marks=[87,83,96]
plt.bar(names,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.show()

'''Best for comparison.'''


# Scatter Plot( ML Favoutite)

age=[20,21,19]
marks=[87,83,96]
plt.scatter(age,marks)
plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Age vs Marks ")
plt.show()

'''Used to:

1) find relationships

2) check trends'''


# Histogram (Very Important for AI)

marks=[87,83,96,78,90,88]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()

'''
| Plot      | When to use  |
| --------- | ------------ |
| Line      | trend        | -> time-series analysis
| Bar       | comparison   | -> to compare numeric values (*values should be min.)
| Scatter   | relationship | -> used to show co-realtion bw objects
| Histogram | distribution | -> for frequency distribution
'''