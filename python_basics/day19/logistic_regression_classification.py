from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

data=load_breast_cancer()
x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)

y_predict=model.predict(x_test)

print("Accuracy :",accuracy_score(y_test,y_predict))
print("Confusion Matrix :\n",confusion_matrix(y_test,y_predict))