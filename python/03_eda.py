import pandas as pd

# ===============================
# AI Credit Risk Analytics Platform
# Phase 3 - Exploratory Data Analysis
# ===============================

# Load cleaned dataset
df = pd.read_csv("../dataset/processed_data.csv")

print("="*60)
print("EXPLORATORY DATA ANALYSIS")
print("="*60)

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nUnique Values")

for column in df.columns:
    print(f"\n{column}")
    print(df[column].unique())

print("\nLoan Approval Distribution")
print(df["Loan_Status"].value_counts())

print("\nGender Distribution")
print(df["Gender"].value_counts())

print("\nEducation Distribution")
print(df["Education"].value_counts())

print("\nProperty Area Distribution")
print(df["Property_Area"].value_counts())

print("\nCredit History Distribution")
print(df["Credit_History"].value_counts())

print("\nApplicant Income Statistics")
print(df["ApplicantIncome"].describe())

print("\nLoan Amount Statistics")
print(df["LoanAmount"].describe())

print("\nCorrelation Matrix")

numeric_df = df.select_dtypes(include=["number"])

print(numeric_df.corr())