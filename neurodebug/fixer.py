import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer

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

class MissingValueHandler:
    def __init__(self, data):
        self.data = data

    def impute(self, strategy="mean", k_neighbors=5, constant_value=None):
        """
        Impute missing values using different strategies.

        Args:
            strategy (str): Imputation strategy ("mean", "median", "most_frequent", "constant", "knn").
            k_neighbors (int): Number of neighbors to use for KNN imputation (if applicable).
            constant_value (any): Value to use for constant strategy (if applicable).

        Returns:
            pandas.DataFrame: Data with imputed values.
        """
        if strategy in ["mean", "median", "most_frequent", "constant"]:
            fill_value = constant_value if strategy == "constant" else None
            imputer = SimpleImputer(strategy=strategy, fill_value=fill_value)
        elif strategy == "knn":
            imputer = KNNImputer(n_neighbors=k_neighbors)
        else:
            raise ValueError(f"Unsupported strategy: {strategy}")

        imputed_data = imputer.fit_transform(self.data)
        return pd.DataFrame(imputed_data, columns=self.data.columns)
