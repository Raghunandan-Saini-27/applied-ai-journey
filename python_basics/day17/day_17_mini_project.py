#🎯 DAY 17 MINI TASK (IMPORTANT)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

'''
1️⃣ Change data to:
'''
x =np.array([2, 4, 6, 8, 10]).reshape(-1,1)
y =np.array([45, 55, 65, 75, 85])



'''
2️⃣ Predict marks for:

hours = 7
'''

model=LR()
model.fit(x,y)

predictions=model.predict([[7]])

'''
3️⃣ Print predicted value
'''

print("Marks predicted for 7 hours :",predictions)
predictions=model.predict(x)

'''
4️⃣ Plot graph
'''

plt.scatter(x,y,label="Actual Data")
plt.plot(x,predictions,label="Predicted line")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Linar Regression :Time Studied vs Marks Obtained")
plt.legend()

'''
5️⃣ Save plot as image'''

plt.savefig("LR_time_marks")
plt.show()