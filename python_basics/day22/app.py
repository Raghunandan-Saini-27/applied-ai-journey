from fastapi import FastAPI
from pydantic import BaseModel

# 🛠 DAY 22 MINI TASK (CONCEPTUAL + LIGHT CODING)

'''
Write a FastAPI file (app.py) that:

1) Has /

2) Has /predict (dummy prediction is fine)'''

# DAY 22: From Model → API (FastAPI)

'''
🧠 Goal for Today

By the end of Day 22, you will understand:

1) How an ML model becomes a service

2) How predictions are accessed via an API

3) How hackathons & real products use models'''


'''1️⃣ What is an API? (AI Context)

An API is:

A door that allows other programs to talk to your model.'''

# 1️⃣ Create FastAPI app
app = FastAPI()

# 2️⃣ Define input structure
class StudentData(BaseModel):
    marks: list[int]

# 3️⃣ Home route (health check)
@app.get("/")
def home():
    return {"message": "AI API is running successfully"}

# 4️⃣ Prediction route
@app.post("/predict")
def predict(data: StudentData):
    avg_marks = sum(data.marks) / len(data.marks)

    if avg_marks >= 60:
        result = "Pass"
    else:
        result = "Fail"

    return {
        "average": avg_marks,
        "prediction": result
    }
