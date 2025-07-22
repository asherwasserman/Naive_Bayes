from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
from CsvCleaner import CsvCleanerForClassifiers
from classifier import Classifier

app = FastAPI()
df = CsvCleanerForClassifiers.basic_data_cleaner("data for NB buys computer - Sheet1.csv")
classifier = Classifier(df, "Buy_Computer")
@app.get("/predict")
async def predict(request: Request):
    features = dict(request.query_params)
    if not features:
        return {"error": "No input features provided"}
    prediction = classifier.classifier(features)
    return {"prediction": prediction}