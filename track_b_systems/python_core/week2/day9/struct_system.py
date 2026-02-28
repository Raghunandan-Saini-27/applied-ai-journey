MAX_LIMIT=25000
DAILY_LIMIT=50000

class User():
	def __init__(self,username,pin,balance=1000):
		self.username=username
		self.balance=balance
		self.pin=pin
		self.daily_withdrawn=0



user=User(username="Raghu",pin="sarghi919",balance=10000)

def check_balance():
	print("Balance : ",user.balance)

def deposit_amount():
	dep_amount=int(input("Enter the amount to be depsited : \n"))
	if dep_amount<=0:
		print("Invalid Amount. Deosit failed !\n")

	else :
		user.balance+=dep_amount
		print("Amount added successfully : ",dep_amount)

def withdraw_amount():
	wit_amount=int(input("Enter the amount to be withdrawn : \n"))
		
	if wit_amount>user.balance :
		print("Insuffecient Amount. Withdraw Failed !\n")

	elif wit_amount>MAX_LIMIT :
		print("Max transaction limit reached.\n")

	elif wit_amount+user.daily_withdrawn>DAILY_LIMIT :
		print("Daily limit reached. Try again tommorow !")
	
	else :
		user.balance-=wit_amount
		user.daily_withdrawn+=wit_amount
		print("Amount Withdrawn Sucessfully :",wit_amount)

def authentication():
	name=str(input("Enter the username : \n"))
	if name==user.username:
		for i in range(3,0,-1):
			password=str(input("Enter the password : \n"))
			if password==user.pin :
				print(f"System Logged in Sucessfully.\n")
				return True
			
			else :
				print(f"Wrong Pin. {i-1} chances reamining ! !\n")

	else: 
			print(f"Wrong Username.\n")

	return False
	

def main():
	system_on=False
	system_on=authentication()
	while system_on==True:
		print("\n------- SYSTEM CONTROL PANEL -------\n")
		print(f"\n------- User : {user.username} -------\n")
		print("1. Check Balance Amount\n")
		print("2. Deposit Amount\n")
		print("3. Withdraw Amount\n")
		print("4. Exit System\n")

		choice=int(input("Enter the choice : \n"))
		if choice==1:
			check_balance()
		
		elif choice==2:
			deposit_amount()
		
		elif choice==3:
			withdraw_amount()

		elif choice==4:
			print("System shutting down...")
			break

		else:
			print("invalid Choice !")
		

if __name__=="__main__":
	main()