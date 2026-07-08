# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Project | AI Credit Risk Analytics Dashboard |
| Dataset | Loan Prediction Dataset |
| Records | 614 |
| Features | 20 |
| Target Variable | Loan_Status |

---

# 1. Introduction

This document describes the data dictionary for the AI Credit Risk Analytics Dashboard.

A data dictionary defines each dataset attribute, including its data type, business meaning, and role within the analytics pipeline.

It serves as a reference for developers, analysts, business users, and future project maintenance.

---

# 2. Dataset Summary

| Property | Value |
|----------|------:|
| Dataset Name | featured_data.csv |
| Total Rows | 614 |
| Total Columns | 20 |
| Missing Values | Handled during preprocessing |
| Target Variable | Loan_Status |

---

# 3. Data Dictionary

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Loan_ID | String | Unique identifier assigned to each loan application | LP001002 |
| Gender | Categorical | Gender of the applicant | Male |
| Married | Categorical | Applicant marital status | Yes |
| Dependents | Integer | Number of financial dependents | 2 |
| Education | Categorical | Applicant education level | Graduate |
| Self_Employed | Categorical | Employment type | Yes |
| ApplicantIncome | Integer | Monthly income of the primary applicant | 4583 |
| CoapplicantIncome | Float | Monthly income of the co-applicant | 1508.0 |
| LoanAmount | Float | Requested loan amount (in thousands) | 128 |
| Loan_Amount_Term | Integer | Loan repayment period (months) | 360 |
| Credit_History | Integer | Credit history indicator (1 = Good, 0 = Poor) | 1 |
| Property_Area | Categorical | Location of the applicant's property | Urban |
| Loan_Status | Target | Loan approval outcome | Y |

---

# 4. Engineered Features

The following features were created during feature engineering.

---

## TotalIncome

### Data Type

```
Float
```

### Formula

```
ApplicantIncome + CoapplicantIncome
```

### Business Purpose

Represents the combined household income available for loan repayment.

---

## LoanToIncomeRatio

### Data Type

```
Float
```

### Formula

```
LoanAmount / TotalIncome
```

### Business Purpose

Measures how large the requested loan is relative to the applicant's total income.

Lower values generally indicate better repayment capability.

---

## IncomeCategory

### Data Type

```
Categorical
```

### Categories

- Low
- Medium
- High
- Very High

### Business Purpose

Groups customers into income segments for reporting and analytics.

---

## LoanSize

### Data Type

```
Categorical
```

### Categories

- Small
- Medium
- Large
- Very Large

### Business Purpose

Categorizes requested loan amounts into business-friendly groups.

---

## ApplicantType

### Data Type

```
Categorical
```

### Categories

- Salaried
- Self Employed

### Business Purpose

Classifies applicants based on employment type.

---

## FamilySize

### Data Type

```
Integer
```

### Formula

```
Dependents + 2
```

### Business Purpose

Provides an estimate of household size for affordability analysis.

---

## RiskCategory

### Data Type

```
Categorical
```

### Categories

- Low Risk
- High Risk

### Business Purpose

Segments applicants according to their credit history.

Applicants with a positive credit history are classified as Low Risk.

---

# 5. Feature Classification

## Numerical Features

- Dependents
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- TotalIncome
- LoanToIncomeRatio
- FamilySize

---

## Categorical Features

- Gender
- Married
- Education
- Self_Employed
- Property_Area
- IncomeCategory
- LoanSize
- ApplicantType
- RiskCategory

---

## Target Feature

- Loan_Status

---

# 6. Data Quality Summary

The dataset originally contained missing values in multiple columns.

The preprocessing pipeline performed:

- Missing value imputation
- Data validation
- Feature engineering
- Scaling
- Encoding

This produced a clean dataset suitable for machine learning and business analysis.

---

# 7. Business Significance

The dataset supports multiple analytical use cases:

### Customer Analytics

- Gender distribution
- Education analysis
- Family structure

---

### Financial Analytics

- Income analysis
- Loan amount analysis
- Loan affordability

---

### Credit Risk Analysis

- Credit history
- Risk segmentation
- Approval trends

---

### Predictive Analytics

The dataset serves as input for machine learning models that predict loan approval decisions.

---

# 8. Relationships Between Features

```
ApplicantIncome
          │
          ▼
CoapplicantIncome
          │
          ▼
     TotalIncome
          │
          ▼
LoanToIncomeRatio
          │
          ▼
Machine Learning Model
          │
          ▼
Loan Approval Prediction
```

---

# 9. Data Usage

The dataset is used across the entire project lifecycle.

| Stage | Usage |
|--------|-------|
| Python | Data Cleaning |
| SQL | Business Analytics |
| Power BI | Interactive Dashboard |
| Machine Learning | Loan Approval Prediction |

---

# 10. Future Data Enhancements

Future versions of the dataset may include:

- Applicant Age
- Occupation
- Annual Income
- Credit Score
- Existing Loans
- Employment Duration
- Debt-to-Income Ratio
- Loan Purpose
- Banking History
- Geographic Region

Adding these variables could improve predictive performance and provide deeper business insights.

---

# 11. Conclusion

The data dictionary provides a standardized reference for all dataset attributes used in the AI Credit Risk Analytics Dashboard.

It ensures consistent understanding across development, analytics, reporting, and machine learning activities while improving project maintainability and documentation quality.