import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_missing_values(self):
        # visualize missing values using a heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.data.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap")
        plt.show()

    def plot_feature_distribution(self, column):
        self.data[column].hist(bins=50)
        plt.title(f"Distribution of {column}")
        plt.show()


