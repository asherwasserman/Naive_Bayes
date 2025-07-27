import pandas as pd
class Loader:
    @staticmethod
    def csv_loader(csv_file):
        df = pd.read_csv(csv_file)
        return df