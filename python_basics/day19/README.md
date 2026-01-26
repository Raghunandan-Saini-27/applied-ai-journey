# 📅 Day 19: Classification using Logistic Regression

## 📌 Objective
Understand **classification problems** in Machine Learning and implement a **Logistic Regression** model.  
Learn how to evaluate classification models using **Accuracy** and **Confusion Matrix**.

---

## 📊 Dataset Used
**Breast Cancer Dataset** from `sklearn.datasets`

- Each row represents a medical record
- Features include tumor characteristics (mean radius, texture, smoothness, etc.)
- Target labels:
  - `0` → Malignant
  - `1` → Benign

### Why this dataset?
It is a **real-world healthcare dataset**, ideal for learning classification and evaluation metrics.

---

## 🔍 What is Classification?
Classification is a type of Machine Learning task where the model predicts **categories or classes** instead of numerical values.

### Examples:
- Spam / Not Spam
- Disease / No Disease
- Fraud / Not Fraud

This is different from **regression**, which predicts continuous values like prices or marks.

---

## 🤖 Model Used: Logistic Regression
Despite the name, **Logistic Regression is a classification algorithm**.

- It predicts **probabilities** between 0 and 1
- These probabilities are converted into class labels using a threshold (usually 0.5)

---

## 🔄 Train-Test Split
The dataset is split into:
- **Training data** → used to train the model
- **Testing data** → unseen data used to evaluate performance

This helps check how well the model generalizes to real-world data.

---

## 📈 Evaluation Metrics Used

### 1️⃣ Accuracy
**Accuracy** measures how many predictions were correct.

Accuracy = Correct Predictions\Total Predictions

- Easy to understand
- Can be misleading for imbalanced datasets

---

### 2️⃣ Confusion Matrix
A confusion matrix gives a **detailed breakdown** of predictions.

|                 | Predicted Positive  | Predicted Negative  |
|-----------------|---------------------|---------------------|
| Actual Positive | True Positive (TP)  | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN)  |

#### Explanation:
- **TP** → Correctly predicted positive case
- **TN** → Correctly predicted negative case
- **FP** → False alarm
- **FN** → Missed detection (often dangerous in healthcare)

Confusion matrix helps understand **what kind of mistakes** the model is making.

---

## 📌 Results & Observation
- The model achieves good accuracy on test data
- Confusion matrix shows how predictions are distributed
- Logistic Regression performs reasonably well for this dataset

However:
- Accuracy alone is not enough in critical domains
- Metrics like **Precision, Recall, and F1-score** become important in imbalanced datasets

---

## 🧠 Key Learnings
- Classification predicts **classes**, not numbers
- Logistic Regression is probability-based
- Evaluation metrics are essential to judge real-world performance
- Confusion matrix gives deeper insight than accuracy alone

---

## 🚀 Conclusion
This task helped build a strong foundation in:
- Classification problems
- Logistic Regression
- Model evaluation using classification metrics

This knowledge is essential for real-world Applied AI projects.