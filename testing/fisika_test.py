import unittest
from OpenSeries import fisika as fisika
from OpenSeries.util import error as error


class TestKecepatan(unittest.TestCase):
    def test_angka_valid(self):
        hasil = fisika.kecepatan(100.0, 10.0)
        self.assertEqual(hasil, 10.0)

    def test_dibagi_nol(self):
        hasil = fisika.kecepatan(150.0, 0)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_invalid_input(self):
        with self.assertRaises(error.ErrorTipeData):
            raise fisika.kecepatan("12", 30)

    def test_kecepatan_invalid_input2(self):
        hasil = fisika.kecepatan("12", "50")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestPercepatan(unittest.TestCase):
    def test_percepatan_valid(self):
        hasil = fisika.percepatan(20.0, 5.0)
        self.assertEqual(hasil, 4.0)

    def test_percepatan_dibagi_nol(self):
        hasil = fisika.percepatan(30.0, 0)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_percepatan_nilai_tidak_valid(self):
        hasil = fisika.percepatan("20", 30)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestGerakLurusBeraturan(unittest.TestCase):
    def test_valid(self):
        hasil = fisika.gerak_lurus_beraturan(10.0, 2.0, 3.0)
        self.assertAlmostEqual(hasil, 39.0, places=2)

    def test_invalid_int(self):
        hasil = fisika.gerak_lurus_beraturan(8, 1.5, 2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestEnergiKinetik(unittest.TestCase):
    def test_valid_input(self):
        hasil = fisika.energi_kinetik(2.0, 5.0)
        self.assertAlmostEqual(hasil, 25.0)

    def test_invalid_input_mix_tipe_data(self):
        hasil = fisika.energi_kinetik("3", 4.5)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKetinggianBarometrik(unittest.TestCase):
    def test_valid_input_tekanan(self):
        hasil = fisika.ketinggian_barometrik(101325.0)
        self.assertIsInstance(hasil, float)

    def test_tekanan_lebih_besar_daripada_air(self):
        hasil = fisika.ketinggian_barometrik(110000.0)
        with self.assertRaises(error.Error):
            raise hasil

    def test_tekanan_angka_negatif(self):
        hasil = fisika.ketinggian_barometrik(-820.3)
        with self.assertRaises(error.Error):
            raise hasil

    def test_tekanan_tipe_data_salah(self):
        hasil = fisika.ketinggian_barometrik("12")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestGayaSentripental(unittest.TestCase):
    def test_gaya_sentripental(self):
        hasil = fisika.gaya_sentripental(10, 5, 2)
        self.assertEqual(hasil, 125.0)

    def test_gaya_sentripental_error_tipe_data(self):
        hasil = fisika.gaya_sentripental("12", 5, 2)
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_gaya_sentripental_minus(self):
        hasil = fisika.gaya_sentripental(-10, 5, 2)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil

    def test_gaya_sentripental_nol(self):
        hasil = fisika.gaya_sentripental(10, 5, 0)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil


class TestEfekDoppler(unittest.TestCase):
    def test_efek_doppler(self):
        hasil = fisika.efek_doppler(100, 340, 20, 10)
        rounding_hasil = round(hasil)
        self.assertEqual(rounding_hasil, 109)

    def test_efek_doppler_invalid_tipe_data(self):
        hasil = fisika.efek_doppler("12", "340", "20", 10)
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_efek_doppler_dibagi_nol(self):
        hasil = fisika.efek_doppler(0, 0, 0, 0)
        self.assertIsInstance(hasil, error.ErrorDibagiNol)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_efek_doppler_nilai_negatif(self):
        hasil = fisika.efek_doppler(-100, -340, 20, 10)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil


class Testjumlah_partikel(unittest.TestCase):
    def test_jumlah_partikel(self):
        hasil = fisika.jumlah_partikel(15)
        rounding_hasil = hasil
        self.assertEqual(rounding_hasil, 9032999999999999536529408)

    def test_jumlah_partikel_invalid_tipe_data(self):
        hasil = fisika.jumlah_partikel("15")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_jumlah_partikel_negatif(self):
        hasil = fisika.jumlah_partikel(-15)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil


class Testjumlah_mol(unittest.TestCase):
    def test_jumlah_mol(self):
        hasil = fisika.jumlah_mol(25, 5)
        rounding_hasil = hasil
        self.assertEqual(rounding_hasil, 5)

    def test_jumlah_mol_invalid_tipe_data(self):
        hasil = fisika.jumlah_mol("25", 5)
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_jumlah_mol_dibaginol(self):
        hasil = fisika.jumlah_mol(25, 0)
        self.assertIsInstance(hasil, error.ErrorDibagiNol)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_jumlah_mol_invalid_negatif(self):
        hasil = fisika.jumlah_mol(-25, 5)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil


class Testmassa_atom(unittest.TestCase):
    def test_massa_atom(self):
        hasil = fisika.massa_atom(17 * pow(10, 23))
        rounding_hasil = hasil
        self.assertEqual(rounding_hasil, 2.8229823978744606)

    def test_jumlah_massa_atom_tipe_data(self):
        hasil = fisika.massa_atom("17")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_jumlah_massa_invalid_negatif(self):
        hasil = fisika.massa_atom(-17)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil
