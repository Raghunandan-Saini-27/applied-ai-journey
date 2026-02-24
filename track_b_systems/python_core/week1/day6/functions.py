def classify_number(n):
	if n>0:
		return "Positive"
	
	elif n<0:
		return "Negative"
	
	else :
		return "Zero"
	
def main():
	num=int(input("Enter the number :"))
	result=classify_number(num)
	print("Result :",result)

if __name__=="__main__":
	main()