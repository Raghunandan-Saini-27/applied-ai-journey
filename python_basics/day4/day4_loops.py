# for Loop (Most used)

for i in range(5):
    print(i)
    
for i in range(1, 11, 2):
    print(i)


# while loop 

i = 1
while i <= 5:
    print(i)
    i += 1

# ex-Table of a number 

num=int(input("Enter the number :"))
print("Table of ",num)
for i in range(1,11):
    print(num,'X',i,'=',num*i)
    
# ex-sum of numbers from 1 to n

num=int(input("Enter the number :"))
x=0
for i in range(1,num+1):
    x+=i
print("Sum of digits upto n is",x,".")

# Practice Exercises 

'''Exercise 1: Even numbers 1–20

Print all even numbers from 1 to 20.'''

for i in range(1,21):
    if i%2==0 :
        print(i)

'''Exercise 2: Count digits in a number

Input: 12345
Output: 5'''
x=0
num=int(input("Enter the number :"))
while num>0:
    num//=10
    x+=1

print(x)


'''Exercise 3: Simple password retry system

Correct password: 1234

User has 3 attempts

If correct → “Access granted”

Else → “Access denied”'''

x=3
for i in range(1,4):
    x-=1
    password=int(input("Enter the password :"))

    if password==1234:
        print("Acess Granted.")
        break

    else :
        print("Acess Denied.(",x," chances remaining)")