# 📅 Day 22: Serving ML Models with FastAPI

## 🎯 Objective
Learn how machine learning models are exposed as APIs using FastAPI so they can be accessed by real applications.

---

## 🔌 What is FastAPI?
FastAPI is a Python framework used to build APIs quickly and efficiently.

In Applied AI, APIs are used to:
- Send input data to a model
- Get predictions as responses
- Integrate ML into apps and systems

---

## 🧠 Why APIs are Needed for ML
Machine learning models cannot be used directly by users.

Instead of running Python scripts manually, we expose models through APIs so:
- Mobile apps can use them
- Web apps can call them
- Hackathon demos work smoothly

---

## 🔁 ML Deployment Flow

User/App → API Request → ML Model → Prediction → API Response

FastAPI acts as the bridge between users and the model.

---

## 📦 API Endpoints Implemented

### GET `/`
Used to check whether the API is running.

### POST `/predict`
- Accepts numerical input
- Runs prediction logic
- Returns result as JSON

---

## 📥 Example Input

```json
{
  "values": [30, 40, 50]
}
