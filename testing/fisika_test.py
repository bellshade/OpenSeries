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


class TestKecepatanSudut(unittest.TestCase):
    def test_kecepatan_sudut_valid(self):
        hasil = fisika.kecepatan_sudut(30, 2)
        self.assertEqual(hasil, 15)

    def test_kecepatan_sudut_dibagi_nol(self):
        hasil = fisika.kecepatan_sudut(30.0, 0)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_kecepatan_sudut_tidak_valid(self):
        hasil = fisika.kecepatan_sudut("30.0", 2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestPercepatanSudut(unittest.TestCase):
    def test_percepatan_sudut_valid(self):
        hasil = fisika.percepatan_sudut(50, 2)
        self.assertEqual(hasil, 25)

    def test_percepatan_sudut_dibagi_nol(self):
        hasil = fisika.percepatan_sudut(50.0, 0)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_percepatan_sudut_tidak_valid(self):
        hasil = fisika.percepatan_sudut("50.0", 2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestPercepatanSentripetallinear(unittest.TestCase):
    def test_percepatanSentripetal_linear_valid(self):
        hasil = fisika.percepatan_sentripetal_linear(5.0, 2)
        self.assertEqual(hasil, 12.5)

    def test_percepatan_sudut_dibagi_nol(self):
        hasil = fisika.percepatan_sudut(50.0, 0)
        with self.assertRaises(error.ErrorDibagiNol):
            raise hasil

    def test_percepatan_sudut_tidak_valid(self):
        hasil = fisika.percepatan_sudut("50.0", 2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestPercepatanSentripetalSudut(unittest.TestCase):
    def test_percepatansentripetal_sudut_valid(self):
        hasil = fisika.percepatan_sentripetal_sudut(5, 8)
        self.assertEqual(hasil, 320)

    def test_percepatan_sudut_tidak_valid(self):
        hasil = fisika.percepatan_sentripetal_sudut("5", 8)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestGerakLurusBeraturan(unittest.TestCase):
    def test_valid(self):
        hasil = fisika.gerak_lurus_beraturan(10.0, 2.0, 3.0)
        self.assertAlmostEqual(hasil, 39.0)

    def test_invalid_int(self):
        hasil = fisika.gerak_lurus_beraturan(8, 1.5, 2)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TesGerakMelingkarBeraturan(unittest.TestCase):
    def test_valid(self):
        hasil = fisika.gerak_melingkar_beraturan(5, 6, 3)
        self.assertAlmostEqual(hasil, 23)

    def test_invalid(self):
        hasil = fisika.gerak_melingkar_beraturan("5", "6", 3)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestInersia(unittest.TestCase):
    def test_valid(self):
        hasil = fisika.inersia(2, 4)
        self.assertAlmostEqual(hasil, 32)

    def test_invalid(self):
        hasil = fisika.inersia("2", 4)
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


class TestEnergiKinetikRotasi(unittest.TestCase):
    def test_valid(self):
        hasil = fisika.energi_kinetik_rotasi(2, 6)
        self.assertAlmostEqual(hasil, 36)

    def test_invalid(self):
        hasil = fisika.energi_kinetik_rotasi("2", 6)
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


class TestCelciusFarenheit(unittest.TestCase):
    def test_CelciusFarenheit(self):
        hasil = fisika.celcius_farenheit(0)
        rounding_hasil = round(hasil)
        self.assertEqual(rounding_hasil, 32)

    def test_CelciusFarenheit_invalid_tipe_data(self):
        hasil = fisika.celcius_farenheit("0")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestFarenheitCelcius(unittest.TestCase):
    def test_FarenheitCelcius(self):
        hasil = fisika.farenheit_celcius(32)
        rounding_hasil = round(hasil)
        self.assertEqual(rounding_hasil, 0)

    def test_FarenheitCelcius_invalid_tipe_data(self):
        hasil = fisika.farenheit_celcius("32")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestCelciusReamur(unittest.TestCase):
    def test_CelciusReamur(self):
        hasil = fisika.celcius_reaumur(32)
        self.assertEqual(hasil, 25.6)

    def test_CelciusReamur_invalid_tipe_data(self):
        hasil = fisika.farenheit_celcius("32")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestReamurCelcius(unittest.TestCase):
    def test_ReamurCelcius(self):
        hasil = fisika.reamur_celcius(32)
        self.assertEqual(hasil, 40)

    def test_ReamurCelcius_invalid_tipe_data(self):
        hasil = fisika.farenheit_celcius("32")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestCelciusKelvin(unittest.TestCase):
    def test_CelciusKelvin(self):
        hasil = fisika.celcius_kelvin(0)
        self.assertEqual(hasil, 273.15)

    def test_CelciusKelvin_invalid_tipe_data(self):
        hasil = fisika.farenheit_celcius("0")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKelvinCelcius(unittest.TestCase):
    def test_KelvinCelcius(self):
        hasil = fisika.kelvin_celcius(273.15)
        self.assertEqual(hasil, 0)

    def test_kelvin_nilai_negatif(self):
        hasil = fisika.kelvin_celcius(-10)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil

    def test_KelvinCelcius_invalid_tipe_data(self):
        hasil = fisika.kelvin_celcius("273.15")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKelvinFarenheit(unittest.TestCase):
    def test_KelvinFarenheit(self):
        hasil = fisika.kelvin_fahrenheit(300)
        self.assertEqual(hasil, 80.32999999999998)

    def test_kelvin_nilai_negatif(self):
        hasil = fisika.kelvin_fahrenheit(-10)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil

    def test_KelvinFarenheit_invalid_tipe_data(self):
        hasil = fisika.kelvin_fahrenheit("0")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestFarenheitKelvin(unittest.TestCase):
    def test_FarenheitKelvin(self):
        hasil = fisika.fahrenheit_kelvin(-459.67)
        self.assertEqual(hasil, 0)

    def test_FarenheitKelvin_invalid_tipe_data(self):
        hasil = fisika.fahrenheit_kelvin("-459.67")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKelvinReamur(unittest.TestCase):
    def test_KelvinReamur(self):
        hasil = fisika.kelvin_reamur(300)
        self.assertEqual(hasil, 21.480000000000018)

    def test_kelvin_nilai_negatif(self):
        hasil = fisika.kelvin_reamur(-10)
        self.assertIsInstance(hasil, error.Error)
        with self.assertRaises(error.Error):
            raise hasil

    def test_KelvinReamur_invalid_tipe_data(self):
        hasil = fisika.kelvin_reamur("300")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestReamurKelvin(unittest.TestCase):
    def test_ReamurKelvin(self):
        hasil = fisika.reamur_kelvin(0)
        self.assertEqual(hasil, 273.15)

    def test_ReamurFahrenheit_invalid_tipe_data(self):
        hasil = fisika.reamur_fahrenheit("-218.52")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestReamurFahrenheit(unittest.TestCase):
    def test_ReamurFahrenheit(self):
        hasil = fisika.reamur_fahrenheit(0)
        self.assertEqual(hasil, 32)

    def test_ReamurFahrenheit_invalid_tipe_data(self):
        hasil = fisika.reamur_fahrenheit("0")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestFahrenheitReamur(unittest.TestCase):
    def test_FahrenheitReamur(self):
        hasil = fisika.fahrenheit_reamur(40)
        self.assertEqual(hasil, 3.5555555555555554)

    def test_FahrenheitReamur_invalid_tipe_data(self):
        hasil = fisika.fahrenheit_reamur("0")
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil
