'''🧠 1️⃣ Core Concept (VERY IMPORTANT)

Training a model ≠ good model.

We evaluate models using metrics.

For Regression, the main ones are:

🔹 Mean Absolute Error (MAE)

-> Average absolute difference between predicted and actual

-> Easy to understand

🔹 Mean Squared Error (MSE)

-> Squares the error (punishes big mistakes)

🔹 R² Score (Most Important)

-> Tells how well the model explains the data

->Value range:

1) 1.0 → perfect

2) 0.0 → useless

3) < 0 → garbage'''

# Use a REAL DataSet

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


# Load dataset

data=load_diabetes()
x=data.data
y=data.target

# Train-test split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

'''Why?

Train → learn

Test → check honesty'''


# Train Model

model=LinearRegression()
model.fit(x_train,y_train)


# Predict

y_pred=model.predict(x_test)


# Evaluate

mae=mean_absolute_error(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("MAE :",mae)
print("MSE :",mse)
print("R2 Score :",r2)

'''
MAE: 42.7
MSE: 2900.1
R2 Score: 0.45

-> Means:

1) On average → prediction is off by ~42

2) Model explains ~45% of data

3) Decent baseline, not amazing
'''