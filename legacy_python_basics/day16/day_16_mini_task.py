# 🎯 DAY 16 MINI TASK (DO THIS)

import matplotlib.pyplot as plt

'''1️⃣ Plot student marks using bar chart'''
''' Add labels + title'''

names=["a","b","c","d","e"]
marks=[87,96,83,67,49]
plt.bar(names,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.savefig("student_mark_bar_chart.png")
plt.show()


'''2️⃣ Plot marks distribution using histogram'''
''' Add labels + title'''

plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Student Mark Histogram")
plt.savefig("student_marks_histogram.png")
plt.show()


'''3️⃣ Save the plot as an image'''
