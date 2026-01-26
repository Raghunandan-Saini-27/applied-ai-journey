# 🎯 4️⃣ Day 18 Mini Task (DO THIS)

'''
1️⃣ Train Linear Regression on Diabetes dataset
'''

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

data=load_diabetes()
x=data.data
y=data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

'''
2️⃣ Print MAE, MSE, R²
'''

mae=mean_absolute_error(y_test,y_pred)
print('MAE :',mae)

mse=mean_squared_error(y_test,y_pred)
print('MSE :',mse)

r2=r2_score(y_test,y_pred)
print('R2 :',r2)

'''
3️⃣ Write a README explaining:
'''

'''
-> What dataset is

-> What each metric means

-> Is the model good or bad?'''