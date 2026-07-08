# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Database | MySQL |
| Database Name | loan_analysis |
| Table | loan_applications |
| SQL Version | MySQL 8.0+ |
| Total Records | 614 |

---

# 1. Introduction

This document describes the SQL implementation used in the AI Credit Risk Analytics Dashboard.

The database stores processed loan application records and supports analytical queries for customer analysis, financial reporting, and credit risk assessment.

The SQL implementation focuses on business intelligence rather than transaction processing.

---

# 2. Database Architecture

```
                 loan_analysis
                       │
                       ▼
              loan_applications
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
Customer Data    Financial Data    Loan Status
                       │
                       ▼
               SQL Business Queries
                       │
                       ▼
               Power BI Dashboard
```

---

# 3. Database Schema

Database Name

```
loan_analysis
```

Table Name

```
loan_applications
```

Primary Key

```
Loan_ID
```

---

# 4. Table Structure

| Column | Data Type | Description |
|---------|-----------|-------------|
| Loan_ID | VARCHAR | Unique Loan Identifier |
| Gender | VARCHAR | Applicant Gender |
| Married | VARCHAR | Marital Status |
| Dependents | INT | Number of Dependents |
| Education | VARCHAR | Education Level |
| Self_Employed | VARCHAR | Employment Status |
| ApplicantIncome | INT | Monthly Applicant Income |
| CoapplicantIncome | DECIMAL | Monthly Co-applicant Income |
| LoanAmount | DECIMAL | Requested Loan Amount |
| Loan_Amount_Term | INT | Loan Repayment Period |
| Credit_History | INT | Credit History Indicator |
| Property_Area | VARCHAR | Property Location |
| Loan_Status | VARCHAR | Loan Approval Status |
| TotalIncome | DECIMAL | Combined Income |
| LoanToIncomeRatio | DECIMAL | Loan to Income Ratio |
| IncomeCategory | VARCHAR | Income Segment |
| LoanSize | VARCHAR | Loan Category |
| ApplicantType | VARCHAR | Salaried / Self Employed |
| FamilySize | INT | Estimated Family Size |
| RiskCategory | VARCHAR | Credit Risk Category |

---

# 5. SQL Concepts Implemented

The project demonstrates the following SQL concepts:

## Data Retrieval

- SELECT
- DISTINCT
- WHERE
- LIMIT
- ORDER BY

---

## Aggregate Functions

- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

---

## Grouping

- GROUP BY
- HAVING

---

## Conditional Logic

- CASE
- IFNULL
- COALESCE

---

## Window Functions

Implemented:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

Business Applications:

- Ranking highest income customers
- Ranking loan amounts
- Ranking customer groups

---

## Common Table Expressions (CTE)

Used for:

- Temporary business reports
- Aggregated analysis
- Simplifying complex queries

Example

```sql
WITH income_summary AS
(
    SELECT
        IncomeCategory,
        COUNT(*) AS Total_Customers
    FROM loan_applications
    GROUP BY IncomeCategory
)

SELECT *
FROM income_summary;
```

---

## Views

Views were created for reusable reports.

Examples

- High Risk Customers
- Approved Customers
- Financial Summary

Advantages

- Improved readability
- Reusable queries
- Simplified reporting

---

# 6. Business Questions Solved

The SQL queries answer several business questions.

### Customer Analysis

- How many applicants are male and female?
- Which education level has the highest approval rate?
- How many self-employed applicants received approval?
- Which property area has the most applicants?

---

### Financial Analysis

- Average applicant income
- Average loan amount
- Highest income customer
- Lowest income customer
- Loan distribution by income category

---

### Loan Analysis

- Approved vs Rejected loans
- Loan approval percentage
- Average loan amount by education
- Loan amount by property area

---

### Risk Analysis

- High-risk customers
- Credit history analysis
- Loan approval by risk category
- Family size impact
- Loan-to-income ratio analysis

---

# 7. SQL Query Categories

The project contains over **30 analytical SQL queries**.

### Basic Queries

- SELECT
- DISTINCT
- LIMIT
- ORDER BY

---

### Filtering Queries

- WHERE
- BETWEEN
- IN
- LIKE

---

### Aggregation Queries

- COUNT
- AVG
- SUM
- MAX
- MIN

---

### Grouping Queries

- GROUP BY
- HAVING

---

### Ranking Queries

- ROW_NUMBER()
- RANK()
- DENSE_RANK()

---

### CTE Queries

- Income Summary
- Loan Summary
- Risk Summary

---

### View Queries

- Customer View
- Financial View
- Risk View

---

# 8. SQL Performance Considerations

Potential optimizations include:

- Indexing frequently queried columns
- Optimizing WHERE clauses
- Reducing unnecessary SELECT *
- Using Views for repeated reports
- Efficient GROUP BY operations

---

# 9. Suggested Indexes

For larger datasets, the following indexes are recommended:

```sql
CREATE INDEX idx_loan_status
ON loan_applications(Loan_Status);

CREATE INDEX idx_credit_history
ON loan_applications(Credit_History);

CREATE INDEX idx_property_area
ON loan_applications(Property_Area);

CREATE INDEX idx_income
ON loan_applications(ApplicantIncome);
```

Benefits:

- Faster filtering
- Improved joins
- Better dashboard performance

---

# 10. Integration with Power BI

The SQL database serves as the data source for Power BI.

Workflow:

```
CSV Dataset
      │
      ▼
Python Cleaning
      │
      ▼
MySQL Database
      │
      ▼
SQL Analytics
      │
      ▼
Power BI Dashboard
```

---

# 11. Best Practices Followed

The project follows several SQL best practices:

- Meaningful table names
- Consistent column naming
- Modular queries
- Reusable Views
- Window Functions for ranking
- CTEs for readability
- Proper formatting and indentation

---

# 12. Limitations

Current limitations include:

- Single table design
- No normalized schema
- No stored procedures
- No triggers
- No user management

These limitations are acceptable for an analytical portfolio project.

---

# 13. Future Improvements

Future enhancements may include:

- Database normalization
- Multiple related tables
- Foreign key constraints
- Stored Procedures
- Triggers
- Scheduled Events
- Role-Based Access
- Data Warehouse Design

---

# 14. Conclusion

The SQL implementation demonstrates practical business analytics using MySQL.

The queries provide meaningful insights into customer behavior, financial performance, and credit risk while supporting the interactive Power BI dashboards.

The project showcases a broad range of SQL concepts, from basic retrieval to advanced analytical techniques such as Window Functions, CTEs, and Views.