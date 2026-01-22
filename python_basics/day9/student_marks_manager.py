# Mini Project: Student Marks Manager

'''-> What this program will do
'''

'''1) Add student marks'''
students={}
def add_student():
	global students
	n_1=int(input("Enter the number of the students :"))
	n_2=int(input("Enter the number of subjects :"))

	for i in range(n_1):
		stu_marks={}
		stu_name=input("Name of the student :")
		for j in range(n_2):
			sub=input("Enter the name of the subject :")
			marks=int(input(f"Enter the marks for the {sub} :"))
			stu_marks[sub]=marks
		students[stu_name]=stu_marks



'''
2) View all students
'''
def view_students():
	if not students :
		print("No student data available.")
		return
	
	for name ,marks in students.items():
		print(f"{name}->{marks}")

'''
3) Calculate average marks
'''
def calculate_average():
	global students
	for name,subjects in students.items(): 
		avg=sum(subjects.values())/len(subjects.values())
		print(f"Avg of {name}:{avg}")


'''
4) Save data to a file
'''

def save_data_to_file():
	global students
	with open("students_data.txt","w") as f:
		for name,subjects in students.items():
			subject_marks=[]
			for sub,mark in subjects.items():
				subject_marks.append(f"{sub}:{mark}")
			line=name+"|"+",".join(subject_marks)
			f.write(line+"\n")
	print("Data Saved Sucessfully.")
'''
5)Load data from a file
'''

def load_students_from_file():
	global students
	try:
		with open("students_data.txt","r") as f:
			for line in f:
				line=line.strip()

				if not line:
					continue
				name,data=line.split("|")
				subjects={}

				for item in data.split(","):
					sub,mark=item.split(":")
					subjects[sub]=int(mark)
				students[name]=subjects

	except FileNotFoundError:
		pass


def main():
    load_students_from_file()

    while True:
        print("\n--- Student Marks Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average")
        print("4. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            save_data_to_file()
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

main()