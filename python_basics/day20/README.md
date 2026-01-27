# 📅 Day 20: Classification Metrics – Precision, Recall & F1 Score

## 📌 Objective
Understand why **accuracy alone is not sufficient** for evaluating classification models and learn how to use **Precision, Recall, and F1-score** for better real-world decision making.

---

## 📊 Dataset Used
**Breast Cancer Dataset** from `sklearn.datasets`

- Medical dataset used for binary classification
- Target labels:
  - `0` → Malignant (cancer)
  - `1` → Benign (non-cancer)
- Widely used to understand classification metrics in healthcare scenarios

---

## 🤖 Model Used
**Logistic Regression**

- A classification algorithm that predicts probabilities
- Uses a threshold (default 0.5) to decide class labels
- Suitable for binary classification problems

---

## 🔄 Train-Test Split
The dataset is divided into:
- **Training data** → Used to train the model
- **Testing data** → Used to evaluate model performance on unseen data

This ensures the evaluation reflects real-world behavior.

---

## ❌ Why Accuracy Is Not Enough
Accuracy only measures overall correctness and can be misleading, especially for **imbalanced datasets**.

Example:
- If 95% data belongs to one class, a model predicting only that class can still achieve 95% accuracy while being useless.

---

## 📈 Evaluation Metrics Used

### 1️⃣ Accuracy
Measures how many predictions were correct overall.

Accuracy = {Correct Predictions}/{Total Predictions}

---

### 2️⃣ Precision
Measures how **reliable positive predictions** are.

Precision = {TP}/{TP + FP}

- High precision → fewer false alarms
- Important when false positives are costly

---

### 3️⃣ Recall
Measures how many **actual positive cases** the model correctly identifies.

Recall = {TP}/{TP + FN}

- High recall → fewer missed cases
- Very important in healthcare and safety-critical systems

---

### 4️⃣ F1 Score
Harmonic mean of Precision and Recall.

F1 = {2(Precision\Recall)}{Precision + Recall}


- Useful when dataset is imbalanced
- Penalizes extreme imbalance between precision and recall

---

## 📌 Confusion Matrix
The confusion matrix helps visualize prediction results:

| Actual \ Predicted | Positive				| Negative			  |
|--------------------|----------------------|---------------------|
| Positive			 | True Positive (TP)   | False Negative (FN) |
| Negative		 	 | False Positive (FP)  | True Negative (TN)  |

- **FN** is most dangerous in healthcare (missed disease cases)
- **FP** causes false alarms

---

## 🧠 Key Learnings
- Accuracy can be misleading
- Precision focuses on correctness of positive predictions
- Recall focuses on catching all actual positives
- F1-score balances both
- Metric choice depends on the problem, not the algorithm

---

## 🚀 Conclusion
This task helped build a strong understanding of **classification evaluation metrics**, which are essential for real-world Applied AI systems, especially in healthcare and safety-critical applications.