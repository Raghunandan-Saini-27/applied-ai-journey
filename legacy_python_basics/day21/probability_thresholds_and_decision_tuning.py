# 🎯 DAY 21 MINI TASK: Probability Threshold Tuning

'''🧠 Objective

Understand how changing thresholds affects model behavior

See precision–recall tradeoff in action

Think like a real-world AI decision designer'''

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score,precision_score,f1_score

data=load_breast_cancer()

x=data.data
y=data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)

# Prediction Probabilities

y_prob=model.predict_proba(x_test)[:,1]


# Trying Multiple Tresholds

thresholds=[0.3,0.5,0.7]

for t in thresholds:
	y_pred_custom=(y_prob>=t).astype(int)
	print(f"\nThreshold: {t}")
	print("Precision:", precision_score(y_test, y_pred_custom))
	print("Recall   :", recall_score(y_test, y_pred_custom))
	print("F1 Score :", f1_score(y_test, y_pred_custom))
