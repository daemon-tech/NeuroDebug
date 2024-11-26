import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_missing_values(self):
        missing = self.data.isnull().sum()
        plt.bar(missing.index, missing.values)
        plt.title("Missing Values")
        plt.show()

    def plot_feature_distribution(self, column):
        self.data[column].hist(bins=50)
        plt.title(f"Distribution of {column}")
        plt.show()
