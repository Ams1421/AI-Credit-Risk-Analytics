# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Project | AI Credit Risk Analytics Dashboard |
| Version | 1.0 |
| Language | Python |
| Database | MySQL |
| Dashboard | Power BI |
| Machine Learning | Scikit-learn |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

# 1. Introduction

This document describes the technical implementation of the AI Credit Risk Analytics Dashboard.

The project combines data engineering, SQL analytics, business intelligence, and machine learning into a unified analytics workflow. The system is designed to process historical loan application data, generate business insights, and predict loan approval outcomes.

---

# 2. System Architecture

```
                  Loan Dataset
                       │
                       ▼
              Python Data Processing
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
 Feature Engineering          Data Cleaning
         │                           │
         └─────────────┬─────────────┘
                       ▼
                Processed Dataset
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
               MySQL Database
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
             SQL Analytics      Machine Learning
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
             Power BI Dashboard
                       │
                       ▼
             Business Insights
```

---

# 3. Technology Stack

## Programming Language

- Python 3.14

Purpose

- Data Processing
- Machine Learning
- Automation

---

## Database

MySQL

Purpose

- Store cleaned loan records
- Execute business queries
- Aggregate analytics

---

## Dashboard

Power BI Desktop

Purpose

- Interactive reports
- Executive dashboards
- Business intelligence

---

## Machine Learning

Scikit-learn

Algorithms

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

---

## Python Libraries

| Library | Purpose |
|----------|----------|
| Pandas | Data Manipulation |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| Joblib | Model Serialization |

---

# 4. Project Folder Structure

```
AI-Credit-Risk-Analytics/
│
├── dataset/
│
├── python/
│   ├── models/
│   ├── outputs/
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_visualization.py
│   ├── 05_feature_engineering.py
│   ├── 06_data_preprocessing.py
│   ├── 07_model_training.py
│   ├── 08_model_evaluation.py
│   └── 09_prediction.py
│
├── mysql/
│
├── powerbi/
│
├── reports/
│
├── images/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 5. Python Workflow

The Python workflow consists of nine independent modules.

## Step 1

Data Loading

Input

- loan_train.csv
- loan_test.csv

Output

- DataFrames

---

## Step 2

Data Cleaning

Operations

- Missing Value Treatment
- Duplicate Checking
- Data Type Validation
- Null Analysis

Output

- processed_data.csv

---

## Step 3

Exploratory Data Analysis

Performed Analysis

- Loan Distribution
- Income Distribution
- Gender Analysis
- Credit History
- Property Area

Output

Charts

---

## Step 4

Visualization

Generated

- Bar Charts
- Histograms
- Pie Charts
- Box Plots
- Scatter Plots

---

## Step 5

Feature Engineering

Generated Features

- TotalIncome
- LoanToIncomeRatio
- IncomeCategory
- LoanSize
- ApplicantType
- FamilySize
- RiskCategory

Output

featured_data.csv

---

## Step 6

Data Preprocessing

Operations

- Train/Test Split
- StandardScaler
- OneHotEncoder
- ColumnTransformer
- Pipeline Preparation

Outputs

- preprocessor.pkl
- X_train.pkl
- X_test.pkl
- y_train.pkl
- y_test.pkl

---

## Step 7

Model Training

Models

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Output

best_pipeline.pkl

---

## Step 8

Model Evaluation

Generated

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Classification Report

Outputs

evaluation_metrics.csv

classification_report.csv

confusion_matrix.png

---

## Step 9

Prediction

Input

loan_test.csv

Output

predictions.csv

---

# 6. Database Design

Database

loan_analysis

Table

loan_applications

Primary Key

Loan_ID

Total Records

614

---

# 7. SQL Analytics

Implemented SQL Concepts

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- Aggregate Functions
- CASE Statements
- Window Functions
- CTE
- Views
- Ranking Functions

---

# 8. Power BI Dashboard

Pages

Executive Dashboard

Customer Analytics

Financial Analytics

Credit Risk Analytics

Each dashboard supports interactive filtering using slicers and cross-filtering between visuals.

---

# 9. Machine Learning Pipeline

The final pipeline uses the following workflow.

```
Raw Dataset
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
Logistic Regression
      │
      ▼
Prediction
```

---

# 10. Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 86.18% |
| Precision | 84.69% |
| Recall | 97.65% |
| F1 Score | 90.71% |
| ROC-AUC | 85.14% |

Selected Model

Logistic Regression

---

# 11. Performance Optimization

The project incorporates several optimization techniques.

- Feature Engineering
- Standard Scaling
- One-Hot Encoding
- Pipeline Automation
- Model Serialization using Joblib
- Modular Python Scripts

These optimizations improve reproducibility and maintainability.

---

# 12. Security Considerations

The current implementation is intended for educational and portfolio purposes.

Future enhancements may include:

- User Authentication
- Role-Based Access Control
- Data Encryption
- Secure Database Credentials
- Audit Logging

---

# 13. Limitations

Current limitations include:

- Static dataset
- No real-time prediction API
- No automated database refresh
- Limited hyperparameter tuning
- No cloud deployment

---

# 14. Future Technical Enhancements

Future improvements may include:

- XGBoost
- LightGBM
- Hyperparameter Optimization using GridSearchCV
- SHAP Explainability
- FastAPI Deployment
- Docker Containerization
- Azure or AWS Cloud Deployment
- CI/CD Pipeline using GitHub Actions

---

# 15. Conclusion

The AI Credit Risk Analytics Dashboard demonstrates a complete technical implementation of a modern analytics solution.

The project integrates Python, SQL, Power BI, and Machine Learning into a modular and scalable architecture capable of supporting business decision-making and predictive analytics.

The modular design enables future expansion with additional data sources, machine learning models, and deployment strategies.