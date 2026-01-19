#Creating a list:

marks = [78, 85, 90, 66]
print(marks)

#Indexing 

print(marks[0])   # First element
print(marks[-1])  # Last element

#Slicing

print(marks[1:3])
print(marks[:2])
print(marks[2:])

#looping over list

for m in marks:
    print(m)

#List methods 

marks.append(88)      # Add element
marks.remove(66)      # Remove element
marks.sort()          # Sort list
marks.reverse()       # Reverse list

print(marks)


# Mini example

marks = []

for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)

average = sum(marks) / len(marks)
print("Average:", average)


# Tuples(Read only lists)

colors = ("red", "green", "blue")
print(colors[0])

'''
Tuples cannnot be modified.
It is used when data isn't supposed to change.
'''


'''Exercise 1

Take 5 numbers

Store in list

Print:

Max

Min

Average
'''

lst=[]
for i in range(5):
    x=int(input("Enter the element :"))
    lst.append(x)
    
print(min(lst))
print(max(lst))
print(sum(lst)/len(lst))

'''Exercise 2

Given list: [10, 20, 30, 40, 50]

Print elements > 25
'''

l_2=[10,20,30,40,50]
for m in l_2:
    if m>25:
        print(m) 


'''Exercise 3

Store 5 names in a tuple

Print them using a loop
'''

tup=("Raju","Krishna","Rahul","Dev","Ravi")
for m in tup:
    print(m[:])