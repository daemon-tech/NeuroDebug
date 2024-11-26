from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer

class MissingValuePipeline:
    @staticmethod
    def create_pipeline(strategy="mean", k_neighbors=5, constant_value=None):
        """
        Create a scikit-learn pipeline for missing value handling.

        Args:
            strategy (str): Imputation strategy.
            k_neighbors (int): Number of neighbors for KNN imputation.
            constant_value (any): Value for constant imputation.

        Returns:
            sklearn.pipeline.Pipeline: Configured pipeline.
        """
        if strategy in ["mean", "median", "most_frequent", "constant"]:
            fill_value = constant_value if strategy == "constant" else None
            imputer = SimpleImputer(strategy=strategy, fill_value=fill_value)
        elif strategy == "knn":
            imputer = KNNImputer(n_neighbors=k_neighbors)
        else:
            raise ValueError(f"Unsupported strategy: {strategy}")

        pipeline = Pipeline([("imputer", imputer)])
        return pipeline
