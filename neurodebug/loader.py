import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def summary(self):
        return self.data.describe()

    def preview(self, n=5):
        return self.data.head(n)
