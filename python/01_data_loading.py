import pandas as pd

# Load datasets
train_df = pd.read_csv("../dataset/loan_train.csv")
test_df = pd.read_csv("../dataset/loan_test.csv")

# Display first 5 rows
print("\n========== TRAIN DATASET ==========")
print(train_df.head())

print("\n========== TEST DATASET ==========")
print(test_df.head())

# Display shape
print("\n========== DATASET SHAPES ==========")
print("Train Shape:", train_df.shape)
print("Test Shape:", test_df.shape)

# Display columns
print("\n========== TRAIN COLUMNS ==========")
print(train_df.columns.tolist())

# Dataset information
print("\n========== TRAIN INFO ==========")
train_df.info()

# Check missing values
print("\n========== MISSING VALUES ==========")
print(train_df.isnull().sum())

# Basic statistics
print("\n========== NUMERICAL SUMMARY ==========")
print(train_df.describe())

# Target variable distribution
print("\n========== LOAN STATUS DISTRIBUTION ==========")
print(train_df["Loan_Status"].value_counts())