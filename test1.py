from neurodebug.loader import DataLoader
from neurodebug.analyzer import DataAnalyzer
from neurodebug.visualizer import DataVisualizer

loader = DataLoader("tests/sample_dataset.csv")
data = loader.load_data()
print(loader.preview_data())

analyzer = DataAnalyzer(data)
summary = analyzer.summerize_data()
print(summary)
print('---------------------')

missing = analyzer.missing_values()
print("Missing Values:", missing)

vis = DataVisualizer(data)
vis.plot_missing_values()
