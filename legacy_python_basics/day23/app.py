from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Loading Trained Model

with open("model.pkl","rb") as f :
	model=pickle.load(f)

app=FastAPI()

class InputData(BaseModel):
	features:list[float]


@app.get("/")
def home():
	return {"message":"ML model api is running."}

@app.post("/predict")
def predict(data:InputData):
	features_array=np.array(data.features).reshape(1,-1)
	prediction=model.predict(features_array)

	return {"Prediction": prediction[0]}
