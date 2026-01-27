# 📅 Day 21: Probability Thresholds & Decision Tuning

## 📌 Objective
Understand how changing probability thresholds affects model decisions and evaluation metrics such as Precision, Recall, and F1-score.

---

## 📊 Dataset Used
**Breast Cancer Dataset** from `sklearn.datasets`

- Binary classification problem
- Target values:
  - 0 → Malignant (cancer)
  - 1 → Benign (non-cancer)
- Commonly used in medical AI evaluation

---

## 🤖 Model Used
**Logistic Regression**

- Outputs probabilities instead of direct class labels
- Default classification threshold = 0.5
- Threshold can be changed to control model behavior

---

## 🔢 What Is a Probability Threshold?
A probability threshold decides when a prediction is considered positive.

Example:
- Probability ≥ threshold → class 1
- Probability < threshold → class 0

The default threshold (0.5) is not always optimal.

---

## 🔄 Thresholds Tested
The following thresholds were evaluated:
- 0.3 → Lenient (high recall)
- 0.5 → Balanced (default)
- 0.7 → Strict (high precision)

---

## 📈 Observations

### Lower Threshold (0.3)
- Higher recall
- Lower precision
- Fewer missed positive cases

### Default Threshold (0.5)
- Balanced precision and recall

### Higher Threshold (0.7)
- Higher precision
- Lower recall
- Fewer false positives

---

## 📊 Metrics Used

### Precision
Measures how accurate positive predictions are.

### Recall
Measures how many actual positives are correctly identified.

### F1 Score
Balances precision and recall and penalizes imbalance.

---

## 🏥 Real-World Decision
For medical diagnosis:
- **Recall is more important**
- Missing a disease case is more dangerous than a false alarm
- Lower or moderate thresholds are preferred

---

## 🧠 Key Learnings
- Models output probabilities, not decisions
- Thresholds control model behavior
- Metric selection depends on real-world cost
- Applied AI focuses on decisions, not just accuracy

---

## 🚀 Conclusion
This task demonstrated how probability thresholds allow engineers to tune model behavior based on real-world requirements, making machine learning systems practical and responsible.
