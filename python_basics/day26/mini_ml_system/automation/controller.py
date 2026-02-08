from mini_ml_system.automation.monitoring_signals import get_system_signals
from mini_ml_system.automation.retrain_logic import should_retrain
from mini_ml_system.automation.actions import system_action

def system_controller():
	signals = get_system_signals()
	decision,reason=should_retrain(accuracy=signals["accuracy"],
								drift_score=signals["drift_score"],
								new_data_size=signals["new_data_size"])
	action=system_action(decision,reason)
	
	return {"signals":signals,
		 	"retrain":decision,
			"reason":reason,
			"action":action}