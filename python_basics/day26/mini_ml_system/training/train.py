import pickle
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

#load data
data=load_diabetes()

x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#train model
model=LinearRegression()
model.fit(x_train,y_train)

#save versioned model

with open("mini_ml_system/models/model_v1.pkl","wb") as f:
	pickle.dump(model,f)

print("Model v1 trained and saved.")