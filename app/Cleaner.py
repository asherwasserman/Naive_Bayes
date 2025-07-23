import pandas as pd
class CsvCleanerForClassifiers:
    @staticmethod
    def basic_data_cleaner(csv_file):
        df = pd.read_csv(csv_file)
        df = df.drop_duplicates()
        df = df.dropna()
        for i in df.columns:
            if "id" in i.lower():
                df = df.drop(columns=[i])
        return df