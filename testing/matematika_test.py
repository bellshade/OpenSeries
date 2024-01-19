import unittest
from OpenSeries import matematika as matematika
from OpenSeries.util import error as error


class TestKonversi(unittest.TestCase):
    def test_radian_ke_derajat(self):
        self.assertAlmostEqual(matematika.radian_ke_derajat(1), 57.2957795131)
        self.assertAlmostEqual(matematika.radian_ke_derajat(0), 0)
        self.assertEqual(
            matematika.radian_ke_derajat("12"), error.error_tipe_data(["float", "int"])
        )

    def test_derajat_ke_radian(self):
        self.assertAlmostEqual(matematika.derajat_ke_radian(180), 3.1415926535)
        self.assertAlmostEqual(matematika.derajat_ke_radian(0), 0)
        self.assertEqual(
            matematika.derajat_ke_radian("15"), error.error_tipe_data(["float", "int"])
        )

    def test_radian_ke_gradian(self):
        self.assertAlmostEqual(matematika.radian_ke_gradian(180), 11459.1559026)
        self.assertEqual(
            matematika.radian_ke_gradian("128"), error.error_tipe_data(["float", "int"])
        )

    def test_gradian_ke_radian(self):
        self.assertAlmostEqual(matematika.gradian_ke_radian(52), 0.8168140899)
        self.assertEqual(
            matematika.gradian_ke_radian("200"), error.error_tipe_data(["float", "int"])
        )


class TestKelilingLingkaran(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.keliling_lingkaran(2.5)
        self.assertEqual(hasil, 15.707963267948966)

    def test_tipe_data_int(self):
        hasil = matematika.keliling_lingkaran(3)
        self.assertAlmostEqual(hasil, 18.84955592153876)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.keliling_lingkaran("45")
        self.assertEqual(hasil, error.error_tipe_data(["float", "int"]))


class TestDiameterLingkaran(unittest.TestCase):
    def test_tipe_data_float(self):
        hasil = matematika.diameter_lingkaran(2.5)
        self.assertAlmostEqual(hasil, 5.0)

    def test_tipe_data_int(self):
        hasil = matematika.diameter_lingkaran(3)
        self.assertAlmostEqual(hasil, 6.0)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.diameter_lingkaran("800")
        self.assertEqual(hasil, error.error_tipe_data(["float", "int"]))


class TestPersamaanKuadrat(unittest.TestCase):
    def test_nilai_valid(self):
        hasil = matematika.persamaan_kuadrat(1, -3, 2)
        self.assertAlmostEqual(hasil, 2.0)

    def test_nilai_valid_float(self):
        hasil = matematika.persamaan_kuadrat(1.0, -2.0, 1.0)
        self.assertAlmostEqual(hasil, 1.0)

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.persamaan_kuadrat("12", 2, 3)
        self.assertEqual(hasil, error.error_tipe_data(["float", "int"]))

    def test_nilai_complex(self):
        hasil = matematika.persamaan_kuadrat(1, 2, 5)
        self.assertEqual(hasil, error.error_format("Persamaan memiliki solusi complex"))


class TestRataRata(unittest.TestCase):
    def test_nilai_valid(self):
        hasil = matematika.rata_rata([1, 2, 3, 4, 5])
        self.assertAlmostEqual(hasil, 3.0)

    def test_nilai_valid_float(self):
        hasil = matematika.rata_rata([1.5, 2.5, 3.5, 4.5])
        self.assertAlmostEqual(hasil, 3.0)

    def test_list_kosong(self):
        hasil = matematika.rata_rata([])
        self.assertEqual(hasil, error.error_format("List tidak boleh kosong"))


class TestFaktorial(unittest.TestCase):
    def test_faktorial_nilai_nol(self):
        hasil = matematika.faktorial(0)
        self.assertEqual(hasil, 1)

    def test_faktorial_nilai_int(self):
        hasil = matematika.faktorial(5)
        self.assertEqual(hasil, 120)

    def test_faktorial_nilai_float(self):
        hasil = matematika.faktorial(2.5)
        self.assertEqual(hasil, error.error_tipe_data(["int"]))

    def test_faktorial_nilai_negatif(self):
        hasil = matematika.faktorial(-20)
        self.assertEqual(
            hasil, error.error_format("Tidak bisa menggunakan angka negatif")
        )


class TestPermutasi(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.permutasi(5, 2)
        self.assertEqual(hasil, 20)

    def test_input_invalid_float(self):
        hasil = matematika.permutasi(5.2, 2.0)
        self.assertEqual(hasil, error.error_tipe_data(["int"]))

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.permutasi("12", "14")
        self.assertEqual(hasil, error.error_tipe_data(["int"]))


class TestKombinasi(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.kombinasi(5, 2)
        self.assertEqual(hasil, 10)

    def test_input_invalid_float(self):
        hasil = matematika.kombinasi(5.2, 2.0)
        self.assertEqual(hasil, error.error_tipe_data(["int"]))

    def test_nilai_input_tidak_valid(self):
        hasil = matematika.kombinasi("12", "14")
        self.assertEqual(hasil, error.error_tipe_data(["int"]))


class TestFPB(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.fpb(36, 48)
        self.assertEqual(hasil, 12)

    def test_invalid_input(self):
        hasil = matematika.fpb(15.0, 20.0)
        self.assertEqual(hasil, 5.0)

    def test_angka_invalid(self):
        hasil = matematika.fpb(-36, -40)
        self.assertEqual(hasil, error.error_format("Angka tidak boleh negatif"))

    def test_angka_nol(self):
        hasil = matematika.fpb(0, 48)
        self.assertEqual(hasil, 48)


class TestFaktorPrima(unittest.TestCase):
    def test_input_valid(self):
        hasil = matematika.faktor_prima(30)
        self.assertEqual(hasil, [2, 3, 5])

    def test_input_float(self):
        hasil = matematika.faktor_prima(25.0)
        self.assertEqual(hasil, [5, 5])

    def test_faktor_prima_kosong(self):
        hasil = matematika.faktor_prima(1)
        self.assertEqual(hasil, [])

    def test_input_negatif(self):
        hasil = matematika.faktor_prima(-30)
        self.assertEqual(hasil, error.error_format("Angka tidak boleh negatif"))


class TestMatriksTranspose(unittest.TestCase):
    def test_valid_input(self):
        matriks_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ekspetasi = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        hasil = matematika.transpose_matriks(matriks_a)
        self.assertEqual(hasil, ekspetasi)
