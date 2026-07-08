# User Manual
# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Project | AI Credit Risk Analytics Dashboard |
| Version | 1.0 |
| Dashboard Tool | Microsoft Power BI Desktop |
| Target Users | Business Users, Credit Analysts, Managers, Data Analysts |

---

# 1. Introduction

The AI Credit Risk Analytics Dashboard is an interactive Business Intelligence solution designed to analyze historical loan applications, assess applicant risk, and support loan approval decisions.

The dashboard enables users to explore customer demographics, financial information, credit risk, and machine learning predictions without requiring technical expertise.

This manual explains how to use the dashboard effectively.

---

# 2. Intended Users

This dashboard is designed for:

- Business Managers
- Credit Analysts
- Loan Officers
- Financial Analysts
- Data Analysts
- Students and Researchers

---

# 3. Dashboard Overview

The dashboard contains four interactive pages.

| Page | Description |
|------|-------------|
| Executive Dashboard | Overall business performance |
| Customer Analytics | Customer demographics |
| Financial Analytics | Income and loan analysis |
| Credit Risk Analytics | Credit risk assessment |

Each page provides different business insights while sharing the same underlying dataset.

---

# 4. Opening the Dashboard

Open the project folder.

Navigate to:

```
powerbi/
```

Open

```
loan_dashboard.pbix
```

Power BI Desktop will load the dashboard automatically.

---

# 5. Dashboard Navigation

Use the tabs at the bottom of Power BI to switch between pages.

Example

```
Executive Dashboard

↓

Customer Analytics

↓

Financial Analytics

↓

Credit Risk Analytics
```

---

# 6. Using Slicers

Slicers allow users to filter dashboard data.

Available slicers include:

- Gender
- Education
- Property Area
- Loan Status
- Income Category
- Risk Category
- Applicant Type

Selecting a slicer automatically updates every chart and KPI on the page.

To clear a filter:

Click the **Clear Filter** icon in the slicer.

---

# 7. Executive Dashboard

## Purpose

Provides a high-level overview of loan application performance.

### KPI Cards

- Total Applications
- Approved Loans
- Rejected Loans
- Approval Rate
- Average Income
- Average Loan Amount

### Business Use

Managers can quickly understand overall lending performance.

---

# 8. Customer Analytics

## Purpose

Analyze customer demographics.

Visuals include:

- Gender Distribution
- Marital Status
- Education
- Dependents
- Applicant Type

### Business Use

Understand the profile of loan applicants.

---

# 9. Financial Analytics

## Purpose

Analyze financial information.

Visuals include:

- Income Categories
- Loan Amount Distribution
- Loan Size Analysis
- Loan-to-Income Ratio
- Income vs Loan Amount

### Business Use

Evaluate customer repayment capability.

---

# 10. Credit Risk Analytics

## Purpose

Assess applicant risk.

Visuals include:

- Credit History
- Risk Categories
- Loan Approval by Risk
- Loan Amount by Risk
- Property Area Risk

### Business Use

Identify high-risk applicants and monitor approval trends.

---

# 11. Understanding KPIs

### Total Applications

Total number of loan applications received.

---

### Approved Loans

Number of approved applications.

---

### Rejected Loans

Number of rejected applications.

---

### Approval Rate

Percentage of approved applications.

Higher values indicate stronger loan approval performance.

---

### Average Income

Average household income of applicants.

---

### Average Loan Amount

Average requested loan amount.

---

# 12. Understanding Charts

### Pie Chart

Shows percentage distribution.

Example

Gender Distribution

---

### Bar Chart

Compares different categories.

Example

Property Area

---

### Column Chart

Displays comparisons over categories.

Example

Income Category

---

### Scatter Plot

Shows relationships between two numerical variables.

Example

Income vs Loan Amount

---

### Matrix

Displays summarized information in tabular form.

---

# 13. Interacting with Visuals

Power BI allows users to interact with every visual.

Users can:

- Click a chart segment
- Filter another chart
- Hover for tooltips
- Cross-highlight visuals
- Drill into details (if enabled)

---

# 14. Refreshing Data

To refresh the dashboard:

```
Home

↓

Refresh
```

Power BI reloads the latest dataset.

---

# 15. Machine Learning Outputs

The project generates prediction results.

Generated Files

```
predictions.csv

model_metrics.csv

evaluation_metrics.csv

classification_report.csv
```

These files can be imported into Power BI for additional reporting.

---

# 16. Frequently Asked Questions

### Why did KPI values change?

Because a slicer or filter has been applied.

---

### How do I clear filters?

Use the **Clear Filter** option in the slicer.

---

### Why is a chart empty?

Possible reasons:

- Selected filters removed all matching records.
- Dataset path has changed.
- Data was not refreshed.

---

### Can the dashboard predict new loans?

Yes.

Run

```
python 09_prediction.py
```

to generate predictions for new loan records.

---

### Can I use another dataset?

Yes.

Replace the dataset while maintaining the same column structure.

---

# 17. Best Practices

For best results:

- Refresh data after updates.
- Apply only necessary filters.
- Review KPIs before analyzing charts.
- Use multiple visuals together.
- Compare trends across dashboard pages.

---

# 18. Troubleshooting

## Dashboard Does Not Open

Verify:

- Power BI Desktop is installed.
- File path is correct.

---

## Charts Not Displaying

Check:

- Dataset connection
- Refresh status
- Applied filters

---

## Incorrect KPI Values

Ensure:

- Data is refreshed.
- Correct slicers are selected.
- Dataset has not been modified.

---

# 19. Future Enhancements

Future versions may include:

- AI Prediction Dashboard
- Real-time Data Refresh
- Power BI Service Deployment
- Mobile Dashboard
- Role-Level Security
- Forecasting Visuals
- Natural Language Queries

---

# 20. Support

For project-related questions:

GitHub Repository

```
https://github.com/Ams1421/AI-Credit-Risk-Analytics
```

Author

**Ams**

Aspiring Data Analyst | Python | SQL | Power BI | Machine Learning

---

# 21. Conclusion

The AI Credit Risk Analytics Dashboard provides an interactive platform for analyzing loan applications, understanding customer behavior, assessing financial risk, and supporting data-driven lending decisions.

By combining Python, SQL, Power BI, and Machine Learning into a single workflow, the project demonstrates a complete analytics solution suitable for business reporting, academic learning, and professional portfolio development.