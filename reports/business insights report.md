# 📊 Business Insights Report
## AI Credit Risk Analytics Dashboard

---

# Project Summary

This project analyzes historical loan application data to understand customer behavior, identify credit risk, and predict loan approval outcomes using Machine Learning.

The solution combines Python, SQL, Power BI, and Machine Learning to build an end-to-end analytics workflow for financial institutions.

---

# Business Objectives

The project aims to:

- Analyze customer loan applications.
- Identify factors affecting loan approval.
- Classify customers into different risk categories.
- Build predictive models for loan approval.
- Provide interactive dashboards for business users.

---

# Dataset Overview

| Metric | Value |
|---------|------:|
| Total Loan Applications | 614 |
| Features | 20 |
| Training Records | 491 |
| Testing Records | 123 |

---

# Executive Summary

The analysis indicates that customer credit history is the strongest factor influencing loan approval.

Applicants with higher combined income and a positive credit history are significantly more likely to receive loan approval.

The developed Machine Learning model achieved strong predictive performance and can assist financial institutions in making faster and more consistent lending decisions.

---

# Data Cleaning Summary

The following preprocessing tasks were performed:

- Removed missing values
- Handled inconsistent data
- Converted data types
- Feature engineering
- One-Hot Encoding
- Standard Scaling
- Train/Test Split

---

# Feature Engineering

The following business features were created:

| Feature | Description |
|----------|-------------|
| TotalIncome | Applicant + Co-applicant Income |
| LoanToIncomeRatio | Loan Amount / Total Income |
| IncomeCategory | Low, Medium, High, Very High |
| LoanSize | Small, Medium, Large, Very Large |
| ApplicantType | Salaried / Self Employed |
| FamilySize | Estimated household size |
| RiskCategory | Low Risk / High Risk |

These engineered features improved business understanding and supported predictive modeling.

---

# SQL Analytics Summary

Business analysis was performed using MySQL.

Implemented SQL concepts include:

- Data Filtering
- Aggregation
- GROUP BY
- ORDER BY
- Window Functions
- Ranking
- Common Table Expressions (CTE)
- Views
- Business Reporting Queries

---

# Dashboard Summary

The Power BI dashboard contains four interactive pages.

## 1. Executive Dashboard

KPIs:

- Total Applications
- Approved Loans
- Rejected Loans
- Approval Rate
- Average Loan Amount
- Average Income

Purpose:

Provides an overall performance overview of the loan portfolio.

---

## 2. Customer Analytics

Visualizes:

- Gender Distribution
- Education
- Marital Status
- Dependents
- Applicant Type
- Customer Demographics

Purpose:

Helps understand the characteristics of loan applicants.

---

## 3. Financial Analytics

Visualizes:

- Income Distribution
- Loan Amount Distribution
- Loan Size Analysis
- Loan-to-Income Ratio
- Income vs Loan Scatter Plot

Purpose:

Analyzes customer financial capacity and borrowing patterns.

---

## 4. Credit Risk Analytics

Visualizes:

- Risk Category Distribution
- Credit History Analysis
- Loan Approval by Risk
- High Risk Customers
- Loan Size by Risk Category

Purpose:

Supports credit risk assessment and lending decisions.

---

# Machine Learning Summary

Models evaluated:

| Model | Accuracy |
|---------|---------:|
| Logistic Regression | **86.18%** |
| Decision Tree | 70.73% |
| Random Forest | 86.18% |
| Gradient Boosting | 81.30% |

Selected Model:

**Logistic Regression**

Reason:

Although Logistic Regression and Random Forest achieved identical accuracy, Logistic Regression was selected due to its simplicity, interpretability, and strong overall performance.

---

# Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | 86.18% |
| Precision | 84.69% |
| Recall | 97.65% |
| F1 Score | 90.71% |
| ROC-AUC | 85.14% |

---

# Key Business Insights

## Credit History

Applicants with a positive credit history demonstrate significantly higher approval rates.

Credit history is the strongest predictor of loan approval.

---

## Customer Income

Customers with higher total household income are more likely to receive loan approval.

Income remains one of the primary indicators of repayment capability.

---

## Loan Amount

Very large loan requests tend to have lower approval rates than moderate loan requests.

---

## Risk Segmentation

The engineered RiskCategory feature helps categorize applicants into low-risk and high-risk groups, supporting faster credit assessment.

---

## Financial Health

The Loan-to-Income Ratio provides an effective measure of repayment capacity.

Applicants with lower ratios generally exhibit stronger financial stability.

---

# Business Recommendations

Based on the analysis:

1. Prioritize applicants with a strong credit history during loan evaluation.

2. Include the Loan-to-Income Ratio as a standard risk assessment metric.

3. Monitor high-risk applicants more closely before approval.

4. Use predictive analytics to support, not replace, human decision-making.

5. Continue collecting additional customer information to further improve model performance.

---

# Project Outcomes

The project successfully demonstrates:

- Data Cleaning
- Feature Engineering
- SQL Analytics
- Interactive Dashboard Development
- Machine Learning
- Business Intelligence
- Predictive Analytics

The solution provides a scalable framework for analyzing loan applications and supporting credit risk assessment.

---

# Future Enhancements

Potential improvements include:

- Hyperparameter tuning using GridSearchCV
- XGBoost and LightGBM implementation
- SHAP Explainability
- Real-time prediction API using FastAPI
- Automated Power BI data refresh
- Cloud deployment using Azure or AWS

---

# Conclusion

This project demonstrates a complete end-to-end analytics workflow, integrating data engineering, business intelligence, SQL analysis, and machine learning into a single solution.

The developed dashboard and predictive model provide actionable insights that can support financial institutions in making more informed and efficient loan approval decisions.