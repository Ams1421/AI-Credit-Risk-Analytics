/* ============================================================
   1. Rank Customers by Total Income
   ============================================================ */

SELECT
    Loan_ID,
    TotalIncome,
    RANK() OVER (ORDER BY TotalIncome DESC) AS Income_Rank
FROM loan_applications;


/* ============================================================
   2. Top 5 Customers by Loan Amount
   ============================================================ */

SELECT
    Loan_ID,
    LoanAmount,
    DENSE_RANK() OVER (ORDER BY LoanAmount DESC) AS Loan_Rank
FROM loan_applications
LIMIT 5;


/* ============================================================
   3. Row Number by Property Area
   ============================================================ */

SELECT
    Loan_ID,
    Property_Area,
    ROW_NUMBER() OVER(PARTITION BY Property_Area ORDER BY TotalIncome DESC) AS Row_Num
FROM loan_applications;


/* ============================================================
   4. High Income Customers (CTE)
   ============================================================ */

WITH HighIncome AS
(
    SELECT *
    FROM loan_applications
    WHERE TotalIncome > 10000
)

SELECT *
FROM HighIncome;


/* ============================================================
   5. Approval Summary View
   ============================================================ */

CREATE VIEW approval_summary AS

SELECT
    Loan_Status,
    COUNT(*) AS Applications,
    ROUND(AVG(LoanAmount),2) AS AvgLoan
FROM loan_applications
GROUP BY Loan_Status;


/* ============================================================
   6. Risk Score Summary
   ============================================================ */

SELECT
RiskCategory,
COUNT(*) AS Customers,
ROUND(AVG(TotalIncome),2) AS AvgIncome,
ROUND(AVG(LoanAmount),2) AS AvgLoan
FROM loan_applications
GROUP BY RiskCategory;


/* ============================================================
   7. Loan Size Analysis
   ============================================================ */

SELECT
LoanSize,
COUNT(*) AS Applications,
ROUND(AVG(LoanAmount),2) AS AvgLoan
FROM loan_applications
GROUP BY LoanSize;


/* ============================================================
   8. Approval Rate by Property Area
   ============================================================ */

SELECT
Property_Area,
Loan_Status,
COUNT(*) AS Applications
FROM loan_applications
GROUP BY Property_Area, Loan_Status
ORDER BY Property_Area;