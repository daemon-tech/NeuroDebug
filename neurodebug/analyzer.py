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
