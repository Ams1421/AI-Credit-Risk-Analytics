import pandas as pd
import joblib
import os

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

print("=" * 60)
print("AI CREDIT RISK ANALYTICS")
print("PHASE 6 - DATA PREPROCESSING")
print("=" * 60)

# --------------------------------------------------
# Create folders
# --------------------------------------------------

os.makedirs("../python/models", exist_ok=True)
os.makedirs("../python/outputs", exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv("../dataset/featured_data.csv")

print("\nDataset Loaded Successfully!")
print(df.shape)

# --------------------------------------------------
# Features & Target
# --------------------------------------------------

X = df.drop(columns=["Loan_ID", "Loan_Status"])

y = df["Loan_Status"]

# --------------------------------------------------
# Categorical & Numerical Columns
# --------------------------------------------------

categorical_features = X.select_dtypes(include="object").columns.tolist()

numerical_features = X.select_dtypes(exclude="object").columns.tolist()

print("\nCategorical Features")

print(categorical_features)

print("\nNumerical Features")

print(numerical_features)

# --------------------------------------------------
# Train Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("\nTraining Shape :", X_train.shape)

print("Testing Shape  :", X_test.shape)

# --------------------------------------------------
# Preprocessing Pipeline
# --------------------------------------------------

preprocessor = ColumnTransformer(

    transformers=[

        (

            "num",

            StandardScaler(),

            numerical_features

        ),

        (

            "cat",

            OneHotEncoder(handle_unknown="ignore"),

            categorical_features

        )

    ]

)

# --------------------------------------------------
# Save Everything
# --------------------------------------------------

joblib.dump(

    preprocessor,

    "../python/models/preprocessor.pkl"

)

joblib.dump(

    categorical_features,

    "../python/models/categorical_features.pkl"

)

joblib.dump(

    numerical_features,

    "../python/models/numerical_features.pkl"

)

joblib.dump(

    X_train,

    "../python/outputs/X_train.pkl"

)

joblib.dump(

    X_test,

    "../python/outputs/X_test.pkl"

)

joblib.dump(

    y_train,

    "../python/outputs/y_train.pkl"

)

joblib.dump(

    y_test,

    "../python/outputs/y_test.pkl"

)

print("\nPreprocessor Saved!")

print("Training Data Saved!")

print("Testing Data Saved!")

print("\nDATA PREPROCESSING COMPLETED SUCCESSFULLY!")