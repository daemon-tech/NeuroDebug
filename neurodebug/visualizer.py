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

class MissingValueVisualizer:
    def __init__(self, data):
        self.data = data

    def bar_chart(self):
        """
        Visualize missing values as a bar chart.
        """
        missing_counts = self.data.isnull().sum()
        missing_counts = missing_counts[missing_counts > 0].sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        missing_counts.plot(kind="bar", color="skyblue")
        plt.title("Missing Values by Column")
        plt.ylabel("Count")
        plt.show()

    def heatmap(self, sample_size=1000):
        """
        Visualize missing values as a heatmap for a sample of the data.

        Args:
            sample_size (int): Number of rows to sample for visualization.
        """
        sample_data = self.data.sample(n=min(len(self.data), sample_size), random_state=42)
        plt.figure(figsize=(12, 8))
        sns.heatmap(sample_data.isnull(), cbar=False, cmap="viridis")
        plt.title("Missing Values Heatmap (Sample)")
        plt.show()
