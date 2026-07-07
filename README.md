# 🏦 AI Credit Risk Analytics Dashboard

An end-to-end **Data Analytics and Machine Learning** project that predicts loan approval decisions, analyzes customer credit risk, and provides interactive business dashboards using **Python, MySQL, Power BI, and Machine Learning**.

---

# 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Evaluating applicant eligibility manually is time-consuming and prone to inconsistencies.

This project demonstrates how data analytics and machine learning can be used to:

- Analyze loan applications
- Identify customer risk categories
- Predict loan approval
- Generate business insights
- Visualize key metrics using Power BI

---

# 🎯 Objectives

- Clean and preprocess loan application data
- Perform exploratory data analysis (EDA)
- Engineer meaningful business features
- Analyze loan applications using SQL
- Build interactive Power BI dashboards
- Train multiple Machine Learning models
- Predict loan approval status
- Generate business insights for decision-makers

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Power BI |
| Machine Learning | Scikit-learn |
| Database | MySQL |
| SQL | MySQL Workbench |
| Version Control | Git & GitHub |
| IDE | VS Code |

---

# 📂 Project Structure

```text
AI-Credit-Risk-Analytics/
│
├── dataset/
│   ├── loan_train.csv
│   ├── loan_test.csv
│   ├── processed_data.csv
│   └── featured_data.csv
│
├── python/
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_visualization.py
│   ├── 05_feature_engineering.py
│   ├── 06_data_preprocessing.py
│   ├── 07_model_training.py
│   ├── 08_model_evaluation.py
│   ├── 09_prediction.py
│   │
│   ├── models/
│   │     best_pipeline.pkl
│   │     preprocessor.pkl
│   │
│   └── outputs/
│         predictions.csv
│         model_metrics.csv
│         evaluation_metrics.csv
│         classification_report.csv
│         confusion_matrix.png
│
├── mysql/
│     loan_analysis.sql
│
├── powerbi/
│     loan_dashboard.pbix
│
├── images/
│
├── reports/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dataset

The project uses the **Loan Prediction Dataset**.

Dataset includes:

- Applicant Information
- Income
- Co-applicant Income
- Education
- Property Area
- Credit History
- Loan Amount
- Loan Status

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Missing value handling
- Duplicate removal
- Data type correction
- Feature engineering
- OneHot Encoding
- Standard Scaling
- Train-Test Split
- ML Pipeline using Scikit-learn

---

# ⚙️ Feature Engineering

New business features created:

- Total Income
- Loan-to-Income Ratio
- Income Category
- Loan Size
- Applicant Type
- Family Size
- Risk Category

---

# 📈 Exploratory Data Analysis

Performed detailed analysis including:

- Loan Approval Distribution
- Income Analysis
- Loan Amount Distribution
- Property Area Analysis
- Credit History Analysis
- Customer Demographics
- Risk Category Analysis

---

# 🗄️ SQL Analytics

Implemented SQL analysis using MySQL.

Topics covered:

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- Aggregate Functions
- Window Functions
- CTE
- Views
- Ranking Functions
- Business Queries

---

# 📊 Power BI Dashboard

The dashboard consists of **4 interactive pages**.

### Executive Dashboard

- Total Applications
- Approved Loans
- Rejected Loans
- Approval Rate
- Average Income
- Average Loan Amount

---

### Customer Analytics

- Gender Distribution
- Education Analysis
- Marital Status
- Dependents
- Applicant Type
- Customer Demographics

---

### Financial Analytics

- Income Distribution
- Loan Size Analysis
- Loan Amount Distribution
- Income vs Loan Scatter Plot
- Loan-to-Income Ratio

---

### Credit Risk Analytics

- Risk Category Distribution
- Credit History Analysis
- Loan Approval by Risk
- High Risk Customers
- Loan Size by Risk

---

# 🤖 Machine Learning

Models Trained:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

Best Model:

**Logistic Regression**

---

# 📊 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **86.18%** |
| Precision | **84.69%** |
| Recall | **97.65%** |
| F1 Score | **90.71%** |
| ROC-AUC | **85.14%** |

---

# 📁 Generated Outputs

The project automatically generates:

- predictions.csv
- model_metrics.csv
- evaluation_metrics.csv
- classification_report.csv
- confusion_matrix.png

---

## 📸 Dashboard Preview

### Executive Dashboard

![Executive Dashboard](images/Executive%20Dashboard.png)

---

### Customer Dashboard

![Customer Dashboard](images/Customer%20Dashboard.png)


# 🚀 Installation


Move into the project

```bash
cd AI-Credit-Risk-Analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Python pipeline

```bash
python 01_data_loading.py
python 02_data_cleaning.py
python 03_eda.py
python 04_visualization.py
python 05_feature_engineering.py
python 06_data_preprocessing.py
python 07_model_training.py
python 08_model_evaluation.py
python 09_prediction.py
```

---

# 📌 Business Insights

- Applicants with a positive credit history have a significantly higher approval rate.
- Total income and loan amount strongly influence loan decisions.
- High-risk applicants are more likely to face loan rejection.
- Logistic Regression delivered the best balance between accuracy and interpretability for this dataset.
- Interactive dashboards provide actionable insights for banking and financial decision-makers.

---

# 🔮 Future Improvements

- Hyperparameter tuning with GridSearchCV
- XGBoost and LightGBM models
- Model deployment using Flask/FastAPI
- Real-time prediction API
- Cloud deployment (Azure/AWS)
- Automated Power BI refresh
- Explainable AI using SHAP

---

# 👨‍💻 Author

**Ams**

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning

GitHub: https://github.com/Ams1421

---

# ⭐ If you found this project useful, consider giving it a star!
