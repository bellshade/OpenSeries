import unittest
import OpenSeries as opseries
import OpenSeries.util.error as error


class TestBulat(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(opseries.bulat(5), 5)

    def test_valid_nilai_float(self):
        self.assertEqual(opseries.bulat(5.6), 6)

    def test_valid_nilai_negatif_int(self):
        self.assertEqual(opseries.bulat(-5.6), -5)

    def test_valid_float_cek_true(self):
        self.assertEqual(opseries.bulat(5.6, True), 5)

    def test_error_tipe_data(self):
        with self.assertRaises(error.ErrorTipeData):
            raise opseries.bulat("2.5")
