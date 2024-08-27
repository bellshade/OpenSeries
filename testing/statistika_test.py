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
        with self.assertRaises(pesan_error.Error):
            raise hasil

    def test_nilai_element_dalam_label(self):
        label = [1, 2, "3", 4]
        hasil = statistika.entropy(label, base=2)
        with self.assertRaises(pesan_error.ErrorTipeData):
            raise hasil

    def test_tipe_data_tuple(self):
        label = (1, 2, 3)
        hasil = statistika.entropy(label, base=2)
        with self.assertRaises(pesan_error.ErrorTipeData):
            raise hasil


class TestFungiStandardDeviasi(unittest.TestCase):
    def test_standard_deviasi_dengan_numpy_array(self):
        vektor = np.array([1, 2, 3, 4, 5])
        hasil = statistika.standar_deviasi(vektor)
        self.assertAlmostEqual(hasil, np.std(vektor), places=2)

    def test_standard_deviasi_dengan_list(self):
        vektor = [1, 2, 3, 4, 5]
        hasil = statistika.standar_deviasi(vektor)
        with self.assertRaises(pesan_error.ErrorTipeData):
            raise hasil

    def test_standard_deviasi_dengan_numpy_kosong(self):
        vektor = np.array([])
        hasil = statistika.standar_deviasi(vektor)
        with self.assertRaises(pesan_error.Error):
            raise hasil


class TestFungsiVarian(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.ekpetasi = 2.0

    def test_variance_dengan_nilai_bulat(self):
        hasil = statistika.variance(self.data)
        self.assertEqual(hasil, self.ekpetasi)

    def test_variance_dengan_nilai_desimal(self):
        data_decimal = [float(val) for val in self.data]
        hasil = statistika.variance(data_decimal)
        self.assertEqual(hasil, self.ekpetasi)

    def test_variance_dengan_nilai_string(self):
        data_string = [str(val) for val in self.data]
        hasil = statistika.variance(data_string)
        with self.assertRaises(pesan_error.ErrorTipeData):
            raise hasil

    def test_variance_dengan_list_blank(self):
        blank_data = []
        hasil = statistika.variance(blank_data)
        with self.assertRaises(pesan_error.Error):
            raise hasil
