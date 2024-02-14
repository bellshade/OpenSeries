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


class TestAkar(unittest.TestCase):
    def setUp(self):
        self.angka = 4

    def test_akar_integer(self):
        self.assertEqual(opseries.akar(self.angka), 2)

    def test_akar_floar(self):
        self.assertEqual(opseries.akar(float(self.angka)), 2.0)

    def test_akar_string(self):
        with self.assertRaises(error.ErrorTipeData):
            raise opseries.akar(str(self.angka))