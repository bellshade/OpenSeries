import unittest
from OpenSeries import matematika as matematika
from OpenSeries.util import error as error
import numpy as np


class TestKonversi(unittest.TestCase):
    def test_radian_ke_derajat(self):
        self.assertAlmostEqual(matematika.radian_ke_derajat(1), 57.2957795131)
        self.assertAlmostEqual(matematika.radian_ke_derajat(0), 0)
        with self.assertRaises(error.ErrorTipeData):
            raise matematika.radian_ke_derajat("12")

    def test_derajat_ke_radian(self):
        self.assertAlmostEqual(matematika.derajat_ke_radian(180), 3.1415926535)
        self.assertAlmostEqual(matematika.derajat_ke_radian(0), 0)
        with self.assertRaises(error.ErrorTipeData):
            raise matematika.derajat_ke_radian("12")

    def test_radian_ke_gradian(self):
        self.assertAlmostEqual(matematika.radian_ke_gradian(180), 11459.1559026)
        with self.assertRaises(error.ErrorTipeData):
            raise matematika.radian_ke_gradian("128")

    def test_gradian_ke_radian(self):
        self.assertAlmostEqual(matematika.gradian_ke_radian(52), 0.8168140899)
        with self.assertRaises(error.ErrorTipeData):
            raise matematika.gradian_ke_radian("200")


