# Day 24 — Logistic Regression Model Deployment with FastAPI

## Overview
This project demonstrates how to deploy a trained Machine Learning model
(Logistic Regression) using FastAPI and expose it as a REST API.

The model predicts whether a tumor is malignant or benign using the
Breast Cancer dataset from scikit-learn and also returns prediction confidence.

---

## Dataset
- Source: sklearn.datasets.load_breast_cancer
- Total features: 30
- Target:
  - 0 → Malignant
  - 1 → Benign

---

## Model
- Algorithm: Logistic Regression
- Training:
  - Data split into training and testing sets
  - Model trained on training data only
- Output:
  - Class prediction
  - Probability score using `predict_proba`

---

## API Endpoints

### GET /
Checks if the API is running.

Response:
