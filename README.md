# titanic-survival
🚢  ## **Titanic Survival Prediction API**

📌 **Project Overview**

This is an end-to-end machine learning classification project where I trained a model to predict Titanic survival and deployed it as a FastAPI REST API

**Exploratory Data Analysis (EDA)**

I started by understanding distributions, categorical balance, and correlations to guide preprocessing decisions.

Discovered some issues;

Class Imbalance

<img width="1920" height="931" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/4b92ffd1-fc32-4d3f-9551-056bb09cfc94" />

Skewed features/ outliers

<img width="1806" height="946" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/f9df9633-356f-4121-a0d9-5ab2761f1b33" />

Missing values

<img width="1806" height="770" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/122d99f3-e448-434f-8fdc-226bb9226bc1" />

**Data Wrangling & Feature Engineering**

I created reusable functions to handle missing values, skewness, and outliers in a consistent way;

1. Median mode inputation
2. Log transformation for skew
3. IQR-based outlier handling
4. Explicit reasoning for each step
   
<img width="1796" height="900" alt="Screenshot (16)" src="https://github.com/user-attachments/assets/b8f83c8a-1743-4571-a3c1-c586df753e71" />

<img width="1801" height="935" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/4d531335-0dec-4b3f-8002-932ae0ce9168" />

🧠 **Machine Learning Details**

- Problem Type: Binary Classification
- Target Variable: Survived (0 = Did not survive, 1 = Survived)
- Model: Logistic Regression
- Pipeline Includes:Missing value imputation, Log transformation for skewed numerical features, Outlier capping (IQR method),One-hot encoding for nominal categorical variables, Scaling with StandardScaler
  
<img width="1795" height="926" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/3edf2be4-ab92-4039-bc20-8895289746eb" />

<img width="1798" height="939" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/303cbdb4-a579-4282-87b1-25758e830108" />

📊 **Model Performance**

Interpretation:

- The model performs well at identifying non-survivors
- Reasonable recall on survivors given class imbalance
- Suitable baseline model for further tuning
- 
<img width="1796" height="820" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/205efab6-42d0-401d-9336-51e310e1248a" />

I improved model performance by using Class weighted Logistics Regression

<img width="1775" height="835" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/4267adc6-dff1-4b2e-a868-b573443d6afd" />

<img width="1920" height="828" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/f71e04ec-7877-4d3d-9636-af2c9fdec4b1" />

🗂 **FAST API Project Structure**

<img width="894" height="444" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/493a47ab-e3b0-4bac-9a23-dd6e2922dfb8" />

📚 **API Documentation (Swagger)**

Open in your browser:

http://127.0.0.1:8000/docs

Use the interactive UI to test predictions easily.

🔮 **Making a Prediction**

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

🧑‍💻 **Author**

Olufemi Makinde

Data Scientist | Machine Learning Engineer
