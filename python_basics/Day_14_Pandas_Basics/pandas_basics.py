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
