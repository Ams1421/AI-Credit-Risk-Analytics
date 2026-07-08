# AI Credit Risk Analytics Dashboard

---

# Version Information

| Property | Value |
|----------|-------|
| Project | AI Credit Risk Analytics Dashboard |
| Version | 1.0 |
| Deployment Type | Local Development |
| Platform | Windows / Linux / macOS |
| IDE | Visual Studio Code |

---

# 1. Introduction

This guide provides step-by-step instructions to deploy and run the AI Credit Risk Analytics Dashboard.

The project includes:

- Python Data Processing
- MySQL Database
- Power BI Dashboard
- Machine Learning Pipeline

Following this guide will recreate the complete project from scratch.

---

# 2. System Requirements

## Hardware

| Component | Minimum |
|-----------|----------|
| RAM | 8 GB |
| Storage | 2 GB Free |
| Processor | Intel i5 / AMD Ryzen 5 |

---

## Software

Install the following software before running the project.

| Software | Version |
|----------|---------|
| Python | 3.10 or later |
| MySQL Server | 8.0+ |
| MySQL Workbench | Latest |
| Power BI Desktop | Latest |
| Visual Studio Code | Latest |
| Git | Latest |

---

# 3. Clone Repository

Clone the project from GitHub.

```bash
git clone https://github.com/Ams1421/AI-Credit-Risk-Analytics.git
```

Move into the project directory.

```bash
cd AI-Credit-Risk-Analytics
```

---

# 4. Install Python Dependencies

Install all required libraries.

```bash
pip install -r requirements.txt
```

Verify installation.

```bash
pip list
```

---

# 5. Project Structure

```
AI-Credit-Risk-Analytics/

dataset/

python/

mysql/

powerbi/

reports/

images/

README.md

requirements.txt
```

---

# 6. Dataset Setup

Copy the following files into the dataset folder.

```
loan_train.csv

loan_test.csv
```

Location

```
dataset/
```

---

# 7. Execute Python Pipeline

Run each script in the following order.

## Step 1

```bash
python 01_data_loading.py
```

---

## Step 2

```bash
python 02_data_cleaning.py
```

---

## Step 3

```bash
python 03_eda.py
```

---

## Step 4

```bash
python 04_visualization.py
```

---

## Step 5

```bash
python 05_feature_engineering.py
```

---

## Step 6

```bash
python 06_data_preprocessing.py
```

---

## Step 7

```bash
python 07_model_training.py
```

---

## Step 8

```bash
python 08_model_evaluation.py
```

---

## Step 9

```bash
python 09_prediction.py
```

---

# 8. Expected Python Outputs

After successful execution the following files should be generated.

```
processed_data.csv

featured_data.csv

predictions.csv

model_metrics.csv

evaluation_metrics.csv

classification_report.csv

confusion_matrix.png

best_pipeline.pkl

preprocessor.pkl
```

---

# 9. MySQL Deployment

Create a database.

```sql
CREATE DATABASE loan_analysis;
```

Use the database.

```sql
USE loan_analysis;
```

Import

```
featured_data.csv
```

Execute

```
loan_analysis.sql
```

Verify

```sql
SELECT COUNT(*)
FROM loan_applications;
```

Expected Result

```
614
```

---

# 10. Power BI Deployment

Open

```
loan_dashboard.pbix
```

Refresh Data

```
Home

↓

Refresh
```

Verify

- KPI Cards
- Charts
- Slicers
- Filters

---

# 11. Machine Learning Deployment

The trained model is automatically saved as

```
best_pipeline.pkl
```

Prediction

```
python 09_prediction.py
```

Output

```
predictions.csv
```

---

# 12. Generated Reports

The project automatically generates

```
model_metrics.csv

evaluation_metrics.csv

classification_report.csv

predictions.csv
```

These outputs can be imported into Power BI or used for further analysis.

---

# 13. Troubleshooting

## Missing Library

Install dependencies again.

```bash
pip install -r requirements.txt
```

---

## MySQL Import Error

Check

- Database selected
- CSV delimiter
- Column names
- Data types

---

## Power BI Refresh Error

Verify

- Dataset location
- Column names
- Data source path

---

## Python Errors

Check

- Python version
- Installed packages
- Dataset path
- File names

---

# 14. Folder Verification

Before running the project, verify the structure.

```
dataset/

python/

mysql/

powerbi/

reports/

images/

README.md

requirements.txt
```

---

# 15. Future Deployment

The project can be extended using

- Docker
- FastAPI
- Azure App Service
- AWS EC2
- Power BI Service
- Azure SQL Database

---

# 16. Conclusion

Following this deployment guide enables users to recreate the complete AI Credit Risk Analytics Dashboard on a local machine.

The modular architecture and step-by-step execution process ensure reproducibility, maintainability, and ease of deployment for future enhancements.