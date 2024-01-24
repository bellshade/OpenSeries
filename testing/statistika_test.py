import unittest
import numpy as np
from OpenSeries import statistika as statistika
from OpenSeries.util import error as pesan_error


class TestFungsiEntropy(unittest.TestCase):
    def test_entropy_dengan_none(self):
        label = [1, 1, 2, 2, 3, 3]
        hasil = statistika.entropy(label, base=2)
        self.assertTrue(np.allclose(hasil, 1.584962500721156))

    def test_nilai_kosong(self):
        label = []
        hasil = statistika.entropy(label, base=2)
        self.assertEqual(hasil, pesan_error.error_format("label tidak boleh kosong"))

    def test_nilai_element_dalam_label(self):
        label = [1, 2, "3", 4]
        hasil = statistika.entropy(label, base=2)
        self.assertEqual(hasil, pesan_error.error_tipe_data(["int"]))

    def test_tipe_data_tuple(self):
        label = (1, 2, 3)
        hasil = statistika.entropy(label, base=2)
        self.assertEqual(hasil, pesan_error.error_tipe_data(["list"]))


class TestFungiStandardDeviasi(unittest.TestCase):
    def test_standard_deviasi_dengan_numpy_array(self):
        vektor = np.array([1, 2, 3, 4, 5])
        hasil = statistika.standar_deviasi(vektor)
        self.assertAlmostEqual(hasil, np.std(vektor), places=2)

    def test_standard_deviasi_dengan_list(self):
        vektor = [1, 2, 3, 4, 5]
        hasil = statistika.standar_deviasi(vektor)
        self.assertEqual(hasil, pesan_error.error_tipe_data(["numpy array"]))

    def test_standard_deviasi_dengan_numpy_kosong(self):
        vektor = np.array([])
        hasil = statistika.standar_deviasi(vektor)
        self.assertEqual(hasil, pesan_error.error_format("vektor tidak boleh kosong"))
