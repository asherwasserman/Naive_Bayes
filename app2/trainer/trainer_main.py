from fastapi import FastAPI
from trainer.Trainer import Trainer
from trainer.Cleaner import CsvCleaner

path = 'data/data for NB buys computer - Sheet1.csv'
df = CsvCleaner.basic_data_cleaner(path)
classifier = Trainer(df, "Buy_Computer")
probability_dictionary = classifier.probability_dictionary()
sum_target_variable = classifier.sum_target_variable

app = FastAPI()

@app.get("/")
async def get_dictionary():
    return probability_dictionary, sum_target_variable



