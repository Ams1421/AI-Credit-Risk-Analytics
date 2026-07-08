import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    roc_auc_score
)

print("=" * 60)
print("AI CREDIT RISK ANALYTICS")
print("PHASE 8 - MODEL EVALUATION")
print("=" * 60)

# --------------------------------------------------
# Load Best Pipeline
# --------------------------------------------------

pipeline = joblib.load("../python/models/best_pipeline.pkl")

print("\nBest Pipeline Loaded!")

# --------------------------------------------------
# Load Test Data
# --------------------------------------------------

X_test = joblib.load("../python/outputs/X_test.pkl")
y_test = joblib.load("../python/outputs/y_test.pkl")

print("Test Data Loaded!")

# --------------------------------------------------
# Predictions
# --------------------------------------------------

y_pred = pipeline.predict(X_test)

y_prob = pipeline.predict_proba(X_test)[:, 1]

# --------------------------------------------------
# Metrics
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="Y")
recall = recall_score(y_test, y_pred, pos_label="Y")
f1 = f1_score(y_test, y_pred, pos_label="Y")

# Convert labels for ROC AUC
y_test_binary = (y_test == "Y").astype(int)

roc_auc = roc_auc_score(y_test_binary, y_prob)

print("\nAccuracy :", round(accuracy,4))
print("Precision:", round(precision,4))
print("Recall   :", round(recall,4))
print("F1 Score :", round(f1,4))
print("ROC AUC  :", round(roc_auc,4))

# --------------------------------------------------
# Save Metrics
# --------------------------------------------------

metrics = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ],

    "Value":[
        accuracy,
        precision,
        recall,
        f1,
        roc_auc
    ]

})

metrics.to_csv(
    "../python/outputs/evaluation_metrics.csv",
    index=False
)

print("\nEvaluation metrics saved!")

# --------------------------------------------------
# Classification Report
# --------------------------------------------------

report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

report_df.to_csv(
    "../python/outputs/classification_report.csv"
)

print("Classification report saved!")

# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Rejected","Approved"]
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")

plt.tight_layout()

plt.savefig("../python/outputs/confusion_matrix.png")

plt.close()

print("Confusion Matrix saved!")

print("\nMODEL EVALUATION COMPLETED SUCCESSFULLY!")