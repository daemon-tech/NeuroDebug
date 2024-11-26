class DataAnalyzer:
    def __init__(self, data):

        # init with pandas dataFrame
        self.data = data

    def summerize_data(self):
        # provide summary to dataset
        summary = {
                "Columns": self.data.columns.tolist(),
                "Data Types": self.data.dtypes.to_dict(),
                "Missing Values": self.data.isnull().sum().to_dict(),
                "Total Rows": len(self.data),
                "Total Columns": len(self.data.columns),
                }
        return summary

    def missing_values(self):
        # detect missing values
        missing = self.data.isnull().sum()
        return missing[missing > 0].to_dict()

    def detailed_report(self, threshold=0.3):
        """
        Generate a detailed report on missing values.

        Args:
            threshold (float): Percentage threshold to flag significant missing values.

        Returns:
            dict: Summary of missing values and flagged columns.
        """
        missing_counts = self.data.isnull().sum()
        total_rows = len(self.data)
        missing_percentage = (missing_counts / total_rows).sort_values(ascending=False)

        significant_missing = missing_percentage[missing_percentage > threshold]

        return {
            "total_missing": missing_counts.sum(),
            "missing_by_column": missing_counts.to_dict(),
            "percentage_missing": missing_percentage.to_dict(),
            "significant_missing_columns": significant_missing.to_dict(),
        }
