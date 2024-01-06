import unittest
import OpenSeries.matematika as matematika


class TestKelilingLingkaran(unittest.TestCase):
    def cek_hasil(self):
        jari = 2
        nilai_ekspetasi = 12.566370614359172
        nilia_aktual = matematika.keliling_lingkaran(jari)
        self.assertEqual(nilia_aktual, nilai_ekspetasi)
