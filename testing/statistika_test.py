import unittest
import numpy as np
from OpenSeries import statistika as statistika
from OpenSeries.util import error as pesan_error


class TestFungsiEntropy(unittest.TestCase):
    def test_entropy_dengan_none(self):
        label = [1, 1, 2, 2, 3, 3]
        hasil = statistika.entropy(label)
        self.assertFalse(np.allclose(hasil, 1.584962500721156))

    def test_nilai_kosong(self):
        label = []
        hasil = statistika.entropy(label)
        self.assertEqual(hasil, pesan_error.error_format("label tidak boleh kosong"))

    def test_nilai_element_dalam_label(self):
        label = [1, 2, "3", 4]
        hasil = statistika.entropy(label)
        self.assertEqual(hasil, pesan_error.error_tipe_data(["int"]))

    def test_tipe_data_tuple(self):
        label = (1, 2, 3)
        hasil = statistika.entropy(label)
        self.assertEqual(hasil, pesan_error.error_tipe_data(["list"]))
