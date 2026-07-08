import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

print("=" * 60)
print("AI CREDIT RISK ANALYTICS")
print("PHASE 7 - MODEL TRAINING")
print("=" * 60)

# --------------------------------------------------
# Load Saved Data
# --------------------------------------------------

X_train = joblib.load("../python/outputs/X_train.pkl")
X_test = joblib.load("../python/outputs/X_test.pkl")

y_train = joblib.load("../python/outputs/y_train.pkl")
y_test = joblib.load("../python/outputs/y_test.pkl")

preprocessor = joblib.load("../python/models/preprocessor.pkl")

print("\nTraining data loaded successfully!")

# --------------------------------------------------
# Models
# --------------------------------------------------

models = {

    "Logistic Regression":
        LogisticRegression(
            max_iter=3000,
            random_state=42
        ),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ),

    "Gradient Boosting":
        GradientBoostingClassifier(
            random_state=42
        )

}

results = []

best_pipeline = None
best_accuracy = 0
best_model_name = ""

# --------------------------------------------------
# Train Every Model
# --------------------------------------------------

for name, model in models.items():

    print(f"\nTraining {name}...")

    pipeline = Pipeline([

        ("preprocessor", preprocessor),

        ("model", model)

    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, pos_label="Y")
    recall = recall_score(y_test, predictions, pos_label="Y")
    f1 = f1_score(y_test, predictions, pos_label="Y")

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    results.append({

        "Model": name,
        "Accuracy": round(accuracy,4),
        "Precision": round(precision,4),
        "Recall": round(recall,4),
        "F1 Score": round(f1,4)

    })

    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_pipeline = pipeline
        best_model_name = name

# --------------------------------------------------
# Save Best Pipeline
# --------------------------------------------------

joblib.dump(

    best_pipeline,

    "../python/models/best_pipeline.pkl"

)

print("\nBest Pipeline Saved!")

print(f"Best Model : {best_model_name}")

print(f"Best Accuracy : {best_accuracy:.4f}")

# --------------------------------------------------
# Save Model Comparison
# --------------------------------------------------

results_df = pd.DataFrame(results)

results_df.to_csv(

    "../python/outputs/model_metrics.csv",

    index=False

)

print("\nModel Comparison")

print(results_df)

print("\nMODEL TRAINING COMPLETED SUCCESSFULLY!")