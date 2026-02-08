def should_retrain(accuracy,drift_score,new_data_size):
	if accuracy < 0.7:
		return True,"Low accuracy detected"
	
	if drift_score > 0.3 :
		return True,"High data drift detected"
	
	if new_data_size > 1000 :
		return True,"New data threshold reached"
	
	return False,"System stable"