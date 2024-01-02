from OpenSeries.util import constant
from OpenSeries.util import error as pesan_error
import math


def radian_ke_derajat(radian: float | int) -> float | str:
    """
    mengubah nilai radian ke derajat

    parameter:
        radian (float atau integer): nilai radian
    """
    if not isinstance(radian, (float, int)):
        return pesan_error.error_tipe_data()
    else:
        return radian * (180 / constant.pi)


def luas_lingkaran(jari: float | int) -> float:
    """
    menghitung luas lingkaran

    Parameter:
    jari-jari (float atau integer): jari jari yang akan dihitung
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jari, (float, int)):
        return constant.pi * jari**2
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def keliling_lingkaran(jari: float | int) -> float:
    """
    menghitung keliling lingkaran

    parameter:
        jari (float atau integer): jari-jari lingkaran
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jari, (float, int)):
        return 2 * constant.pi * jari
    else:
        return pesan_error.error_tipe_data(["float"])


def diameter_lingkaran(jari: float | int) -> float | str:
    """
    menghitung diameter lingkaran

    parameter:
        jari (float atau integer): jari-jari lingkaran
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jari, (float, int)):
        return 2 * jari
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def persamaan_linear(
    a: int | float, b: int | float, c: int | float
) -> int | float | str:
    """
    menghitung persamaan linear

    parameter:
        a (float atau integer): nilai a
        b (float atau integer): nilai b
        c (float atau integer): nilai c

    return:
        (float atau integer): hasil persamaan linear dari 3 bilangan a, b, dan c
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance((a, b, c), (int, float)):
        return (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def rata_rata(nilai: list[int | float]) -> list[int | float] | str:
    """
    menghitung nilai rata-rata

    parameter:
        nilai (list(float atau integer)): nilai yang dihitung
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, (list)):
        # membuat looping untuk memecah nilai yang terdapat pada list
        for cek_nilai in nilai:
            # mengecek nilai di dalam list apakah semua tipe data berbentuk int atau float
            # jika tidak maka error
            if isinstance(cek_nilai, (int, float)):
                return sum(nilai) / len(nilai)
            else:
                return pesan_error.error_tipe_data(["float", "int"])
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def faktorial(nilai: int) -> int | str:
    """
    menghitung produk dari semua bilangan bulat positif
    contoh `4! = 24 = 4 x 3 x 2 x 1`

    parameter:
        nilai (int): nilai yang akan di faktorial
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, int):
        if nilai == 0 or nilai == 1:
            return 1
        else:
            return nilai * faktorial(nilai - 1)
    else:
        return pesan_error.error_tipe_data(["int"])


def permutasi(nilai: int, r: int) -> int | float | str:
    """
    menghitung nilai permutasi dari n objek yang diambil dari r

    parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, (int, float)):
        return faktorial(nilai) / faktorial(nilai - r)
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def kombinasi(nilai: int, r: int) -> int | float | str:
    """
    menghitung nilai kombasi dari n objek yang diambil dari r

    parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, (int, float)):
        return faktorial(nilai) / (faktorial(r) * faktorial(nilai - r))
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def fpb(
    bilangan_pertama: int | float, bilangan_kedua: int | float
) -> int | float | str:
    """
    menghitung faktor persekutuan terbesar dari dua buah bilangan

    parameter:
        bilangan_pertama (float atau integer): bilagan pertama
        bilangan_kedua (float atau integer): bilangan kedua
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(bilangan_pertama, (int, float)) and isinstance(
        bilangan_kedua, (int, float)
    ):
        while bilangan_kedua:
            bilangan_pertama, bilangan_kedua = (
                bilangan_kedua,
                bilangan_pertama % bilangan_kedua,
            )
        return abs(bilangan_pertama)
    else:
        return pesan_error.error_tipe_data(["float", "int"])


def faktor_prima(n: int) -> list[int] | str:
    """
    membuat fungsi untuk mengurutkan nilai faktor prima

    parameter:
        n (int): rentang angka yang mau di tampilkan bilangan faktor prima
    """
    # mengecek apakah variable n bertipe data integer atau float
    if not isinstance(n, (int)) and not isinstance(n, (float)):
        # menampilkan pesan error jika tipe data salah
        return pesan_error.error_tipe_data(["float", "int"])
    else:
        # jika desimal mengubah bilangan ke integer
        n = int(n)
        i = 2
        faktor = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                # memasukkan hasil faktor prima ke dalam list
                faktor.append(i)
        if n > 1:
            faktor.append(i)
        return faktor


def peluang_kejadian(
    kejadian: int | float, ukuran_sampel: int | float
) -> int | float | str:
    """
    menghitung probabilitas dari suatu kejadian

    parameter:
        kejadian (float atau integer): jumlah hasil yang menguntungkan (n(A))
        ukuran sampel (float atau integer): ukurang ruang sampel (n(S))
    """
    # mengecek apakah variable kejadian, ukuran sampel bertipe data integer atau float
    if not isinstance(kejadian, (float, int)) and not isinstance(
        ukuran_sampel, (float, int)
    ):
        return pesan_error.error_tipe_data(["float", "int"])
    else:
        try:
            return kejadian / ukuran_sampel
        except ZeroDivisionError:
            # menampilkan pesan error jika dibagi dengan 0
            return pesan_error.error_dibagi_nol()


def hitung_jumlah_deret(
    n: float | int, a: float | int, b: float | int
) -> float | int | str:
    """
    menghitung jumlah deret aritmatika

    parameter:
        n (float atau integer): jumlah suku dalam deret
        a (float atau integer): suku pertama dalam deret
        b (float atau integer): selisih antara dua suku berturut-turut
    """
    # mengecek apakah variable n, a dan b bertipe data integer atau float
    if (
        not isinstance(n, (float, int))
        and not isinstance(a, (float, int))
        and not isinstance(b, (float, int))
    ):
        return pesan_error.error_tipe_data(["float", "int"])
    else:
        return 0.5 * n * (2 * a + (n - 1) * b)
