🚢 Titanic Survival Prediction API

End-to-End Machine Learning & FastAPI Deployment

A production-style machine learning classification project that predicts Titanic passenger survival and serves predictions via a FastAPI REST API.

This repository demonstrates real-world ML engineering skills — not just model training, but data preprocessing, pipelines, deployment, and API testing.

🔍 What This Project Shows

✔ Data cleaning & feature engineering
✔ Handling missing values, skewness, and outliers
✔ Proper categorical & ordinal encoding
✔ Scikit-learn pipelines
✔ Model evaluation & interpretation
✔ REST API development with FastAPI
✔ Dockerized ML deployment
✔ Debugging production issues (paths, versions, JSON, OS differences)

🧠 Machine Learning Overview

Problem: Binary Classification

Target: Survived (0 = No, 1 = Yes)

Model: Logistic Regression

Pipeline Includes:

Median / mode imputation

Log transformation for skewed features

IQR-based outlier capping

One-Hot Encoding for categorical variables

Feature scaling with StandardScaler

📊 Model Performance
Accuracy: 0.78

Confusion Matrix:
[[95 15]
 [24 45]]


Strong performance on non-survivors

Reasonable recall for survivors given class imbalance

Clean, interpretable baseline model

🗂 Repository Structure
titanic/
├── app/
│   ├── main.py          # FastAPI app
│   ├── model.py         # Model loader
│   └── schemas.py       # Request/response schemas
│
├── model/
│   └── titanic_model.pkl  # Trained pipeline
│
├── Titanic.ipynb        # EDA + training notebook
├── Dockerfile           # Container setup
├── requirements.txt     # Dependencies
└── README.md

▶️ Run Locally
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Open API docs:

http://127.0.0.1:8000/docs

🔮 Example API Request
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 40,
  "SibSp": 2,
  "Parch": 2,
  "Fare": 7.25,
  "Embarked": "S"
}

Response
{
  "survived": 0,
  "survival_probability": 0.18
}

🐳 Docker Support
docker build -t titanic-api .
docker run -p 8000:8000 titanic-api

🚀 Future Enhancements

Model tuning & ensemble methods

Class imbalance handling (SMOTE / class weights)

Cloud deployment (AWS / Render / Railway)

Monitoring & logging

CI/CD pipeline

👤 Author

Olufemi Makinde
Data Scientist | Machine Learning Engineer

📌 This project reflects production-oriented ML development — from data to deployed API.

⭐ Why This Repo Matters

This is not a “Kaggle-only” project.
It demonstrates how machine learning actually ships to production.