class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def missing_values(self):
        return self.data.isnull().sum()

    def outliers(self, column):
        q1 = self.data[column].quantile(0.25)
        q3 = self.data[column].quantile(0.75)
        iqr = q3 - q1
        return self.data[(self.data[column] < q1 - 1.5 * iqr) |
                         (self.data[column] > q3 + 1.5 * iqr)]

    def class_imbalance(self, target_column):
        return self.data[target_column].value_counts(normalize=True)
