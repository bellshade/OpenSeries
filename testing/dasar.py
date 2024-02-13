import unittest
import OpenSeries as opseries


class TestBulat(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(opseries.bulat(5), 5)
