# Mini Project: Student Marks Manager WIth OOPS

# Add student marks

students={}
class StudentManager:
	def __init__(self):
		self.students={}

	def add_student(self):
		n_1=int(input("Enter the number of the students :"))
		n_2=int(input("Enter the number of subjects :"))

		for i in range(n_1):
			stu_marks={}
			stu_name=input("Name of the student :")
			for j in range(n_2):
				sub=input("Enter the name of the subject :")
				marks=int(input(f"Enter the marks for the {sub} :"))
				stu_marks[sub]=marks
			self.students[stu_name]=stu_marks

 
# View Student

	def view_students(self):
		if not self.students :
			print("No student data available.")
			return
	
		for name ,marks in self.students.items():
			print(f"{name}->{marks}")



# Calculate average marks

	def calculate_average(self):
		for name,subjects in self.students.items(): 
			avg=sum(subjects.values())/len(subjects.values())
			print(f"Avg of {name}:{avg}")


# Save data to a file

	def save_data_to_file(self,filename="oop_students_data.txt"):
		with open(filename,"w") as f:
			for name,subjects in self.students.items():
				subject_marks=[]
				for sub,mark in subjects.items():
					subject_marks.append(f"{sub}:{mark}")
				line=name+"|"+",".join(subject_marks)
				f.write(line+"\n")
		print("Data Saved Sucessfully.")


# Load data from a file

	def load_students_from_file(self,filename="oop_students_data.txt"):
		try:
			with open(filename,"r") as f:
				for line in f:
					line=line.strip()

					if not line:
						continue
					name,data=line.split("|")
					subjects={}

					for item in data.split(","):
						sub,mark=item.split(":")
						subjects[sub]=int(mark)
					self.students[name]=subjects

		except FileNotFoundError:
			pass

# User Interface

def main():
	manager=StudentManager()
	manager.load_students_from_file()
	
	while True:
		print("\n--- Student Marks Manager ---")
		print("1. Add Student")
		print("2. View Students")
		print("3. Calculate Average")
		print("4. Save & Exit")
		
		
		choice = input("Enter your choice: ")
		
		if choice == "1":
			manager.add_student()
		
		elif choice == "2":
			manager.view_students()
		
		elif choice == "3":
			manager.calculate_average()
			
		elif choice == "4":
			manager.save_data_to_file()
			print("Exiting program...")
			break
		
		else:
			print("Invalid choice!")

main()