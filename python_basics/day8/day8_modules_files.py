# Module

import math 

print(math.sqrt(25))
print(math.pi)

# Import whole module

import random 
print(random.randint(1,10))

# Import specific things 

from math import sqrt,pow
print(sqrt(16))
print(pow(2,3))

# Import with alias 

import math as m
print(m.sqrt(36))

# Useful builtin modules 

import datetime
today=datetime.date.today()
print(today)

# Basic file writiing

file=open("sample.txt","w")
file.write("Hello Applied AI\n")
file.write("Day 8 learning \n")
file.close()

# Basic file reading

file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

# Better way (auto closes file)

with open("sample.txt","r") as file :
	print(file.read())

# Practice Questions

'''Exercise 1

Write your name & age to a file

Read and print it'''

with open("ex_1.txt","w") as f_1 :
	f_1.write("Raghunandan\n")
	f_1.write("19\n")
	
with open("ex_1.txt","r") as f_1:
	print(f_1.read())

'''Exercise 2

Generate 5 random numbers

Save them to a file'''

import random as r 
with open("ex_2.txt","w") as f_2:
	for i in range(5):
		f_2.write(str(r.randint(1,100))+"\n")

with open("ex_2.txt","r") as f_2:
	print(f_2.read())

'''Exercise 3

Read marks from file

Calculate total & average'''

with open("ex_3.txt","r") as f_3:
	x=f_3.readlines()
	
marks=[]
for line in x:
	marks.append(int(line.strip()))

print("Total Marks",sum(marks))
print("Average Marks :",sum(marks)/len(marks))