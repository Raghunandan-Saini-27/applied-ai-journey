#comparison operators 

'''
| Operator | Meaning          |
| -------- | ---------------- |
| >      | greater than     |
| <      | less than        |
| >=     | greater or equal |
| <=     | less or equal    |
| ==     | equal            |
| !=     | not equal        |
'''

a=10
b=5
print(a>b)
print(a==b)

# if statement

age=int(input("Enter the age :"))
if age>18 :
	print("You are eligible to vote.")

# if-else statement 

age=int(input("Enter the age :"))
if age>18 :
	print("You are eligible to vote.")

else :
	print("You aren't eligible to wait.")


# if-elif-else statement 

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Mini Exercises 

'''Exercise 1: Even or Odd

Take a number from user

Print if it’s even or odd'''

num=int(input("enter the number :"))

if num%2==0 :
      print("Number is even.")
      
else :
      print("Number is odd.")
      

'''Exercise 2: Biggest of Two Numbers

Take 2 numbers

Print the larger one'''

num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
if num2>num1 :
      print("2nd number",num2,"is greater.")
      
elif num1==num2 :
	  print("both numbers are equal.")
        
else :
      print("1st number",num1,"is greater.")


'''Exercise 3: Simple Login System

Username = admin

Password = 1234

If correct → “Login successful”

Else → “Invalid credentials”
'''

Username=input("Enter the user name :")
Password=int(input("Enter the password :"))

if Username=="admin":
      if Password==1234:
            print("Login Successful.")
      else:
            print("Invalid Credentials.")
else :
      print("Invalid Credentials.")