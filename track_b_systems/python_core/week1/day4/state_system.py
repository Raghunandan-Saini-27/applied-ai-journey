# Day-4 Stateful System

from datetime import datetime

class MemorySystem:
	def __init__(self):
		self.history=[]			# System Memory(state)

	def process(self,value):
		result= "Positive" if value>0 else "Negative"
		time=datetime.now()

		# Store in memory	
		record={
			"input":value,
			"result":result,
			"timestamp":time	
			}
		self.history.append(record)

		return result
	
	def show_memory(self):
		return self.history
	
# runtime control
if __name__=="__main__":
	system=MemorySystem()

	print(system.process(10))
	print(system.process(-5))
	print(system.process(20))

	print("\nSystem Memory :")
	print(system.show_memory())