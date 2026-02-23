# Get user input 

name=input("Enter your name :")
age=int(input("Enter your age :"))  #int(input(" ")) -> converting imput into integer

print("What's Up!",name)
print("Next year u will be :",age+1)

# basic calculations

num1=float(input("Enter the first number :"))
num2=float(input("Enter the second number :"))

# performing arithmetic opertaions

print("Sum :",num1+num2)
print("Sub :",num1-num2)
print("Multi :",num1*num2)
print("Div :",num1/num2)
print("Floor Div :",num1//num2)
print("Square :",num1**num2)

# Mini Exercise 

m1=int(input("Enter thr marks for English sub:"))
m2=int(input("Enter the marks for Maths sub :"))
m3=int(input("Enter the marks for Hindi sub :"))
print("Total Marks :",m1+m2+m3)
print("Avg. Marks :",(m1+m2+m3)/3)