import unittest
from OpenSeries import fisika as fisika
from OpenSeries.util import error as error


class TestKecepatan(unittest.TestCase):
    def test_angka_valid(self):
        hasil = fisika.kecepatan(100.0, 10.0)
        self.assertEqual(hasil, 10.0)

    def test_dibagi_nol(self):
        hasil = fisika.kecepatan(150.0, 0)
        self.assertEqual(hasil, error.error_dibagi_nol())

    def test_invalid_input(self):
        hasil = fisika.kecepatan("12", 5.0)
        self.assertIsInstance(hasil, str)
        self.assertIn(error.error_tipe_data(["int", "float"]), hasil)

    def test_kecepatan_invalid_input2(self):
        hasil = fisika.kecepatan("12", "50")
        self.assertIsInstance(hasil, str)
        self.assertIn(error.error_tipe_data(["int", "float"]), hasil)


class TestPercepatan(unittest.TestCase):
    def test_percepatan_valid(self):
        hasil = fisika.percepatan(20.0, 5.0)
        self.assertEqual(hasil, 4.0)

    def test_percepatan_dibagi_nol(self):
        hasil = fisika.percepatan(30.0, 0)
        self.assertEqual(error.error_dibagi_nol(), hasil)

    def test_percepatan_nilai_tidak_valid(self):
        hasil = fisika.percepatan("20", 30)
        self.assertIsInstance(hasil, str)
        self.assertIn(error.error_tipe_data(["int", "float"]), hasil)


class TestGerakLurusBeraturan(unittest.TestCase):
    def test_valid(self):
        hasil = fisika.gerak_lurus_beraturan(10.0, 2.0, 3.0)
        self.assertAlmostEqual(hasil, 39.0, places=2)

    def test_invalid_int(self):
        hasil = fisika.gerak_lurus_beraturan(8, 1.5, 2)
        self.assertEqual(hasil, error.error_tipe_data(["float"]))


class TestEnergiKinetik(unittest.TestCase):
    def test_valid_input(self):
        hasil = fisika.energi_kinetik(2.0, 5.0)
        self.assertAlmostEqual(hasil, 25.0)

    def test_invalid_input_mix_tipe_data(self):
        hasil = fisika.energi_kinetik("3", 4.5)
        self.assertEqual(hasil, error.error_tipe_data(["int", "float"]))


class TestKetinggianBarometrik(unittest.TestCase):
    def test_valid_input_tekanan(self):
        hasil = fisika.ketinggian_barometrik(101325.0)
        self.assertIsInstance(hasil, float)

    def test_tekanan_lebih_besar_daripada_air(self):
        hasil = fisika.ketinggian_barometrik(110000.0)
        self.assertEqual(
            hasil,
            error.error_format("nilai lebih tinggi dari tekanan di permukaan laut"),
        )

    def test_tekanan_angka_negatif(self):
        hasil = fisika.ketinggian_barometrik(-820.3)
        self.assertEqual(
            hasil, error.error_format("tekanan atmosfir tidak bisa negatif")
        )

    def test_tekanan_tipe_data_salah(self):
        hasil = fisika.ketinggian_barometrik("12")
        self.assertEqual(hasil, error.error_tipe_data(["float"]))
