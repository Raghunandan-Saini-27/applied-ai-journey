from datetime import datetime

LOG_FILE="mini_ml_system/logs/system.log"

def log_event(input_data,prediction,model_version,status):
	with open(LOG_FILE,"a") as f :
		f.write(f"{datetime.now()} | {input_data} | {prediction} | {model_version} | {status}\n")