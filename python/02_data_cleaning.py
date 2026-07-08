import pandas as pd

# ==========================================
# AI Credit Risk Analytics Platform
# Phase 2 - Data Cleaning
# ==========================================

print("=" * 60)
print("AI CREDIT RISK ANALYTICS")
print("PHASE 2 - DATA CLEANING")
print("=" * 60)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv("../dataset/loan_train.csv")

print("\nDataset Loaded Successfully")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# ------------------------------------------
# Data Quality Report
# ------------------------------------------

print("\n" + "=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# ------------------------------------------
# Missing Value Treatment
# ------------------------------------------

# Categorical Columns
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

# Numerical Columns
df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

# ------------------------------------------
# Remove Duplicates
# ------------------------------------------

df = df.drop_duplicates()

# ------------------------------------------
# Verify Cleaning
# ------------------------------------------

print("\n" + "=" * 60)
print("AFTER CLEANING")
print("=" * 60)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# ------------------------------------------
# Save Clean Dataset
# ------------------------------------------

output_path = "../dataset/processed_data.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print(f"Location: {output_path}")

print("\nFinal Shape:")
print(df.shape)

print("\nData Cleaning Completed Successfully!")