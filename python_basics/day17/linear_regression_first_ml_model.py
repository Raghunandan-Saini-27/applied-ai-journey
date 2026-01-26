# DAY 17 – LINEAR REGRESSION (APPLIED AI STYLE)

'''🧠 What we are doing (simple words)

We teach the computer to predict numbers using past data.
'''

'''📌 sklearn = machine learning toolbox
📌 LinearRegression = simplest ML model'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

# Prepare Data

x=np.array([1,2,3,4,5]).reshape(-1,1)  # x=input (hours studied)
y=np.array([40,50,60,70,80])		   # y=output (marks)

'''Why reshape

ML models expect :
X → 2D
y → 1D
'''

# Create and train model

model=LR()
model.fit(x,y)
print("Slope :",model.coef_)      # slope(m)
print("Intercept :",model.intercept_) # intercept(b)


'''This is training:

model learns relationship between X and y'''


# Make predictions

predictions=model.predict(x)
print(predictions)

'''This is inference.'''


# Visualising Results

plt.scatter(x,y,label="Actual Data")
plt.plot(x,predictions,label="Prediction Line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Linear Regression : Study vs Marks")
plt.legend()
plt.savefig("linear_regression.png")
plt.show()
'''📌 Dots = real data
📌 Line = learned pattern'''


# Key Concepts

'''
| Term      | Meaning                 |
| --------- | ----------------------- |
| fit()     | learning                |
| predict() | using learned knowledge |
| X         | input / features        |
| y         | output / labels         |
'''