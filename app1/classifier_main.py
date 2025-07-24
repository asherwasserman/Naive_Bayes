import pandas as pd
from fastapi import FastAPI, Request
from Classifier import Classifier
import requests

def get_probability():
    response = requests.get("http://api_gateway:8000/")
    return response.json()
data = get_probability()
probability_dictionary = data[0]
sum_target_dict = data[1]

app = FastAPI()



@app.get("/predict")
async def predict(request: Request):
    features = dict(request.query_params)
    if not features:
        return {"error": "No input features provided"}
    prediction = Classifier(probability_dictionary, sum_target_dict).classification(features)
    return {"prediction": prediction}