class DataFixer:
    def __init__(self, data):
        self.data = data

    def impute_missing(self, method="mean"):
        if method == "mean":
            return self.data.fillna(self.data.mean())
        elif method == "median":
            return self.data.fillna(self.data.median())
        elif method == "mode":
            return self.data.fillna(self.data.mode().iloc[0])
