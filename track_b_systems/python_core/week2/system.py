balance=1000
daily_withdrawn=0
	
def main():
	system_on=authentication()
	if system_on:
		print("Welcome to the system!\n")

	else :
		print("Access Denied.\n")

	while(system_on):
		print("\n----- SYSTEM CONTROL PANEL -----\n")
		print("1. Check Balance \n")
		print("2. Deposit Money \n")
		print("3. Withdraw money \n")
		print("4. Exit System \n")
		choice=int(input("Choose Option : \n"))
		if choice==1:
			check_balance()

		elif choice==2:
			deposit_money()

		elif choice==3:
			withdraw_money()

		elif choice==4:
			print("System shutting down...\n")
			break

		else :
			print("Invalid Input.Try Again!\n")
		

def check_balance():
	print("\nBalance :",balance)

def deposit_money():
	global balance
	amount=int(input("\nEnter the amount to be added : \n"))
	balance+=amount
	return print(f"\nDeposited : {amount}")

def withdraw_money():
	global balance
	global daily_withdrawn
	daily_limit=25000
	max_limit=10000
	withdraw=int(input("\nEnter the amount to be withdrawn : \n"))
	if withdraw<=0:
		return print("Invalid Input.\n")
	
	elif withdraw>balance:
		return print("Insuffecient Balance.\n")

	elif withdraw>max_limit:
		return print("Max transaction limit exceeded.\n")

	elif withdraw+daily_withdrawn>daily_limit:
		return print("Daily limit reached. Try tommorow.\n")

	else :
		balance-=withdraw
		daily_withdrawn+=withdraw
		return print(f"\nWithdrawal successful : {withdraw}\n")
	
		
def authentication():
	for i in range(3,0,-1):
		password=str(input("Enter the password : \n"))
		if password=="sarghi919":
			print("Correct Password(You may proceed!).\n")
			return True
			
		else :
			print(f"Wrong Password(chances reamining : {i-1})\n")
	return False
			
if __name__=="__main__":
	main()