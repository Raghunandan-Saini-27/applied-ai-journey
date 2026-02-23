def classify_numbers(x):
	if x>0:
		return "Positive"

	elif x<0:
		return "Negative"

	else :
		return "Zero"

if __name__=="__main__":
	num=int(input("Enter number :"))
	result=classify_numbers(num)
	print("Result :",result)