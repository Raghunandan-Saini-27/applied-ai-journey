import random 

def get_system_signals():
	return {
		"accuracy":round(random.uniform(0.6,0.95),2),
		"drift_score":round(random.uniform(0.0,0.5),2),
		"new_data_size":random.randint(0,2000)
		}