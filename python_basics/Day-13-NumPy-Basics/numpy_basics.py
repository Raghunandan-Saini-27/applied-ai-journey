# WHY NUMPY EXISTS (VERY IMPORTANT)

# Python lists are:
'''
1) slow

2) not mathematical

3) not AI-friendly
''' 

# AI needs:

'''
1) fast math

2) vectors & matrices

3) batch operations

👉 NumPy = Python + math engine'''

import numpy as np

arr=np.array([10,20,30,40])
print(arr)
print(type(arr))

# Shape and dimensions

print(arr.shape)
print(arr.ndim)

# 2-D Array

marks=np.array([[80,90,70],[60,85,75]])
print(marks.shape)

# Numpy vs loop

for i in range(len(arr)):
    arr[i] += 5
print(arr)

arr=arr+5
print(arr)

# Basic Operations

print(arr+10)
print(arr*2)
print(arr.mean())
print(arr.max())
print(arr.min())

# Indexing and slicing

print(arr[1])
print(arr[1:3])

'''for 2D'''

print(marks[0])
print(marks[:,1])


# Mini Task

marks=np.array([[10,20,30],[60,50,40],[70,80,90]])
print("Shape :",marks.shape)
print("Average per student :",marks.mean(axis=1))
print("Avearge per subject :",marks.mean(axis=0))

'''axis=1 -> rowise
axis=2 -> columnwise'''