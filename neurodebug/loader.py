import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        # Initialize the dataloader with the file path
        self.filepath = filepath
        self.data = None

    def load_data(self):
        # load data from a csv file and return pandas dataframe
        try:
            self.data = pd.read_csv(self.filepath)
            print(f'Data loaded successfully from {self.filepath}')
            return self.data

        except Exception as e:
            print(f'Error loading data: {e}')
            return None

    def summary(self):
        return self.data.describe()

    def preview_data(self, n=5):
        if self.data is not None:
            return self.data.head(n)
        else:
            print('No data loaded yet. Use load_data() function first')
            return None
