#----Validation Layer----

def validate_input(username,password,role,access_level):
	if not isinstance(username,str):
		return False
	
	if not isinstance(password,str):
		return False 
	
	if role not in ["user","admin","manager"]:
		return False
	
	if access_level not in [1,2,3]:
		return False
	
	return True

#----Authentic Layer----

def authenticate(username,password):
	users_db={
		"admin": "admin123",
		"rahul": "rahul123",
		"system": "sys999"
	}
	return users_db.get(username,"Not Found")==password

#----Autherization Layer----

def authorize(role,access_level):
	role_permissions={
		"user": 1,
		"manager": 2,
		"admin": 3
	}
	return role_permissions.get(role,0 )>=access_level

#----Rule Engine----

def acess_decision_engine(username,password,role,access_level):

	#Guard Clause
	if not validate_input(username,password,role,access_level):
		return "Invalid Input Data"

	if not authenticate(username,password):
		return "Authentication Failed!"
	
	if not authorize(role,access_level):
		return "Access Denied(Insuffecient Privileges!)"
	return "Access Granted"


if __name__=="__main__":
	username=input("Enter the username : ")
	password=input("Enter the password : ")
	role=input("Enter the role (user/manager/admin) : ")
	access_level=int(input("Enter access level (1-low,2-mid,3-high) : "))

	result=acess_decision_engine(username,password,role,access_level)
	print("\nSystem Decision : ",result)