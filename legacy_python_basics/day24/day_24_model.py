# Model side

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data=load_breast_cancer()

x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)

with open("model24.pkl","wb") as f:
	pickle.dump(model,f)

print("Model saved as model24.pkl")