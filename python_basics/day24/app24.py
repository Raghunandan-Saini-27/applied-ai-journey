# API side

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

with open("model24.pkl","rb") as f:
	model=pickle.load(f)

app=FastAPI()

class InputData(BaseModel):
	features:list[float]
	
@app.get("/")
def home():
	return {"message":"model api is running."}

@app.post("/predict")
def predict(data:InputData):
	features_array=np.array(data.features).reshape(1,-1)
	prediction=model.predict(features_array)
	predict_probability=model.predict_proba(features_array)
	return {"prediction":prediction[0].item(),"probability":predict_probability[0,1].item(),
		 "threshold":0.5,"status":"prediction sucessfull"} 