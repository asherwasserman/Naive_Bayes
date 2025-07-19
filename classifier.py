import pandas as pd
class Classifier:
    def __init__(self, data_frame, target_variable):
        self.data_frame = data_frame
        self.target_variable = target_variable

    def filling_the_dictionary_with_values(self):
        statistic_dictionary = self.filling_with_zeros()
        for column in self.data_frame.columns:
            values_in_column = self.data_frame.groupby([self.target_variable, column]).size()
            for ( target_variable, unique_values), count in values_in_column.items():
                statistic_dictionary[target_variable][column][unique_values] = count
        return statistic_dictionary

    def probability_dictionary(self):
        pass


    def filling_with_zeros(self):
        dictionary_with_zeros = {}
        for target_variable in self.data_frame[self.target_variable].unique():
            if target_variable not in dictionary_with_zeros:
                dictionary_with_zeros[target_variable] = {}
            for column in self.data_frame.columns:
                unique_values = self.data_frame[column].unique()
                if column not in dictionary_with_zeros[target_variable]:
                    dictionary_with_zeros[target_variable][column] = {}
                for u in unique_values:
                    dictionary_with_zeros[target_variable][column][u] = 0
        return dictionary_with_zeros