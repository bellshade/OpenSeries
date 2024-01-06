import unittest
from OpenSeries import matematika as matematika


class TestKelilingLingkaran(unittest.TestCase):
    def test_keliling_lingkaran(self):
        jari = 2
        nilai_ekspetasi = 12.566370614359172
        nilai_aktual = matematika.keliling_lingkaran(jari)
        self.assertEqual(nilai_aktual, nilai_ekspetasi)
