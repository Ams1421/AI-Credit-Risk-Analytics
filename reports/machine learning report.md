# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Project | AI Credit Risk Analytics Dashboard |
| Machine Learning Library | Scikit-learn |
| Problem Type | Binary Classification |
| Dataset | Loan Prediction Dataset |
| Best Model | Logistic Regression |
| Model Accuracy | 86.18% |

---

# 1. Introduction

This report documents the Machine Learning implementation used in the AI Credit Risk Analytics Dashboard.

The objective is to develop a predictive model capable of determining whether a loan application is likely to be approved or rejected based on applicant demographics, financial information, and credit history.

The solution follows a complete Machine Learning lifecycle, including data preprocessing, feature engineering, model training, evaluation, and prediction.

---

# 2. Business Problem

Financial institutions process thousands of loan applications every day.

Traditional manual evaluation is:

- Time-consuming
- Resource-intensive
- Susceptible to inconsistencies

Machine Learning provides an opportunity to support credit analysts by predicting loan approval outcomes using historical data.

---

# 3. Problem Statement

Develop a supervised machine learning model that predicts the loan approval status of applicants.

Target Variable:

```
Loan_Status

Y = Approved

N = Rejected
```

Problem Type:

```
Binary Classification
```

---

# 4. Dataset Overview

| Attribute | Value |
|-----------|------:|
| Total Records | 614 |
| Training Records | 491 |
| Testing Records | 123 |
| Features | 20 |
| Target Variable | Loan_Status |

---

# 5. Data Preprocessing

The following preprocessing operations were performed:

- Missing value handling
- Data validation
- Feature engineering
- Train-test split
- StandardScaler
- OneHotEncoder
- ColumnTransformer
- Scikit-learn Pipeline

These steps ensure consistent preprocessing during both training and prediction.

---

# 6. Feature Engineering

The following derived features were created:

| Feature | Description |
|----------|-------------|
| TotalIncome | Applicant + Co-applicant Income |
| LoanToIncomeRatio | Loan Amount / Total Income |
| IncomeCategory | Income Segmentation |
| LoanSize | Loan Size Classification |
| ApplicantType | Salaried / Self Employed |
| FamilySize | Estimated Household Size |
| RiskCategory | Credit Risk Classification |

Feature engineering improved the model's ability to capture meaningful business patterns.

---

# 7. Machine Learning Pipeline

The project uses a Scikit-learn Pipeline to automate preprocessing and prediction.

```
Loan Dataset
      │
      ▼
Missing Value Handling
      │
      ▼
Feature Engineering
      │
      ▼
Train-Test Split
      │
      ▼
ColumnTransformer
      │
      ├── StandardScaler
      └── OneHotEncoder
      │
      ▼
Classification Model
      │
      ▼
Prediction
```

---

# 8. Algorithms Evaluated

Four classification algorithms were trained and compared.

### Logistic Regression

Advantages:

- Fast
- Interpretable
- Performs well on structured data

---

### Decision Tree

Advantages:

- Easy to understand
- Rule-based decision making

---

### Random Forest

Advantages:

- Ensemble learning
- Reduces overfitting
- High prediction accuracy

---

### Gradient Boosting

Advantages:

- Sequential learning
- High predictive capability

---

# 9. Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|---------:|----------:|--------:|---------:|
| Logistic Regression | **86.18%** | 84.69% | 97.65% | 90.71% |
| Decision Tree | 70.73% | 81.82% | 74.12% | 77.78% |
| Random Forest | 86.18% | 86.96% | 94.12% | 90.40% |
| Gradient Boosting | 81.30% | 83.70% | 90.59% | 87.01% |

---

# 10. Selected Model

Selected Model

```
Logistic Regression
```

Reason:

Although Logistic Regression and Random Forest achieved identical accuracy, Logistic Regression was selected because:

- Simpler architecture
- Faster inference
- Easier interpretation
- Lower computational complexity
- Comparable predictive performance

---

# 11. Model Evaluation

The selected model achieved the following performance:

| Metric | Score |
|---------|------:|
| Accuracy | 86.18% |
| Precision | 84.69% |
| Recall | 97.65% |
| F1 Score | 90.71% |
| ROC-AUC | 85.14% |

---

# 12. Confusion Matrix

The confusion matrix summarizes prediction performance.

- True Positives
- True Negatives
- False Positives
- False Negatives

The matrix is generated automatically and stored as:

```
python/outputs/confusion_matrix.png
```

---

# 13. Classification Report

The classification report contains:

- Precision
- Recall
- F1 Score
- Support

Generated File:

```
classification_report.csv
```

---

# 14. Prediction Pipeline

The prediction workflow is fully automated.

```
New Loan Application
        │
        ▼
Feature Engineering
        │
        ▼
Saved Pipeline
        │
        ▼
Prediction
        │
        ▼
Approved / Rejected
```

The trained pipeline ensures consistent preprocessing during prediction.

---

# 15. Business Impact

The predictive model can help financial institutions:

- Reduce manual loan evaluation time.
- Support credit analysts with data-driven recommendations.
- Improve consistency in approval decisions.
- Identify high-risk applicants earlier.
- Enhance operational efficiency.

---

# 16. Limitations

Current limitations include:

- Limited dataset size.
- Static historical data.
- No hyperparameter tuning.
- No external credit score integration.
- No explainable AI (SHAP/LIME).

---

# 17. Future Improvements

Potential enhancements include:

- Hyperparameter Optimization using GridSearchCV.
- XGBoost and LightGBM models.
- Cross-validation.
- SHAP Explainability.
- Model deployment using FastAPI.
- Real-time prediction API.
- Cloud deployment using Azure or AWS.
- Continuous model monitoring.

---

# 18. Conclusion

The Machine Learning component successfully demonstrates the complete lifecycle of a predictive analytics solution.

By integrating preprocessing, feature engineering, model comparison, evaluation, and prediction into a reusable pipeline, the project provides a scalable and maintainable approach to loan approval prediction.

The final Logistic Regression model achieved an accuracy of **86.18%**, making it a suitable baseline model for supporting credit risk assessment and lending decisions.