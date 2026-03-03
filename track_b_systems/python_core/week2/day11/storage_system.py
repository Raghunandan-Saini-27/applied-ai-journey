import json
import os

#======= CONFIG LAYER =======#

DATA_FILE="user_data.json"

#======= DATA MODEL =======#

class User:
	def __init__(self,username,pin,balance=1000,daily_withdrawn=0):
		self.username=username
		self.pin=pin
		self.balance=balance
		self.daily_withdrawn=daily_withdrawn

	def to_dict(self):
		return {
			"username":self.username,
			"pin":self.pin,
			"balance":self.balance,
			"daily_withdrawn":self.daily_withdrawn
		}
	
	@staticmethod
	def from_dict(data):
		return User(
			username=data["username"],
			pin=data["pin"],
			balance=data["balance"],
			daily_withdrawn=data["daily_withdrawn"]
		)
	
#======= STORAGE LAYER =======#

class StorageManager:
	@staticmethod
	def save_user(user: User):
		with open (DATA_FILE,"w") as f:
			json.dump(user.to_dict(),f,indent=4)

	@staticmethod
	def load_user():
		if not os.path.exists(DATA_FILE):
			return None
		
		with open(DATA_FILE,"r") as f:
			data=json.load(f)
			return User.from_dict(data)
		
#======= AUTH LAYER =======#

def authenticate(user : User):
	for i in range(3,0,-1):
		name=input("Enter the username : ")
		pin=input("Enter pin : ")
		
		if name==user.username and pin ==user.pin:
			print("Login succesful. \n") 
			return True

		else :
			print(f"Wrong credentials. Attempts left : {i-1}. \n")

	return False
	
#======= BUSINESS LOGIC =======#

def check_balance(user):
	print("Balance : ",user.balance)

def deposit(user):
	amt=int(input("Enter amount : "))
	if amt>0:
		user.balance+=amt
		print("Deposited : ",amt)

	else :
		print("Invalid amount.")

def withdraw(user):
	amt=int(input("Enter anount : "))
	if amt<=0:
		print("Invalid amount.")
	
	elif amt > user.balance:
		print("Insuffecient Balance.")

	else :
		user.balance-=amt
		user.daily_withdrawn+=amt
		print("Withdrawn : ",amt)

#======== CONTROLLER =======#

def system_controller(user):
	system_on=True
	while system_on:
		print("\n--- SYSTEM PANEL ---\n")
		print("1. Balance")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Exit")

		choice=int(input("Choose : "))

		if choice==1:
			check_balance(user)

		elif choice==2:
			deposit(user)

		elif choice==3:
			withdraw(user)

		elif choice==4:
			print("Saving system state...")
			StorageManager.save_user(user)		#Persistance on shutdown
			system_on=False

		else:
			print("Invalid Choice.")
	
#======== SYSTEM LIFECYCLE =======#

def system_boot():
	user=StorageManager.load_user()
	if user is None:
		print("No data found. Creating new user.")

		user=User(username="Raghu",pin="sarghi919")
		StorageManager.save_user(user)
	return user

def system_run(user):
	if authenticate(user):
		system_controller(user)

	else :
		print("System Locked.")
	
def system_shutdown():
	print("System shutdown complete.")

#======== MAIN =======#

def main():
	user=system_boot()		#LOAD STATE
	system_run(user)		#RUN SYSTEM
	system_shutdown()		#SHUTDOWN

if __name__=="__main__":
	main()