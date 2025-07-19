import pandas as pd
class Classifier:
    def __init__(self, data_frame, target_variable):
        self.data_frame = data_frame
        self.target_variable = target_variable
        self.sum_target_variable = self.data_frame.groupby(target_variable).size().to_dict()

    def filling_with_zeros(self):
        dictionary_with_zeros = {}
        for target_variable in self.data_frame[self.target_variable].unique():
            if target_variable not in dictionary_with_zeros:
                dictionary_with_zeros[target_variable] = {}
            for column in self.data_frame.columns:
                if column == self.target_variable:
                    continue
                unique_values = self.data_frame[column].unique()
                if column not in dictionary_with_zeros[target_variable]:
                    dictionary_with_zeros[target_variable][column] = {}
                for u in unique_values:
                    dictionary_with_zeros[target_variable][column][u] = 0
        return dictionary_with_zeros

    def filling_the_dictionary_with_values(self):
        statistic_dictionary = self.filling_with_zeros()
        for column in self.data_frame.columns:
            if column == self.target_variable:
                continue
            values_in_column = self.data_frame.groupby([self.target_variable, column]).size()
            for ( target_variable, unique_values), count in values_in_column.items():
                statistic_dictionary[target_variable][column][unique_values] = count
        return statistic_dictionary

    def probability_dictionary(self):
        statistic_dictionary = self.filling_the_dictionary_with_values()
        for target in statistic_dictionary:
            for column in statistic_dictionary[target]:
                denominator = self.sum_target_variable[target]
                for value in statistic_dictionary[target][column]:
                    if statistic_dictionary[target][column][value] == 0:
                        statistic_dictionary[target][column][value] +=1
                        denominator += 1
                for value in statistic_dictionary[target][column]:
                    statistic_dictionary[target][column][value] = statistic_dictionary[target][column][value] / denominator
        return statistic_dictionary






