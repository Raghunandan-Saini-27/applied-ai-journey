import pickle 
import numpy as np
with open("mini_ml_system/models/model_v1.pkl","rb") as f:
	model=pickle.load(f)

MODEL_VERSION="v1"

def predict(features:list):
	arr=np.array(features).reshape(1,-1)
	pred=model.predict(arr)

	return float(pred[0]),MODEL_VERSION