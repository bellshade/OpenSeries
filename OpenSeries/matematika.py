from OpenSeries.util import constant as constant
from OpenSeries.util import error as error
from typing import Union, Sequence
import math


def radian_ke_derajat(radian: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai radian ke derajat

    parameter:
        radian (float atau integer): nilai radian
    """
    if not isinstance(radian, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return radian * (180 / constant.pi)


def derajat_ke_radian(derajat: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai derajat ke nilai radian

    parameter:
        derajat (float atau int): nilai derajat
    """
    if not isinstance(derajat, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return derajat * (constant.pi / 180)


def radian_ke_gradian(radian: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai radian ke gradian

    Parameter:
        radian (float atau int): nilai radian
    """
    if not isinstance(radian, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return radian * (200 / constant.pi)


def gradian_ke_radian(gradian: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai gradian ke radian

    parameter:
        gradian (float atau int): nilai gradian
    """
    if not isinstance(gradian, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return gradian * (constant.pi / 200)


def luas_lingkaran(jari: Union[float, int]) -> Union[float, error.ErrorTipeData]:
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
        return error.ErrorTipeData(["float", "int"])


def keliling_lingkaran(jari: Union[float, int]) -> Union[float, error.ErrorTipeData]:
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
        return error.ErrorTipeData(["float", "int"])


def diameter_lingkaran(jari: Union[float, int]) -> Union[float, error.ErrorTipeData]:
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
        return error.ErrorTipeData(["float", "int"])


def persamaan_kuadrat(
    a: Union[int, float], b: Union[int, float], c: Union[int, float]
) -> Union[float, int, error.Error, error.ErrorTipeData]:
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
    if all(isinstance(data, (int, float)) for data in [a, b, c]):
        diskriminan = b**2 - 4 * a * c
        if diskriminan >= 0:
            akar1 = (-b + math.sqrt(diskriminan)) / (2 * a)
            return akar1
        else:
            return error.Error("Persamaan memiliki solusi complex")
    else:
        return error.ErrorTipeData(["float", "int"])


def rata_rata(
    nilai: Sequence[Union[int, float]],
) -> Union[int, float, error.Error, error.ErrorTipeData]:
    """
    menghitung nilai rata-rata

    parameter:
        nilai (list(float atau integer)): nilai yang dihitung
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, list):
        # mengecek apakah nilai dalam list kodong
        if not nilai:
            return error.Error("List tidak boleh kosong")
        # membuat looping untuk memecah nilai yang terdapat pada list
        for cek_nilai in nilai:
            # mengecek nilai dalam list apakah semua tipe data berbentuk int
            # atau float, jika tidak error
            if not isinstance(cek_nilai, (int, float)):
                return error.ErrorTipeData(["float", "int"])
        # menghitung nilai rata-rata
        return sum(nilai) / len(nilai)
    else:
        return error.ErrorTipeData(["float", "int"])


def faktorial(nilai: int) -> Union[int, float, error.Error, error.ErrorTipeData]:
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
        elif nilai < 0:
            return error.Error("Tidak bisa menggunakan angka negatif")
        else:
            hasil_rekursif = faktorial(nilai - 1)
            if isinstance(hasil_rekursif, int):
                return nilai * hasil_rekursif
            else:
                return hasil_rekursif
    else:
        return error.ErrorTipeData(["int"])


def permutasi(nilai: int, r: int) -> Union[int, float, error.ErrorTipeData]:
    """
    menghitung nilai permutasi dari n objek yang diambil dari r

    parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(nilai, int) or not isinstance(r, int):
        return error.ErrorTipeData(["int"])
    else:
        faktorial_nilai = faktorial(nilai)
        faktorial_nilai_r = faktorial(nilai - r)

        if isinstance(faktorial_nilai, int) and isinstance(faktorial_nilai_r, int):
            return faktorial_nilai / faktorial_nilai_r
        else:
            return error.ErrorTipeData(["int"])


def kombinasi(nilai: int, r: int) -> Union[int, float, error.ErrorTipeData]:
    """
    menghitung nilai kombasi dari n objek yang diambil dari r

    parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, (int)) and isinstance(r, int):
        faktorial_nilai = faktorial(nilai)
        faktorial_r = faktorial(r)
        faktorial_nilai_r = faktorial(nilai - r)

        if (
            isinstance(faktorial_nilai, int)
            and isinstance(faktorial_r, int)
            and isinstance(faktorial_nilai_r, int)
        ):
            return faktorial_nilai / (faktorial_r * faktorial_nilai_r)
        else:
            return error.ErrorTipeData(["int"])
    else:
        return error.ErrorTipeData(["int"])


def fpb(
    bilangan_pertama: Union[int, float], bilangan_kedua: Union[int, float]
) -> Union[int, float, error.Error, error.ErrorTipeData]:
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
        if bilangan_pertama < 0 and bilangan_kedua < 0:
            return error.Error("Angka tidak boleh negatif")
        else:
            while bilangan_kedua:
                bilangan_pertama, bilangan_kedua = (
                    bilangan_kedua,
                    bilangan_pertama % bilangan_kedua,
                )
            return abs(bilangan_pertama)
    else:
        return error.ErrorTipeData(["float", "int"])


def faktor_prima(n: int) -> Union[list[int], error.Error, error.ErrorTipeData]:
    """
    membuat fungsi untuk mengurutkan nilai faktor prima

    parameter:
        n (int): rentang angka yang mau di tampilkan bilangan faktor prima
    """
    # mengecek apakah variable n bertipe data integer atau float
    if not isinstance(n, (int)):
        # menampilkan pesan error jika tipe data salah
        return error.ErrorTipeData(["int"])
    else:
        if n < 0:
            return error.Error("Angka tidak boleh negatif")
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
                faktor.append(n)
            return faktor


def peluang_kejadian(
    kejadian: Union[int, float], ukuran_sampel: Union[int, float]
) -> Union[int, float, error.ErrorTipeData, error.ErrorDibagiNol]:
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
        return error.ErrorTipeData(["float", "int"])
    else:
        try:
            return kejadian / ukuran_sampel
        except ZeroDivisionError:
            # menampilkan pesan error jika dibagi dengan 0
            return error.ErrorDibagiNol()


def hitung_jumlah_deret(
    n: Union[float, int], a: Union[float, int], b: Union[float, int]
) -> Union[float, int, error.ErrorTipeData]:
    """
    menghitung jumlah deret aritmatika

    parameter:
        n (float atau integer): jumlah suku dalam deret
        a (float atau integer): suku pertama dalam deret
        b (float atau integer): selisih antara dua suku berturut-turut
    """
    # mengecek apakah variable n, a dan b bertipe data integer atau float
    if all(isinstance(data, (float, int)) for data in [n, a, b]):
        return error.ErrorTipeData(["float", "int"])
    else:
        return 0.5 * n * (2 * a + (n - 1) * b)


def transpose_matriks(
    matriks: list[list[Union[float, int]]],
) -> Union[list[list[Union[float, int]]], error.ErrorTipeData]:
    """
    fungsi untuk transpose matrix

    parameter:
        matriks: list[float, int]: matriks yang akan di transpose
    """
    if not isinstance(matriks, list):
        return error.ErrorTipeData(["list"])
    else:
        return [
            [matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))
        ]


def euler_pi(
    n: int,
) -> Union[int, float, error.ErrorTipeData, error.Error]:
    """
    menghitung fungsi dari euler pi

    parameter:
        n (int): bilangan untuk menghitung fungsi dari euler phi
    """
    if not isinstance(n, int):
        return error.ErrorTipeData(["int"])
    elif n <= 0:
        return error.Error("nilai dari bilangan tidak boleh negatif atau 0")
    else:
        s = float(n)
        faktor_prima_n = faktor_prima(n)
        if isinstance(faktor_prima_n, list):
            for x in set(faktor_prima_n):
                s *= (x - 1) / x
            return s
        else:
            return faktor_prima_n
