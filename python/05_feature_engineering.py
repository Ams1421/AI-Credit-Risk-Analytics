import pandas as pd

# ==========================================
# AI Credit Risk Analytics Platform
# Phase 5 - Feature Engineering
# ==========================================

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# Load cleaned dataset
df = pd.read_csv("../dataset/processed_data.csv")

print("\nDataset Loaded Successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# ==========================================
# Feature 1 - Total Income
# ==========================================

df["TotalIncome"] = (
    df["ApplicantIncome"] +
    df["CoapplicantIncome"]
)

# ==========================================
# Feature 2 - Loan to Income Ratio
# ==========================================

df["LoanToIncomeRatio"] = (
    df["LoanAmount"] /
    df["TotalIncome"]
).round(4)

# ==========================================
# Feature 3 - Income Category
# ==========================================

def income_category(income):

    if income < 3000:
        return "Low"

    elif income < 6000:
        return "Medium"

    elif income < 10000:
        return "High"

    else:
        return "Very High"

df["IncomeCategory"] = df["TotalIncome"].apply(income_category)

# ==========================================
# Feature 4 - Loan Size
# ==========================================

def loan_size(amount):

    if amount < 100:
        return "Small"

    elif amount < 200:
        return "Medium"

    elif amount < 400:
        return "Large"

    else:
        return "Very Large"

df["LoanSize"] = df["LoanAmount"].apply(loan_size)

# ==========================================
# Feature 5 - Family Size
# ==========================================

df["Dependents"] = df["Dependents"].replace("3+", 3)
df["Dependents"] = df["Dependents"].astype(int)

df["FamilySize"] = df["Dependents"] + 2

# ==========================================
# Feature 6 - Applicant Type
# ==========================================

df["ApplicantType"] = df["Self_Employed"].apply(
    lambda x: "Self Employed" if x == "Yes" else "Salaried"
)

# ==========================================
# Feature 7 - Credit Risk
# ==========================================

def credit_risk(row):

    if row["Credit_History"] == 1 and row["LoanToIncomeRatio"] < 0.03:
        return "Low Risk"

    elif row["Credit_History"] == 1:
        return "Medium Risk"

    else:
        return "High Risk"

df["RiskCategory"] = df.apply(credit_risk, axis=1)

# ==========================================
# Save Dataset
# ==========================================

output = "../dataset/featured_data.csv"

df.to_csv(output, index=False)

print("\nFeature Engineering Completed!")

print(f"\nNew Shape: {df.shape}")

print("\nNew Features Added:")

new_features = [
    "TotalIncome",
    "LoanToIncomeRatio",
    "IncomeCategory",
    "LoanSize",
    "FamilySize",
    "ApplicantType",
    "RiskCategory"
]

for feature in new_features:
    print(f"✓ {feature}")

print(f"\nDataset saved to:\n{output}")