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

class TestVarian(unittest.TestCase):
    def test_varian_dengan_numpy(self):
        vektor = np.array([1,2,3,4])
        hasil = statistika.varian(vektor)
        self.assertAlmostEqual(hasil, np.var(vektor), places=2)
    def test_varian_dengan_kosong(self):
        vektor = np.array([])
        hasil = statistika.varian(vektor)
        with self.assertRaises(pesan_error.Error):
            raise hasil

class TestNilaiTengah(unittest.TestCase):
    def test_nilai_tengah_ganjil_dengan_numpy(self):
        vektor = np.array([1,2,3,4,5])
        hasil = statistika.nilai_tengah(vektor)
        self.assertAlmostEqual(hasil, np.median(vektor), places=2)
    def test_nilai_tengah_genap_dengan_numpy(self):
        vektor = np.array([1,2,3,4])
        hasil = statistika.nilai_tengah(vektor)
        self.assertAlmostEqual(hasil,np.median(vektor),places=2)
    
    def test_nilai_ganjil_dengan_list(self):
        vektor = [1,2,3,4,5]
        hasil = statistika.nilai_tengah(vektor)
        self.assertAlmostEqual(hasil,np.median(hasil),places=2)
    def test_nilai_genap_dengan_list(self):
        vektor = [1,2,3,4]
        hasil = statistika.nilai_tengah(vektor)
        self.assertAlmostEqual(hasil,np.median(hasil),places=2)
    
    def testing_dengan_kosong_list(self):
        vektor = []
        hasil = statistika.nilai_tengah(vektor)
        with self.assertRaises(pesan_error.Error):
            raise hasil
    
    def testing_dengan_numpy(self):
        vektor = np.array([])
        hasil = statistika.nilai_tengah(vektor)
        with self.assertRaises(pesan_error.Error):
            raise hasil