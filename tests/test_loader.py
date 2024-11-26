import sys
sys.path.append('..') # add parent dir to path

import unittest
from neurodebug.loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = DataLoader("sample_dataset.csv")
        data = loader.load_data()
        self.assertIsNotNone(data)
        self.assertEqual(len(data.columns), 5)  # Check column count

if __name__ == "__main__":
    unittest.main()

