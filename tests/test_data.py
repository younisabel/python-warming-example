import unittest
import os
from warming.data.summary import Summary

class TestDataSummary(unittest.TestCase):

    def setUp(self) -> None:
        os.chdir("..")
        self.data = Summary()

    def test_co2_data_len(self):
        self.assertEqual(176, len(self.data.co2()))

if __name__ == "__main__":
    unittest.main()