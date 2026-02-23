import pandas as pd

# load csv
df = pd.read_csv("data.csv")

# basic checks
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# selecting columns
X = df.drop("marks", axis=1)
y = df["marks"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# Average,max,min

print(df["marks"].mean())
print(df["marks"].max())
print(df["marks"].min())

# Filtering Rows

print(df[df["marks"] > 80])


# Day 14 Mini Task (short, practical, AI-focused)

'''🔹 Mini Task: Student Marks Data Analysis using Pandas

Task requirements (do ONLY this):'''

# 1) Load students.csv

df=pd.read_csv("students.csv")


# 2) Print:

'''-> first 5 rows'''

print("First Five Rows :\n",df.head())


'''-> shape'''

print("Shape :",df.shape)

'''-> column names'''

print("Column Names :",df.columns)


# 3) Calculate:

'''-> average marks'''

print("Avg Marks :",df["marks"].mean())

'''-> highest marks'''

print("Highest Marks :",df["marks"].max())

'''-> lowest marks'''

print("Lowest Marks :",df["marks"].min())

# 4) Filter students with marks > 80

print("Students with marks over 80:\n",df[df["marks"]>80])