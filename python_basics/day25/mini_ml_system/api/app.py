from fastapi import FastAPI
from mini_ml_system.schemas.input_schema import InputData
from mini_ml_system.inference.predict import predict
from mini_ml_system.logs.logger import log_event

app=FastAPI()

@app.get("/")
def home():
	return {"status":"ML system running."}

@app.post("/predict")
def prediction(data:InputData):
	try :
		pred,version=predict(data.features)
		log_event(data.features,pred,version,"SUCESS")

		return {"prediction":pred,
		  		"model_version":version,
				"status":"sucess"
				}
	
	except Exception as e:
		log_event(data.features,None,"v1","FAILED")

		return {"error":str(e)}
