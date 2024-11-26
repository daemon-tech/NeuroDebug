import sys
sys.path.append("..")

import unittest
import pandas as pd
from neurodebug.analyzer import DataAnalyzer
from neurodebug.fixer import MissingValueHandler
from neurodebug.visualizer import MissingValueVisualizer

class TestMissingValues(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "A": [1, None, 3, None],
            "B": [None, 2, 3, None],
            "C": [1, 1, 1, 1]
        })

    def test_detailed_report(self):
        analyzer = DataAnalyzer(self.data)
        report = analyzer.detailed_report()
        self.assertEqual(report["total_missing"], 4)
        self.assertIn("A", report["missing_by_column"])

    def test_imputation(self):
        handler = MissingValueHandler(self.data)
        imputed_data = handler.impute(strategy="mean")
        self.assertFalse(imputed_data.isnull().values.any())

if __name__ == "__main__":
    unittest.main()
