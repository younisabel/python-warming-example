import os
import unittest
from warming.plot.maps import World

class TestMapWorld(unittest.TestCase):

    def setUp(self) -> None:
        os.chdir("..")
        self.data = World()

    def test_co2_data_len(self):
        self.assertEqual(177, len(self.data.get_data()))

if __name__ == "__main__":
    unittest.main()