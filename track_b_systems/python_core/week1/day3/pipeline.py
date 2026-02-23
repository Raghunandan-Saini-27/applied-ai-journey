# Data Pipeline System

def clean_data(data):
	"""Remove Invalid Values(Negative Numbers) """

	cleaned=[]

	for x in data :
		if x>=0:
			cleaned.append(x)

		return cleaned
	
def process_data(data):
	"""Transform data(square each value)"""

	processed=[]
	
	for x in data :
		processed.append(x*x)

	return processed

def analyze_data(data):
	"""Analyze data(Compute Average)"""
	
	if len(data)==0:
		return 0
	
	return sum(data)/len(data)

def pipeline(raw_data):
	step1=clean_data(raw_data)
	step2=process_data(raw_data)
	result=analyze_data(raw_data)
	return result

if __name__=="__main__":
	raw=[10,-5,3,-1,7,2]
	final_result=pipeline(raw)
	print("Final Output :",final_result)