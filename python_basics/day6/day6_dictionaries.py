# Creating a dictonary

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

print(student)

# Acessing Values 

print(student["name"])
print(student["marks"])

# Acessing missing key

'''print(student["grade"])  # ❌ KeyError
'''

print(student.get("grade", "Not found"))  #safe way

# Modifying Dictionary

student["age"] = 21
student["grade"] = "A"

print(student)

# Looping Through Dictionary

'''keys only'''

for key in student:
    print(key)

'''values only'''

for value in student.values():
    print(value)

'''key+values'''

for key, value in student.items():
    print(key, ":", value)


# Example

'''Student marks dictionary'''

marks = {
    "math": 90,
    "science": 85,
    "english": 78
}

total = sum(marks.values())
average = total / len(marks)

print("Total:", total)
print("Average:", average)

# Nested Dictionary

students = {
    "101": {"name": "Aman", "marks": 88},
    "102": {"name": "Neha", "marks": 92}
}

print(students["101"]["name"])


# Practice Questions 

'''Exercise 1

Create a dictionary with:

name

age

skills (list)

Print all details'''

d_1={"Name":"Raghu","Age":19,"Skills":["Web Dev","Applied AI"]}
print(d_1.items())


'''Exercise 2

Input 3 subjects and marks from user

Store in dictionary

Print subject-wise marks'''

d_2={}
for i in range(3):
    subject=input("Enter the subject :")
    mark=input("Enter the marks for "+ subject +" :")
    d_2[subject]=mark
    
for subject, mark in d_2.items():
    print(f"{subject}:{mark}")
    

'''Exercise 3

Given dictionary:

prices = {"apple": 100, "banana": 40, "orange": 60}


Print items costing more than 50'''

prices = {"apple": 100, "banana": 40, "orange": 60}

for key,price in prices.items() :
    if price>50:
        print(key)