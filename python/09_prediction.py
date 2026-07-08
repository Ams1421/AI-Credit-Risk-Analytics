import pandas as pd
import joblib

print("=" * 60)
print("AI CREDIT RISK ANALYTICS")
print("PHASE 9 - FINAL PREDICTION")
print("=" * 60)

# --------------------------------------------------
# Load Best Pipeline
# --------------------------------------------------

pipeline = joblib.load("../python/models/best_pipeline.pkl")

print("\nBest Pipeline Loaded!")

# --------------------------------------------------
# Load Test Dataset
# --------------------------------------------------

test_df = pd.read_csv("../dataset/loan_test.csv")

print("Test Dataset Loaded!")

# Save Loan IDs
loan_ids = test_df["Loan_ID"]

# Remove Loan_ID
test_df = test_df.drop(columns=["Loan_ID"])

# --------------------------------------------------
# Handle Missing Values
# --------------------------------------------------

for col in test_df.columns:

    if pd.api.types.is_numeric_dtype(test_df[col]):
        test_df[col] = test_df[col].fillna(test_df[col].median())
    else:
        test_df[col] = test_df[col].fillna(test_df[col].mode()[0])

# --------------------------------------------------
# Convert Dependents
# --------------------------------------------------

test_df["Dependents"] = (
    test_df["Dependents"]
    .astype(str)
    .replace("3+", "3")
    .fillna("0")
    .astype(int)
)

# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------

# Total Income
test_df["TotalIncome"] = (
    test_df["ApplicantIncome"] +
    test_df["CoapplicantIncome"]
)

# Loan To Income Ratio
test_df["LoanToIncomeRatio"] = (
    test_df["LoanAmount"] /
    test_df["TotalIncome"]
)

test_df["LoanToIncomeRatio"] = (
    test_df["LoanToIncomeRatio"]
    .replace([float("inf"), -float("inf")], 0)
    .fillna(0)
)

# --------------------------------------------------
# Income Category
# --------------------------------------------------

def income_category(x):

    if x < 3000:
        return "Low"

    elif x < 6000:
        return "Medium"

    elif x < 10000:
        return "High"

    else:
        return "Very High"


test_df["IncomeCategory"] = test_df["TotalIncome"].apply(income_category)

# --------------------------------------------------
# Loan Size
# --------------------------------------------------

def loan_size(x):

    if x < 100:
        return "Small"

    elif x < 200:
        return "Medium"

    elif x < 400:
        return "Large"

    else:
        return "Very Large"


test_df["LoanSize"] = test_df["LoanAmount"].apply(loan_size)

# --------------------------------------------------
# Applicant Type
# --------------------------------------------------

test_df["ApplicantType"] = test_df["Self_Employed"].replace({

    "Yes": "Self Employed",

    "No": "Salaried"

})

# --------------------------------------------------
# Family Size
# --------------------------------------------------

test_df["FamilySize"] = test_df["Dependents"] + 2

# --------------------------------------------------
# Risk Category
# --------------------------------------------------

def risk(ch):

    if ch == 1:
        return "Low Risk"

    else:
        return "High Risk"


test_df["RiskCategory"] = test_df["Credit_History"].apply(risk)

# --------------------------------------------------
# Predict
# --------------------------------------------------

predictions = pipeline.predict(test_df)

# Convert prediction labels

predictions = [

    "Approved" if p == "Y" else "Rejected"

    for p in predictions

]

# --------------------------------------------------
# Save Predictions
# --------------------------------------------------

results = pd.DataFrame({

    "Loan_ID": loan_ids,

    "Prediction": predictions

})

results.to_csv(

    "../python/outputs/predictions.csv",

    index=False

)

print("\nPredictions Generated Successfully!\n")

print(results.head())

print("\npredictions.csv saved successfully!")

print("\nFINAL PREDICTION COMPLETED SUCCESSFULLY!")