# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Dashboard | AI Credit Risk Analytics |
| Tool | Microsoft Power BI Desktop |
| Data Source | MySQL & CSV |
| Dashboard Pages | 4 |
| Dashboard Type | Interactive Business Intelligence |

---

# 1. Introduction

The Power BI dashboard provides an interactive business intelligence solution for analyzing historical loan application data.

The dashboard enables business users, financial analysts, and decision-makers to monitor loan applications, customer demographics, financial performance, and credit risk using interactive visualizations.

The dashboard supports filtering, drill-down analysis, and KPI monitoring.

---

# 2. Dashboard Objectives

The dashboard is designed to:

- Monitor loan approval trends
- Analyze customer demographics
- Evaluate financial performance
- Assess credit risk
- Support business decision-making
- Present machine learning insights

---

# 3. Dashboard Architecture

```
Loan Dataset
      │
      ▼
Python Data Processing
      │
      ▼
Feature Engineering
      │
      ▼
MySQL Database
      │
      ▼
Power BI Data Model
      │
      ▼
Interactive Dashboards
      │
      ▼
Business Insights
```

---

# 4. Dashboard Pages

The dashboard consists of four interactive pages.

---

# Page 1 — Executive Dashboard

## Purpose

Provides an overview of loan application performance through key business metrics.

---

## KPIs

- Total Loan Applications
- Approved Loans
- Rejected Loans
- Approval Rate
- Average Applicant Income
- Average Loan Amount

---

## Charts

### Loan Status Distribution

Visual

Stacked Column Chart

Purpose

Displays the number of approved and rejected loans.

---

### Property Area Analysis

Visual

Clustered Bar Chart

Purpose

Shows loan applications across Urban, Semiurban, and Rural locations.

---

### Education Analysis

Visual

Pie Chart

Purpose

Displays applicant education distribution.

---

### Income Distribution

Visual

Column Chart

Purpose

Shows applicant income across categories.

---

## Slicers

- Property Area
- Education
- Loan Status
- Gender

---

# Page 2 — Customer Analytics

## Purpose

Analyzes customer demographics.

---

## KPIs

- Male Applicants
- Female Applicants
- Married Applicants
- Self Employed Applicants

---

## Charts

### Gender Distribution

Visual

Pie Chart

Purpose

Shows gender ratio.

---

### Marital Status

Visual

Donut Chart

Purpose

Displays married vs unmarried applicants.

---

### Education Distribution

Visual

Bar Chart

Purpose

Shows education categories.

---

### Dependents Analysis

Visual

Column Chart

Purpose

Shows family dependency distribution.

---

### Applicant Type

Visual

Pie Chart

Purpose

Displays salaried vs self-employed applicants.

---

## Business Value

Helps understand customer characteristics.

---

# Page 3 — Financial Analytics

## Purpose

Analyzes applicant financial capability.

---

## KPIs

- Average Income
- Average Loan Amount
- Average Loan-To-Income Ratio

---

## Charts

### Income Category

Visual

Column Chart

Purpose

Displays Low, Medium, High, and Very High income groups.

---

### Loan Size

Visual

Bar Chart

Purpose

Shows distribution of loan sizes.

---

### Income vs Loan Amount

Visual

Scatter Plot

Purpose

Analyzes relationship between income and requested loan amount.

---

### Loan-To-Income Ratio

Visual

Histogram

Purpose

Evaluates repayment capability.

---

### Total Income by Property Area

Visual

Clustered Column Chart

Purpose

Compares income across locations.

---

## Business Value

Supports financial risk assessment.

---

# Page 4 — Credit Risk Analytics

## Purpose

Provides insights into applicant creditworthiness and loan approval patterns.

---

## KPIs

- Low Risk Customers
- High Risk Customers
- Approval Rate
- Average Credit History Score

---

## Charts

### Risk Category Distribution

Visual

Pie Chart

Purpose

Shows customer segmentation by risk.

---

### Credit History Analysis

Visual

Clustered Column Chart

Purpose

Compares approvals based on credit history.

---

### Loan Approval by Risk Category

Visual

Stacked Bar Chart

Purpose

Shows approval rates for Low Risk and High Risk customers.

---

### Property Area vs Risk

Visual

Matrix

Purpose

Analyzes geographic risk distribution.

---

### Loan Amount by Risk

Visual

Column Chart

Purpose

Compares requested loan amounts across risk groups.

---

## Business Value

Supports loan approval and credit risk management.

---

# 5. Dashboard Filters

The dashboard supports the following slicers:

- Gender
- Education
- Property Area
- Loan Status
- Applicant Type
- Income Category
- Risk Category

These slicers dynamically update all visuals.

---

# 6. DAX Measures

Example measures used:

## Total Applications

```DAX
Total Applications =
COUNT(loan_applications[Loan_ID])
```

---

## Approved Loans

```DAX
Approved Loans =
CALCULATE(
COUNT(loan_applications[Loan_ID]),
loan_applications[Loan_Status]="Y"
)
```

---

## Rejected Loans

```DAX
Rejected Loans =
CALCULATE(
COUNT(loan_applications[Loan_ID]),
loan_applications[Loan_Status]="N"
)
```

---

## Approval Rate

```DAX
Approval Rate =
DIVIDE(
[Approved Loans],
[Total Applications]
)
```

---

## Average Loan Amount

```DAX
Average Loan Amount =
AVERAGE(loan_applications[LoanAmount])
```

---

## Average Income

```DAX
Average Income =
AVERAGE(loan_applications[TotalIncome])
```

---

# 7. Dashboard Design Principles

The dashboard follows BI best practices.

- Consistent color palette
- KPI cards positioned at the top
- Interactive slicers
- Minimal visual clutter
- Responsive layout
- Clear chart titles
- Business-friendly terminology

---

# 8. Business Insights

The dashboard highlights several key findings.

- Customers with positive credit history receive significantly more approvals.
- Medium-sized loans have the highest approval frequency.
- Urban and Semiurban applicants represent the largest customer segments.
- Higher household income generally increases approval probability.
- Low-risk applicants dominate approved loan applications.

---

# 9. Dashboard Benefits

The dashboard enables stakeholders to:

- Monitor loan portfolio performance.
- Identify high-risk applicants.
- Understand customer demographics.
- Analyze financial trends.
- Improve lending decisions.
- Reduce manual reporting effort.

---

# 10. Future Enhancements

Potential improvements include:

- Real-time Power BI Service integration.
- Automatic dataset refresh.
- Drill-through pages.
- Forecasting visuals.
- AI visuals in Power BI.
- Row-Level Security (RLS).
- Mobile dashboard optimization.
- Integration with Azure SQL Database.

---

# 11. Conclusion

The Power BI Dashboard transforms raw loan application data into meaningful visual insights.

By combining interactive dashboards with machine learning outputs, the solution enables financial institutions to make faster, data-driven lending decisions while improving transparency and operational efficiency.