# 📅 Day 18: Model Evaluation using Regression Metrics

## 📌 Objective
Learn how to evaluate a **regression model** using standard evaluation metrics and understand how well a trained model performs on **unseen data**.

---

## 📊 Dataset Used
**Diabetes Dataset** from `sklearn.datasets`

- Contains medical features related to diabetes
- Target variable represents a quantitative disease progression measure
- Used commonly for learning regression tasks

### Dataset Structure
- **X (features)** → Input variables
- **y (target)** → Continuous output value to predict

---

## 🔄 Train-Test Split
The dataset is split into:
- **Training data** → Used to train the model
- **Testing data** → Used to evaluate model performance on unseen data

This helps prevent overfitting and provides a realistic measure of model accuracy.

---

## 🤖 Model Used: Linear Regression
Linear Regression is a supervised learning algorithm used to predict **continuous values**.

The model learns a relationship of the form:
\[
y = mx + b
\]

Where:
- `x` → input features
- `y` → predicted output
- `m`, `b` → learned parameters

---

## 📈 Evaluation Metrics Used

### 1️⃣ Mean Absolute Error (MAE)
MAE measures the **average absolute difference** between actual and predicted values.

MAE = (1/n)(y_{actual} - y_{predicted})

- Easy to interpret
- Lower value indicates better performance
- Represents average prediction error in original units

---

### 2️⃣ Mean Squared Error (MSE)
MSE measures the **average squared difference** between actual and predicted values.

MSE =  (1/n)[y_{actual} - y_{predicted}]^2

- Penalizes large errors more than MAE
- Useful when large errors are especially undesirable
- Lower value indicates better performance

---

### 3️⃣ R² Score (Coefficient of Determination)
R² measures how well the model explains the **variance in the target data**.

- **R² = 1** → Perfect model
- **R² = 0** → Model performs no better than predicting the mean
- **R² < 0** → Model performs worse than random guessing

---

## 📌 Results & Observation
- The model achieves a moderate R² score (~0.45)
- This means the model explains approximately **45% of the variance** in the data
- The model performs reasonably well but has room for improvement

---

## 🧠 Key Learnings
- Model evaluation is critical to understand real-world performance
- Training accuracy alone is not sufficient
- Different metrics capture different aspects of error
- R² provides insight into model usefulness, not just error size

---

## 🚀 Conclusion
This task strengthened understanding of:
- Regression model evaluation
- Importance of MAE, MSE, and R²
- Train-test split for fair evaluation

These concepts are fundamental for building reliable Applied AI systems.
