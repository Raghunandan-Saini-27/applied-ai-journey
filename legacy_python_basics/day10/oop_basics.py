# What is OOP ?

'''It groups data + functions that work on the data into one unit.
This unit is called class.'''

'''
class -> Blueprint
__init__ -> Runs automatically when object is created.
self -> refers to the current object.
'''

class Student:
	def __init__(self,name,marks):
		self.name=name
		self.marks=marks

	def calculate_average(self):
		avg=sum(self.marks.values())/len(self.marks)
		return avg
	
# Creating an object

marks={"Math":80,"Science":90}
student1=Student("Ravi",marks)

print(student1.name)
print(student1.calculate_average())