class TestKelilingLingkaran(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.keliling_lingkaran(2.5)
        self.assertEqual(hasil, 15.707963267948966)

    def test_tipe_data_int(self):
        hasil = matematika.keliling_lingkaran(3)
        self.assertAlmostEqual(hasil, 18.84955592153876)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.keliling_lingkaran("45")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestLuasPersegi(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.luas_persegi(2.5)
        self.assertEqual(hasil, 6.25)

    def test_tipe_data_int(self):
        hasil = matematika.luas_persegi(5)
        self.assertEqual(hasil, 25)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.luas_persegi("5")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestLuasPersegiPanjang(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.luas_persegi_panjang(5.6, 3)
        self.assertEqual(hasil, 16.799999999999997)

    def test_tipe_data_int(self):
        hasil = matematika.luas_persegi_panjang(5, 3)
        self.assertEqual(hasil, 15)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.luas_persegi_panjang("6", "9")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKelilingPersegiPanjang(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.keliling_persegi_panjang(4.3, 5)
        self.assertEqual(hasil, 18.6)

    def test_tipe_data_int(self):
        hasil = matematika.keliling_persegi_panjang(5, 3)
        self.assertEqual(hasil, 16)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.keliling_persegi_panjang("8", "10")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestLuasELips(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.luas_elips(2.3, 7)
        self.assertEqual(hasil, 50.579641722795664)

    def test_tipe_data_int(self):
        hasil = matematika.luas_elips(10, 4)
        self.assertEqual(hasil, 125.66370614359172)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.luas_elips("7", "14")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestLuasTrapesium(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.luas_trapesium(2.6, 4.2, 2.1)
        self.assertEqual(hasil, 7.1400000000000015)

    def test_tipe_data_int(self):
        hasil = matematika.luas_trapesium(6, 2, 3)
        self.assertEqual(hasil, 12)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.luas_trapesium("7", "3", "8")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKelilingSegitiga(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.keliling_segitiga(4.1, 5.3, 2.8)
        self.assertEqual(hasil, 12.2)

    def test_tipe_data_int(self):
        hasil = matematika.keliling_segitiga(5, 2, 3)
        self.assertEqual(hasil, 10)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.keliling_segitiga("10", "7.1", "2.8")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestLuasJajargenjang(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.luas_jajargenjang(3.1, 5)
        self.assertEqual(hasil, 15.5)

    def test_tipe_data_int(self):
        hasil = matematika.luas_jajargenjang(2, 7)
        self.assertEqual(hasil, 14)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.luas_jajargenjang(4, "9")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKelilingJajargenjang(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.keliling_jajargenjang(4.5, 2.1)
        self.assertEqual(hasil, 13.2)

    def test_tipe_data_int(self):
        hasil = matematika.keliling_jajargenjang(9, 3)
        self.assertEqual(hasil, 24)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.keliling_jajargenjang("4.3", "10")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestVolumeKubus(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.volume_kubus(4.5)
        self.assertEqual(hasil, 91.125)

    def test_tipe_data_int(self):
        hasil = matematika.volume_kubus(9)
        self.assertEqual(hasil, 729)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.volume_kubus("10")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestVolumeBalok(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.volume_balok(4.3, 5.2, 1.2)
        self.assertEqual(hasil, 26.831999999999997)

    def test_tipe_data_int(self):
        hasil = matematika.volume_balok(5, 4, 3)
        self.assertEqual(hasil, 60)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.volume_balok(7.2, "2", 12)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestVolumeSilinder(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.volume_silinder(1.2, 4.3)
        self.assertEqual(hasil, 19.452741711028)

    def test_tipe_data_int(self):
        hasil = matematika.volume_silinder(10, 2)
        self.assertEqual(hasil, 628.3185307179587)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.volume_silinder(7.8, "2")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestVolumeElipsoid(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.volume_elipsoid(4.5, 3.2, 2.1)
        self.assertEqual(hasil, 126.66901579274047)

    def test_tipe_data_int(self):
        hasil = matematika.volume_elipsoid(10, 5, 3)
        self.assertEqual(hasil, 628.3185307179585)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.volume_elipsoid(7.2, "2", "2.5")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestVolumeKerucut(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.volume_kerucut(10, 12)
        self.assertEqual(hasil, 1256.637061435917)

    def test_tipe_data_int(self):
        hasil = matematika.volume_kerucut(1.1, 2.5)
        self.assertEqual(hasil, 3.167772592369708)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.volume_kerucut(3, "9")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestVolumeBola(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.volume_bola(3.2)
        self.assertEqual(hasil, 137.25827743044047)

    def test_tipe_data_int(self):
        hasil = matematika.volume_bola(4)
        self.assertEqual(hasil, 268.082573106329)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.volume_bola("4.1")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestPermukaanBola(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.permukaan_bola(2.3)
        self.assertEqual(hasil, 66.47610054996001)

    def test_tipe_data_int(self):
        hasil = matematika.permukaan_bola(8)
        self.assertEqual(hasil, 804.247719318987)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.permukaan_bola("6.3")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestDiameterLingkaran(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.diameter_lingkaran(2.5)
        self.assertAlmostEqual(hasil, 5.0)

    def test_tipe_data_int(self):
        hasil = matematika.diameter_lingkaran(3)
        self.assertAlmostEqual(hasil, 6.0)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.diameter_lingkaran("800")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestPersamaanKuadrat(unittest.TestCase):
    def test_nilai_valid(self):
        hasil = matematika.persamaan_kuadrat(1, -3, 2)
        self.assertAlmostEqual(hasil, 2.0)

    def test_nilai_valid_float(self):
        hasil = matematika.persamaan_kuadrat(1.0, -2.0, 1.0)
        self.assertAlmostEqual(hasil, 1.0)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.persamaan_kuadrat("12", 2, 3)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_complex(self):
        hasil = matematika.persamaan_kuadrat(1, 2, 5)
        with self.assertRaises(error.Error):
            raise hasil


class TestRataRata(unittest.TestCase):
    def test_nilai_valid(self):
        hasil = matematika.rata_rata([1, 2, 3, 4, 5])
        self.assertAlmostEqual(hasil, 3.0)

    def test_nilai_valid_float(self):
        hasil = matematika.rata_rata([1.5, 2.5, 3.5, 4.5])
        self.assertAlmostEqual(hasil, 3.0)

    def test_list_kosong(self):
        hasil = matematika.rata_rata([])
        with self.assertRaises(error.Error):
            raise hasil


class TestFaktorial(unittest.TestCase):
    def test_faktorial_nilai_nol(self):
        hasil = matematika.faktorial(0)
        self.assertEqual(hasil, 1)

    def test_faktorial_tipe_data_salah(self):
        hasil = matematika.faktorial(20.0)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_faktorial_nilai_negatif(self):
        hasil = matematika.faktorial(-120)
        with self.assertRaises(error.Error):
            raise hasil


class TestPermutasi(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.permutasi(5, 2)
        self.assertEqual(hasil, 20)

    def test_input_invalid_float(self):
        hasil = matematika.permutasi(5.2, 2.0)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.permutasi("12", "14")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestKombinasi(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.kombinasi(5, 2)
        self.assertEqual(hasil, 10)

    def test_input_invalid_float(self):
        hasil = matematika.kombinasi(5.2, 2.0)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.kombinasi("12", "14")
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestFPB(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.fpb(36, 48)
        self.assertEqual(hasil, 12)

    def test_invalid_input(self):
        hasil = matematika.fpb(15.0, 20.0)
        self.assertEqual(hasil, 5.0)

    def test_angka_invalid(self):
        hasil = matematika.fpb(-36, -40)
        with self.assertRaises(error.Error):
            raise hasil

    def test_angka_nol(self):
        hasil = matematika.fpb(0, 48)
        self.assertEqual(hasil, 48)


class TestFaktorPrima(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.faktor_prima(30)
        self.assertEqual(hasil, [2, 3, 5])

    def test_input_float(self):
        hasil = matematika.faktor_prima(25.0)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_faktor_prima_kosong(self):
        hasil = matematika.faktor_prima(1)
        self.assertEqual(hasil, [])

    def test_input_negatif(self):
        hasil = matematika.faktor_prima(-30)
        with self.assertRaises(error.Error):
            raise hasil


class TestMatriksTranspose(unittest.TestCase):
    def test_valid_input(self):
        matriks_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ekspetasi = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        hasil = matematika.transpose_matriks(matriks_a)
        self.assertEqual(hasil, ekspetasi)


class TestFungsiEuler(unittest.TestCase):
    def test_nilai_positif(self):
        hasil = matematika.euler_pi(100)
        self.assertEqual(hasil, 40.0)

    def test_nilai_tidak_integer(self):
        hasil = matematika.euler_pi(3.14)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_negatif(self):
        hasil = matematika.euler_pi(-20)
        with self.assertRaises(error.Error):
            raise hasil

    def test_nilai_nol(self):
        hasil = matematika.euler_pi(0)
        with self.assertRaises(error.Error):
            raise hasil


class TestSigmoid(unittest.TestCase):
    def test_sigmoid(self):
        input_nilai_array = np.array([1, 2, 3])
        hasil = matematika.sigmoid(input_nilai_array)
        nilai_ekspetasi = np.array([0.73105858, 0.88079708, 0.95257413])
        np.testing.assert_allclose(hasil, nilai_ekspetasi, rtol=1e-7)

    def test_invalid_input(self):
        hasil = matematika.sigmoid(5)
        self.assertIsInstance(hasil, error.ErrorTipeData)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestDistribusiBinomial(unittest.TestCase):
    def test_valid_input(self):
        hasil = matematika.distribusi_binomial(2, 5, 0.7)
        self.assertAlmostEqual(hasil, 0.13230000000000006)

    def test_invalid_input_keberhasilan_lebih_besar_percobaan(self):
        hasil = matematika.distribusi_binomial(5, 3, 0.5)
        with self.assertRaises(error.ErrorValue):
            raise hasil

    def test_invalid_input_negatif(self):
        hasil = matematika.distribusi_binomial(-2, 4, 0.1)
        with self.assertRaises(error.ErrorValue):
            raise hasil

    def test_input_angka_tidak_integer(self):
        hasil = matematika.distribusi_binomial(2.4, 4.2, 0.5)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestGaussian(unittest.TestCase):
    def test_data_valid_input(self):
        x = 5
        mu = 3
        sigma = 2
        ekspetasi_nilai = 0.12098536225957168
        hasil = matematika.gaussian(x, mu, sigma)
        self.assertAlmostEqual(hasil, ekspetasi_nilai, places=10)


class TestIntegral(unittest.TestCase):
    def test_nilai_integral(self):
        def f(x):
            return x * x

        a = 0
        b = 3
        hasil = matematika.integral(f, a, b)

        self.assertAlmostEqual(hasil, 9.00, places=2)

    def testing_tipe_input_data_string(self):
        def f(x):
            return x * x

        a = "0"
        b = "3"
        hasil = matematika.integral(f, a, b)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def testing_tipe_iterasi_string(self):
        def f(x):
            return x * x

        a = 0
        b = 3
        iterasi = "4"
        hasil = matematika.integral(a, b, iterasi)
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestDerivative(unittest.TestCase):
    def setUp(self):
        def f(x):
            return x * x

        self.inputFungsi = f
        self.inputValue = 4

    def testing_input_value_integer(self):
        hasil = matematika.turunan(self.inputFungsi, self.inputValue)
        self.assertAlmostEqual(hasil, 8.000, places=3)

    def testing_input_value_desimal(self):
        hasil = matematika.turunan(self.inputFungsi, float(self.inputValue))
        self.assertAlmostEqual(hasil, 8.000, places=3)

    def testing_input_value_string(self):
        hasil = matematika.turunan(self.inputFungsi, str(self.inputValue))
        with self.assertRaises(error.ErrorTipeData):
            raise hasil


class TestMeanAbsolutDerivative(unittest.TestCase):
    def test_data_kosong(self):
        hasil = matematika.mean_absolut_deviasi([])
        with self.assertRaises(error.Error):
            raise hasil

    def test_data_string(self):
        hasil = matematika.mean_absolut_deviasi([2, "2"])
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_float(self):
        hasil = matematika.mean_absolut_deviasi([2, 2.3])
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_str_float(self):
        hasil = matematika.mean_absolut_deviasi([2, "3", 3.3])
        with self.assertRaises(error.ErrorTipeData):
            raise hasil

    def test_nilai_integer(self):
        hasil = matematika.mean_absolut_deviasi([100, 200])
        self.assertAlmostEqual(hasil, 50.0)

    def test_nilai_rentang(self):
        hasil = matematika.mean_absolut_deviasi([1, 2, 3, 4, 5])
        self.assertAlmostEqual(hasil, 1.2)

    def test_ekspetasi_nilai_return(self):
        hasil = matematika.mean_absolut_deviasi([100, 200])
        self.assertIsInstance(hasil, float)
