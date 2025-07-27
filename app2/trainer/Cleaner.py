import pandas as pd
class CsvCleaner:
    @staticmethod
    def basic_data_cleaner(df):
        df = df.drop_duplicates()
        df = df.dropna()
        for i in df.columns:
            if "id" in i.lower():
                df = df.drop(columns=[i])
        return df