import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
from app.Cleaner import CsvCleaner
from app.Trainer import Trainer
from app.Classifier import Classifier

app = FastAPI()
path = 'data/data for NB buys computer - Sheet1.csv'
df = CsvCleaner.basic_data_cleaner(path)
classifier = Trainer(df, "Buy_Computer")
probability_dictionary = classifier.probability_dictionary()
sum_target_dict = classifier.sum_target_variable
@app.get("/predict")
async def predict(request: Request):
    features = dict(request.query_params)
    if not features:
        return {"error": "No input features provided"}
    prediction = Classifier(probability_dictionary, sum_target_dict).classification(features)
    return {"prediction": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host= "127.0.0.1", port=8000)