from fastapi import FastAPI
import pandas as pd

from app.schemas import Passenger
from app.model import load_model

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="Predict survival of Titanic passengers",
    version="1.0"
)

model = load_model()


@app.get("/")
def home():
    return {"message": "Titanic ML API is running 🚢"}


@app.post("/predict")
def predict_survival(passenger: Passenger):
    data = pd.DataFrame([passenger.dict()])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "survived": int(prediction),
        "survival_probability": round(float(probability), 3)
    }








