def decision_engine(confidence,risk_score):
	if confidence < 0.6 :
		return "Low confidence -> human review"
	
	if risk_score > 0.7 :
		return "High risk -> block prediction"
	
	return "Autro-approve prediction"