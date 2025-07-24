class Classifier:
    def __init__(self, probability_dictionary, sum_target_dict):
        self.probability_dictionary = probability_dictionary
        self.sum_target_dict = sum_target_dict
        self.total_target_variables = sum(self.sum_target_dict.values())

    def classification(self, values_dictionary):
        probability_dictionary = {}
        target_variables = self.sum_target_dict.keys()
        statistic_dictionary = self.probability_dictionary
        for target in target_variables:
            probability_dictionary[target] = 1
            for key, value in values_dictionary.items():
                try:
                    probability_dictionary[target] *= statistic_dictionary[target][key][value]
                except:
                    continue
        for target in probability_dictionary:
            probability_dictionary[target] *= self.sum_target_dict[target] / self.total_target_variables
        max_probability = max(probability_dictionary, key = probability_dictionary.get)
        return max_probability