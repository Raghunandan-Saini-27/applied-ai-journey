# Function

def greet():
    print("Hello, welcome to Applied AI!")

greet()

# Function with Parameter

def greet(name):
    print("Hello", name)

greet("Sraghi")

# Function with return value

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Functions + lists

def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

marks = [78, 85, 90]
avg = calculate_average(marks)
print("Average:", avg)

# Functions + dictionaries

def print_student(student):
    for key, value in student.items():
        print(key, ":", value)

student = {
    "name": "Aman",
    "age": 20,
    "marks": 88
}

print_student(student)


# Default Parameters

def greet(name="User"):
    print("Hello", name)

greet()
greet("Sraghi")


# Practice Exercises

'''Exercise 1: Even or Odd

Write a function that:

Takes a number

Returns "Even" or "Odd"'''

def f_1(n):
     if n%2==0:
         return f"{n} is even"
     else :
          return f"{n} is odd."
     
num=int(input("Enter the number :"))
result=f_1(num)

print(result)


'''Exercise 2: Maximum of 3 Numbers

Function that returns the largest of three numbers.'''

def check_large_num(a,b,c):
    if a>b :
        if a>c :
            return f"{a} is greatest number."
        else :
            return f"{c} is greatest number."
        
    elif b>a :
        if b>c :
            return f"{b} is greatest number."
        
        else :
            return f"{c} is greatest number."
            
    else:
        return f"{c} is greatest number."

a=int(input("enter the 1st no. :"))
b=int(input("enter the 2nd no. :"))
c=int(input("enter the 3rd no. :"))

result=check_large_num(a,b,c)
print(result)


'''Exercise 3: Marks Report

Function that:

Takes a list of marks

Returns total and average'''

n=int(input("Enter the no. of elements :"))
marks=[]
for i in range(n):
    x=int(input("Enter the element in the list :"))
    marks.append(x)

def marks_report(marks=[]):
    total=sum(marks)
    average=total/len(marks)
    return total,average
    
 
result=marks_report(marks)
print(f"Total and avearge :{result}")