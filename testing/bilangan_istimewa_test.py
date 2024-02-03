import unittest
import OpenSeries.bilangan_istimewa as bilangan
import OpenSeries.util.error as error


class TestAngkaArmstrong(unittest.TestCase):
    def test_angka_armstrong(self):
        self.assertEqual(bilangan.angka_armstrong(153), "Angka armstrong")
        self.assertEqual(bilangan.angka_armstrong(370), "Angka armstrong")

    def test_salah_armstrong(self):
        self.assertEqual(bilangan.angka_armstrong(222), "Bukan Angka armstrong")
        self.assertEqual(bilangan.angka_armstrong(444), "Bukan Angka armstrong")

    def test_salah_tipe_data_armstrong(self):
        hasil = bilangan.angka_armstrong(333.2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil
