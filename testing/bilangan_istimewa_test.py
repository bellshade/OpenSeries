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


class TestAngkaPolindorm(unittest.TestCase):
    def test_angka_polindrom(self):
        hasil = bilangan.angka_polindrom(909)
        hasil_1 = bilangan.angka_polindrom(505)
        self.assertEqual(hasil, "angka polindrom".capitalize())
        self.assertEqual(hasil_1, "angka polindrom".capitalize())

    def test_salah_angka_polindorm(self):
        hasil = bilangan.angka_polindrom(123)
        hasil_1 = bilangan.angka_polindrom(756)
        self.assertEqual(hasil, "bukan angka polindrom".capitalize())
        self.assertEqual(hasil_1, "bukan angka polindrom".capitalize())

    def tes_angka_negatif_polindrom(self):
        hasil = bilangan.angka_polindrom(-909)
        with self.assertRaises(error.Error):
            raise hasil

    def tipe_data_angka_polindrom(self):
        hasil = bilangan.angka_polindrom("909")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestAngkaPrima(unittest.TestCase):
    def test_angka_prima(self):
        hasil1 = bilangan.angka_prima(11)
        hasil2 = bilangan.angka_prima(41)
        self.assertEqual(hasil1, "angka prima".capitalize())
        self.assertEqual(hasil2, "angka prima".capitalize())

    def test_bukan_angka_prima(self):
        self.assertEqual(bilangan.angka_prima(25), "bukan angka prima".capitalize())
        self.assertEqual(bilangan.angka_prima(49), "bukan angka prima".capitalize())

    def test_angka_prima_negatif(self):
        hasil = bilangan.angka_prima(-7)
        with self.assertRaises(error.Error):
            raise hasil

    def test_tipe_data(self):
        hasil = bilangan.angka_prima("5")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class angka_kaprekar(unittest.TestCase):
    def test_angka_kaprekar(self):
        self.assertAlmostEqual(
            bilangan.angka_kaprekar(45), "angka kaprekar".capitalize()
        )
        self.assertAlmostEqual(
            bilangan.angka_kaprekar(55), "angka kaprekar".capitalize()
        )

    def tets_bukan_angka_kaprekar(self):
        self.assertAlmostEqual(
            bilangan.angka_kaprekar(12), "bukan angka kaprekar".capitalize()
        )
        self.assertAlmostEqual(
            bilangan.angka_kaprekar(35), "bukan angka kaprekar".capitalize()
        )

    def tets_angka_negatif(self):
        hasil = bilangan.angka_kaprekar(-81)
        with self.assertRaises(error.Error):
            raise hasil

    def test_tipe_data(self):
        hasil = bilangan.angka_kaprekar("81")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class angka_tetrahendral(unittest.TestCase):
    def test_angka_tetrahedral(self):
        self.assertAlmostEqual(bilangan.angka_tetrahedral(8), 120)
        self.assertAlmostEqual(bilangan.angka_tetrahedral(5), 35)

    def test_angka_negatif(self):
        hasil = bilangan.angka_tetrahedral(-10)
        with self.assertRaises(error.Error):
            raise hasil

    def tipe_data_salah(self):
        hasil = bilangan.angka_tetrahedral("10")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class angka_pentatope(unittest.TestCase):
    def test_angka_pentatope(self):
        self.assertAlmostEqual(bilangan.angka_pentatope(9), 495)
        self.assertAlmostEqual(bilangan.angka_pentatope(7), 210)

    def test_angka_negatif_pentatope(self):
        hasil = bilangan.angka_pentatope(-19)
        with self.assertRaises(error.Error):
            raise hasil

    def tets_tipe_data(self):
        hasil = bilangan.angka_pentatope("9")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil
