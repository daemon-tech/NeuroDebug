import unittest
from neurodebug.loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = DataLoader("tests/sample_dataset.csv")
        self.assertIsNotNone(loader.data)

if __name__ == "__main__":
    unittest.main()
