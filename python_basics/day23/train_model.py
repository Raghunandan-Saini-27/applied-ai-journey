from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

#load dataset

data=load_diabetes()
x=data.data
y=data.target

#split data

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#train model

model=LinearRegression()
model.fit(x_train,y_train)

#Save Model

with open("model.pkl","wb") as f: 
	pickle.dump(model,f)

print("Model trained and saved as model.pkl")