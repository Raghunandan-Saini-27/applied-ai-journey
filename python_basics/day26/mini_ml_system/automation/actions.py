def trigger_retraining(reason):
	return f"Retraining triggerred due to :{reason}"

def system_action(decision,reason):
	if decision:
		return trigger_retraining(reason)
	
	else:
		return "No action required"