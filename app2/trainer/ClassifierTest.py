import pandas as pd
from Cleaner import CsvCleaner
from Trainer import Trainer
class Test:
    def __init__(self,df ,target_variable ):
        self.df = df
        self.target_variable = target_variable
        self.to_classify, self.to_examine = self.part_data()
        self.classifier = Trainer(self.to_classify, target_variable)

    def part_data(self):
        divider = int(len(self.df) * 0.7)
        to_classify = self.df.iloc[:divider]
        to_examine = self.df.iloc[divider:]
        return [to_classify, to_examine]

    def reliability_check(self):
        true_classify = 0
        num_classify = 0
        for index, row in self.to_examine.iterrows():
            data_dictionary = row.to_dict()
            result = self.classifier.classifier(data_dictionary)
            if result == row[self.target_variable]:
                true_classify += 1
            num_classify += 1
        percent = (true_classify / num_classify) * 100
        percent = round(percent, 2)
        return percent
a = CsvCleaner.basic_data_cleaner("data for NB buys computer - Sheet1.csv")
b = Test(a, "Buy_Computer").reliability_check()
print(b)