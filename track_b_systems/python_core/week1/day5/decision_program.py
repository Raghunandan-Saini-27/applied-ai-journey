def check_voting_eligibility(age):
	if age<=0:
		return "Invalid age."
	
	elif age<18:
		return "Not Eligible to vote."
	
	else :
		return "Eligible to vote."
	
def check_driving_eligibility(age):
	if age<0:
		return "Invalid age."

	elif age<18:
		return "Not Eligible to drive."

	else :
		return "Eligible to drive."

def check_senior_citizen_eligibility(age):
	if age<0:
		return "Invalid age."

	elif age<60:
		return "Not a senior citizen."
	
	else:
		return "Senior Citizen."

def main():
	try :
		age=int(input("Enter the age :"))
		result1=check_voting_eligibility(age)
		result2=check_driving_eligibility(age)
		result3=check_senior_citizen_eligibility(age)
		print(f"Voting Eligibility : {result1} \nDriving Eligibility : {result2} \nSenior Citizen eligibility : {result3}")

	except ValueError :
		print("Please enter a valid number.")

if __name__=="__main__":
	main()