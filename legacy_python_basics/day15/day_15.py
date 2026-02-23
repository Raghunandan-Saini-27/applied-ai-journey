# Pandas = table view of data
# NumPy = math engine under the hood

import numpy as np

arr=np.array([10,20,30,40])
print(arr)

print("Adding +5 to all elements of array :\n",arr+5)

data=np.array([[85,90,78],[88,76,92]])
print("Shape of data array :",data.shape)

print("Mean of data array :",data.mean())

print("Mean of 'rows' of data array :",data.mean(axis=0))

print("Mean of 'columns' of data array :",data.mean(axis=1))

# Convert Pandas to Numpy

'''
X_np = X.values
y_np = y.values
'''