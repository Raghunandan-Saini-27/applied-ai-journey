# 📅 Day 23 — Deploying an ML Model with FastAPI

## 🎯 Objective

Build an end-to-end **Applied AI pipeline** where a machine learning model is:

1. Trained offline
2. Saved to disk
3. Loaded into a FastAPI application
4. Exposed through an API endpoint for real-time predictions

This mirrors how ML models are actually used in real-world applications and hackathons.

---

## 📊 Dataset

**Diabetes Dataset (scikit-learn)**

* Features (`X`): Medical measurements
* Target (`y`): Disease progression score

The dataset is split into training and testing sets before training.

---

## 🧠 Concepts Covered

* Offline vs Online Machine Learning
* Model training using `LinearRegression`
* Model serialization using `pickle`
* Loading a trained model into memory
* Creating API endpoints with FastAPI
* Input validation using `BaseModel`
* Returning ML predictions as JSON

---

## 📁 Project Structure

```
Day_23/
 ├── train_model.py   # Train and save ML model
 ├── app.py           # FastAPI app that serves predictions
 ├── model.pkl        # Saved trained model
 └── README.md
```

---

## 🚀 How to Run

### 1️⃣ Train the Model

```bash
python train_model.py
```

This will create a `model.pkl` file.

### 2️⃣ Start the API Server

```bash
python -m uvicorn app:app --reload
```

---

## 🧪 How to Test

1. Open browser: `http://127.0.0.1:8000/docs`
2. Use the `/predict` endpoint
3. Provide input in JSON format:

```json
{
  "features": [0.05, -0.04, 0.06, 0.02, -0.02, -0.03, 0.01, -0.01, 0.02, -0.02]
}
```

### Sample Response

```json
{
  "prediction": 160.23
}
```

---

## 🧠 Key Takeaways

* ML models should be trained once and reused
* APIs act as bridges between users and ML models
* `pickle` allows model reuse without retraining
* FastAPI + ML = real-world AI deployment

---

## ✅ Outcome

A fully working **ML-powered API** capable of accepting input data and returning predictions in real time — a core Applied AI skill.
