import unittest
import numpy as np
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
        self.iterasi = 4

    def test_akar_integer(self):
        self.assertEqual(opseries.akar(self.angka), 2)

    def test_akar_floar(self):
        self.assertEqual(opseries.akar(float(self.angka)), 2.0)

    def test_akar_string(self):
        with self.assertRaises(error.ErrorTipeData):
            raise opseries.akar(str(self.angka))

    def test_akar_iterasi_int(self):
        self.assertEqual(opseries.akar(self.angka, iterasi=self.iterasi), 2)

    def test_akar_iterasi_float(self):
        with self.assertRaises(error.ErrorTipeData):
            raise opseries.akar(self.angka, float(self.iterasi))

    def test_akar_iterasi_string(self):
        with self.assertRaises(error.ErrorTipeData):
            raise opseries.akar(self.angka, str(self.iterasi))


class TestTanHiperbolik(unittest.TestCase):
    def test_tan_hiperbolik_valid(self):
        array = np.array([0.5, 1.0, -0.5])
        self.assertTrue(np.allclose(opseries.tan_hiperbolik(array), np.tanh(array)))

    def test_tan_invalid_input(self):
        input = 5
        with self.assertRaises(error.ErrorTipeData):
            raise opseries.tan_hiperbolik(input)


class TestVolumeKubus(unittest.TestCase):
    def test_volume_nilai_integer(self):
        hasil = opseries.volume_kubus(3)
        self.assertEqual(hasil, 27)

    def test_volume_nilai_float(self):
        hasil = opseries.volume_kubus(3.0)
        self.assertEqual(hasil, 27.0)

    def test_nilai_invalid_str(self):
        hasil = opseries.volume_kubus("20")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_invalid_minus(self):
        hasil = opseries.volume_kubus(-1)
        with self.assertRaises(error.Error):
            raise hasil
