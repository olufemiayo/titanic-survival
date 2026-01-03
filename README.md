# titanic-survival
🚢  **Titanic Survival Prediction API**


📌 Project Overview

This project demonstrates how to:

Clean and preprocess real-world tabular data

Handle missing values, skewness, and outliers

Encode categorical and ordinal variables correctly

Train and evaluate a classification model

Package the full preprocessing + model pipeline

Serve predictions through a REST API using FastAPI

Test the API using Swagger UI, PowerShell, and curl

Containerize the application with Docker

🧠 Machine Learning Details

Problem Type: Binary Classification

Target Variable: Survived (0 = Did not survive, 1 = Survived)

Model: Logistic Regression

Pipeline Includes:

Missing value imputation

Log transformation for skewed numerical features

Outlier capping (IQR method)

One-hot encoding for nominal categorical variables

Scaling with StandardScaler

📊 Model Performance
Accuracy: 0.78

Confusion Matrix:
[[95 15]
 [24 45]]

Classification Report:
              precision    recall  f1-score
Not Survived      0.80      0.86      0.83
Survived          0.75      0.65      0.70


Interpretation:

The model performs well at identifying non-survivors

Reasonable recall on survivors given class imbalance

Suitable baseline model for further tuning

🗂 Project Structure
titanic/
│
├── app/
│   ├── main.py          # FastAPI application
│   ├── model.py         # Model loading logic
│   ├── schemas.py       # Pydantic request/response models
│
├── model/
│   └── titanic_model.pkl  # Trained ML pipeline
│
├── Titanic.ipynb        # Data analysis & model training notebook
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── README.md           # Project documentation


API will be available at:

http://127.0.0.1:8000

📚 API Documentation (Swagger)

Open in your browser:

http://127.0.0.1:8000/docs


Use the interactive UI to test predictions easily.

🔮 Making a Prediction
Example Request (JSON)
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 40,
  "SibSp": 2,
  "Parch": 2,
  "Fare": 7.25,
  "Embarked": "S"
}

Example Response
{
  "survived": 0,
  "survival_probability": 0.203
}

🐳 Docker (Optional)
Build image
docker build -t titanic-api .

Run container
docker run -p 8000:8000 titanic-api


🧑‍💻 Author

Olufemi Makinde
Data Scientist | Machine Learning Engineer

This project was built to demonstrate production-ready ML engineering skills, not just model accuracy.

⭐ Final Note

This repository showcases:

Practical ML preprocessing

Clean model pipelines

Real API deployment

Debugging and production awareness

If you’re a recruiter or reviewer — this project reflects real-world ML work, not just a notebook experiment.
