import unittest
import OpenSeries.bilangan_istimewa as bilangan
import OpenSeries.util.error as error


class TestAngkaArmstrong(unittest.TestCase):
    def test_angka_armstrong(self):
        self.assertEqual(bilangan.angka_armstrong(153), "angka armstrong".capitalize())
        self.assertEqual(bilangan.angka_armstrong(370), "angka armstrong".capitalize())

    def test_salah_armstrong(self):
        self.assertEqual(
            bilangan.angka_armstrong(222), "bukan angka armstrong".capitalize()
        )
        self.assertEqual(
            bilangan.angka_armstrong(444), "bukan angka armstrong".capitalize()
        )

    def test_salah_tipe_data_armstrong(self):
        hasil = bilangan.angka_armstrong(333.2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestAngkaAutomorphic(unittest.TestCase):
    def test_tipe_data_angka(self):
        with self.assertRaises(error.ErrorTipeData):
            raise bilangan.angka_automorphic(12.3)
            raise bilangan.angka_automorphic("23")

    def test_angka_negatif(self):
        hasil = bilangan.angka_automorphic(-2)
        self.assertEqual(hasil, "bukan angka automorphic".capitalize())

    def test_valid_input(self):
        hasil = bilangan.angka_automorphic(25)
        self.assertEqual(hasil, "angka automorphic".capitalize())


class TestAngkaPronic(unittest.TestCase):
    def test_angka_pronic_return_tipe_data(self):
        hasil = bilangan.angka_pronic(30)
        self.assertIsInstance(hasil, str)

        hasil = bilangan.angka_pronic("30")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_angka_pronic_negatif(self):
        hasil = bilangan.angka_pronic(-30)
        self.assertIsInstance(hasil, str)


class TestAngkaSegitiga(unittest.TestCase):
    def test_angka_segitiga(self):
        self.assertEqual(bilangan.angka_segitiga(0), 0)
        self.assertEqual(bilangan.angka_segitiga(3), 6)

    def test_angka_negatif(self):
        hasil = bilangan.angka_segitiga(-1)
        with self.assertRaises(error.Error):
            raise hasil

    def test_beda_tipe_data(self):
        hasil = bilangan.angka_segitiga("12")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestAngkaKatalan(unittest.TestCase):
    def test_angka_valid(self):
        self.assertEqual(bilangan.angka_katalan(1), 1)
        self.assertEqual(bilangan.angka_katalan(4), 5)

    def test_katalan_tipe_data(self):
        self.assertIsInstance(bilangan.angka_katalan("3"), error.ErrorTipeData)

    def test_katalan_negatif(self):
        self.assertIsInstance(bilangan.angka_katalan(-2), error.Error)
