from neurodebug.loader import DataLoader
from neurodebug.analyzer import DataAnalyzer

loader = DataLoader("tests/sample_dataset.csv")
data = loader.load_data()
print(loader.preview_data())

analyzer = DataAnalyzer(data)
summary = analyzer.summerize_data()
print(summary)
