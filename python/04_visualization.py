import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# AI Credit Risk Analytics Platform
# Phase 4 - Data Visualization
# ===============================

# Create images folder if it doesn't exist
os.makedirs("../images", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("../dataset/processed_data.csv")

# Set chart style
plt.style.use("ggplot")

print("=" * 60)
print("CREATING VISUALIZATIONS")
print("=" * 60)


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(f"../images/{filename}", dpi=300)
    plt.close()


# ----------------------------------------------------
# 1. Loan Approval Distribution
# ----------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Loan_Status")
plt.title("Loan Approval Distribution")
save_chart("01_loan_approval_distribution.png")


# ----------------------------------------------------
# 2. Gender Distribution
# ----------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
save_chart("02_gender_distribution.png")


# ----------------------------------------------------
# 3. Education Distribution
# ----------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Education")
plt.title("Education Distribution")
save_chart("03_education_distribution.png")


# ----------------------------------------------------
# 4. Property Area Distribution
# ----------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Property_Area")
plt.title("Property Area Distribution")
save_chart("04_property_area_distribution.png")


# ----------------------------------------------------
# 5. Credit History Distribution
# ----------------------------------------------------

plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Credit_History")
plt.title("Credit History Distribution")
save_chart("05_credit_history_distribution.png")


# ----------------------------------------------------
# 6. Applicant Income Distribution
# ----------------------------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["ApplicantIncome"], bins=30)
plt.title("Applicant Income Distribution")
save_chart("06_applicant_income_distribution.png")


# ----------------------------------------------------
# 7. Loan Amount Distribution
# ----------------------------------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["LoanAmount"], bins=30)
plt.title("Loan Amount Distribution")
save_chart("07_loan_amount_distribution.png")


# ----------------------------------------------------
# 8. Loan Amount vs Applicant Income
# ----------------------------------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="ApplicantIncome",
    y="LoanAmount",
    hue="Loan_Status"
)

plt.title("Loan Amount vs Applicant Income")
save_chart("08_loan_vs_income.png")


# ----------------------------------------------------
# 9. Correlation Heatmap
# ----------------------------------------------------

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
save_chart("09_correlation_heatmap.png")


print("\nAll visualizations saved successfully!")
print("\nLocation: images/")