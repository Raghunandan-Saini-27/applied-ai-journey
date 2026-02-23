import datetime
def log_message(msg):
	with open("log.txt","a") as f:
		f.write(f"{datetime.datetime.now()}-{msg}\n")

if __name__ == "__main__" :
		msg = input("Enter message :")
		log_message(msg)
		print("Logged")