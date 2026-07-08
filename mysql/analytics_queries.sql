/* ============================================================
   1. Total Applications
   ============================================================ */

SELECT
COUNT(*) AS Total_Applications
FROM loan_applications;


/* ============================================================
   2. Approval vs Rejection
   ============================================================ */

SELECT
Loan_Status,
COUNT(*) AS Total
FROM loan_applications
GROUP BY Loan_Status;


/* ============================================================
   3. Approval Rate (%)
   ============================================================ */

SELECT
Loan_Status,
COUNT(*) AS Applications,
ROUND(
COUNT(*) * 100.0 /
(SELECT COUNT(*) FROM loan_applications),
2
) AS Percentage
FROM loan_applications
GROUP BY Loan_Status;


/* ============================================================
   4. Average Loan Amount
   ============================================================ */

SELECT
ROUND(AVG(LoanAmount),2) AS Average_Loan
FROM loan_applications;


/* ============================================================
   5. Income Category Analysis
   ============================================================ */

SELECT
IncomeCategory,
COUNT(*) AS Customers,
ROUND(AVG(TotalIncome),2) AS AvgIncome,
ROUND(AVG(LoanAmount),2) AS AvgLoan
FROM loan_applications
GROUP BY IncomeCategory
ORDER BY AvgIncome DESC;


/* ============================================================
   6. Risk Category
   ============================================================ */

SELECT
RiskCategory,
COUNT(*) AS Customers
FROM loan_applications
GROUP BY RiskCategory;


/* ============================================================
   7. Property Area Analysis
   ============================================================ */

SELECT
Property_Area,
COUNT(*) AS Applications,
ROUND(AVG(LoanAmount),2) AS AvgLoan
FROM loan_applications
GROUP BY Property_Area;


/* ============================================================
   8. Education Analysis
   ============================================================ */

SELECT
Education,
COUNT(*) AS Customers,
ROUND(AVG(ApplicantIncome),2) AS AvgIncome
FROM loan_applications
GROUP BY Education;


/* ============================================================
   9. Applicant Type Analysis
   ============================================================ */

SELECT
ApplicantType,
COUNT(*) AS Customers,
ROUND(AVG(TotalIncome),2) AS AvgIncome
FROM loan_applications
GROUP BY ApplicantType;


/* ============================================================
   10. Top 10 Highest Income Customers
   ============================================================ */

SELECT
Loan_ID,
TotalIncome,
LoanAmount,
RiskCategory
FROM loan_applications
ORDER BY TotalIncome DESC
LIMIT 10;