# Copyright (c) 2023 Bellshade
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from OpenSeries.util import constant as constant
from OpenSeries.util import error as error
from typing import Union, Sequence, Callable
import numpy as np
import math


def radian_ke_derajat(radian: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai radian ke derajat

    Parameter:
        radian (float atau integer): nilai radian

    Return:
        (float): hasil dari kalkulasi radian ke derajat
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(radian, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return radian * (180 / constant.PI)


def derajat_ke_radian(derajat: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai derajat ke nilai radian

    Parameter:
        derajat (float atau int): nilai derajat

    Return:
        (float): hasil dari kalkulasi derajat ke radian
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(derajat, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return derajat * (constant.PI / 180)


def radian_ke_gradian(radian: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai radian ke gradian

    Parameter:
        radian (float atau int): nilai radian

    Return:
        (float): hasil dari kalkulasi radian ke gradian
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(radian, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return radian * (200 / constant.PI)


def gradian_ke_radian(gradian: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    mengubah nilai gradian ke radian

    Parameter:
        gradian (float atau int): nilai gradian

    Return:
        (float): hasil dari kalkulasi gradian ke radian
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(gradian, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return gradian * (constant.PI / 200)


def luas_lingkaran(jari: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    menghitung luas lingkaran

    Parameter:
        jari-jari (float atau integer): jari jari yang akan dihitung

    Return:
        (float): hasil dari kalkulasi luas lingkaran
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jari, (float, int)):
        return constant.PI * jari**2
    else:
        return error.ErrorTipeData(["float", "int"])


def keliling_lingkaran(jari: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    menghitung keliling lingkaran

    Parameter:
        jari (float atau integer): jari-jari lingkaran

    Return:
        (float): hasil dari kalkulasi keliling lingkaran
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jari, (float, int)):
        return 2 * constant.PI * jari
    else:
        return error.ErrorTipeData(["float", "int"])


def diameter_lingkaran(jari: Union[float, int]) -> Union[float, error.ErrorTipeData]:
    """
    menghitung diameter lingkaran

    Parameter:
        jari (float atau integer): jari-jari lingkaran

    Return:
        (float): hasil dari kalkulasi diameter lingkaran
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(jari, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    return 2 * jari


def persamaan_kuadrat(
    a: Union[int, float], b: Union[int, float], c: Union[int, float]
) -> Union[float, int, error.Error, error.ErrorTipeData]:
    """
    menghitung persamaan linear

    Parameter:
        a (float atau integer): nilai a
        b (float atau integer): nilai b
        c (float atau integer): nilai c

    Return:
        (float atau integer): hasil persamaan linear dari 3 bilangan a, b, dan c
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika memiliki nilai complex
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

    Parameter:
        nilai (list(float atau integer)): nilai yang dihitung

    Return:
        (int, float): hasil dari kalkulasi nilai rata-rata
        error.ErrorTipeData: error jika tipe data error
        error.Error: jika di dalam list nilai kosong
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

    Parameter:
        nilai (int): nilai yang akan di faktorial

    Return:
        (int, float): hasil dari kalkulasi faktorial
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika nilai dimasukkan negatif
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(nilai, int):
        return error.ErrorTipeData(["int"])
    if nilai < 0:
        return error.Error("Tidak bisa menggunakan angka negatif")
    try:
        return math.factorial(nilai)
    except OverflowError:
        # faktorial untuk nilai yang cukup besar sehingga menghasilkan overflow
        return error.Error("Nilai terlalu besar untuk dihitung faktorialnya")


def permutasi(nilai: int, r: int) -> Union[int, float, error.ErrorTipeData]:
    """
    menghitung nilai permutasi dari n objek yang diambil dari r

    Parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil

    Return:
        (int, float): hasil dari kalkulasi permutasi
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(nilai, int) or not isinstance(r, int):
        return error.ErrorTipeData(["int"])
    else:
        faktorial_nilai = faktorial(nilai)
        faktorial_nilai_r = faktorial(nilai - r)

        # mengecek tipe data dari nilai faktorial
        if isinstance(faktorial_nilai, int) and isinstance(faktorial_nilai_r, int):
            return faktorial_nilai / faktorial_nilai_r
        else:
            return error.ErrorTipeData(["int"])


def kombinasi(nilai: int, r: int) -> Union[int, float, error.ErrorTipeData]:
    """
    menghitung nilai kombinasi dari n objek yang diambil dari r

    Parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil

    Return:
        (int, float): hasil dari kalkulasi kombinasi
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(nilai, (int)) and isinstance(r, int):
        faktorial_nilai = faktorial(nilai)
        faktorial_r = faktorial(r)
        faktorial_nilai_r = faktorial(nilai - r)

        # mengecek nilai dari faktorial nilai
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

    Parameter:
        bilangan_pertama (float atau integer): bilagan pertama
        bilangan_kedua (float atau integer): bilangan kedua

    Return:
        (int, float): hasil dari kalkulasi fpb
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika nilai yang diberikan negatif
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

    Parameter:
        n (int): rentang angka yang mau di tampilkan bilangan faktor prima

    Return:
        (list[int]): hasil dari kalkulasi dari faktor prima
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
        error.Error: jika angka diberikan nilai negatif
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

    Parameter:
        kejadian (float atau integer): jumlah hasil yang menguntungkan (n(A))
        ukuran sampel (float atau integer): ukurang ruang sampel (n(S))

    Return:
        (int, float): hasil dari kalkulasi peluang kejadian
        error.ErrorTipeData: error jika tipe data salah
        error.ErrorDibagiNol: error jika nilai dibagi dengan 0
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

    Parameter:
        n (float atau integer): jumlah suku dalam deret
        a (float atau integer): suku pertama dalam deret
        b (float atau integer): selisih antara dua suku berturut-turut

    Return:
        (float, int): hasil dari kalkulasi jumlah deret
        error.ErrorTipeData: error jika tipe data salah
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

    Parameter:
        matriks: list[float, int]: matriks yang akan di transpose

    Return:
        (list[float atau int]): hasil dari kalkulasi transpose matriks
        error.ErrorTipeData: jika error tipe data yang diberikan salah
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

    Parameter:
        n (int): bilangan untuk menghitung fungsi dari euler phi

    Return:
        (int, float): hasil dari kalkulasi fungsi euler pi
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika nilai yang diberikan negatif
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


def sigmoid(vektor: np.ndarray) -> Union[error.ErrorTipeData, np.ndarray]:
    """
    fungsi sigmoid adalah fungsi yang berbentuk huruf S. fungsi ini biasanya
    digunakan untuk mengubah nilai input dari neuron menjadi nilai output yang
    lebih mudah diproses oleh neuron lain

    Parameter:
        vektor (np.ndarray): rentang nilai array yang ingin dimasukkan

    Return:
        (np.ndarray): hasil dari kalkulasi sigmoid
        error.ErrorTipeData: error jika tipe data salah
    """
    if not isinstance(vektor, np.ndarray):
        return error.ErrorTipeData(["numpy.narray"])
    return 1 / (1 + np.exp(-vektor))


def distribusi_binomial(
    keberhasilan: int,
    percobaan: int,
    probabilitas: Union[float, int],
) -> Union[float, error.ErrorTipeData, error.ErrorValue]:
    """
    mengembalikan probabilitas k keberhasilan dari n percobaan, dengan probabilitas p
    untuk satu keberhasilan

    fungsi ini menggunakan fungsi faktorial untuk menghitung koefisien binomial

    Parameter:
        keberhasilan (int): probabilitas
        percobaan (int): percobaan dari distribusi binomial
        probabilitas (int): probabilitas dari suatu keberhasilan

    Return:
        (float): hasil dari distribusi binomial
    """
    if keberhasilan > percobaan:
        return error.ErrorValue(
            "jumlah keberhasilan harus kurang dari atau sama dengan jumlah percobaan"
        )
    if percobaan < 0 or keberhasilan < 0:
        return error.ErrorValue("nilai percobaan dan keberhasilan tidak boleh negatif")
    if not all(isinstance(data, (int)) for data in [keberhasilan, percobaan]):
        return error.ErrorTipeData(["int"])
    if not 0 < probabilitas < 1:
        return error.ErrorValue("nilai probabilitas harus 0 atau 1")

    probabilitas_kejadian = (probabilitas**keberhasilan) * (
        (1 - probabilitas) ** (percobaan - keberhasilan)
    )

    koefisien = float(math.factorial(percobaan))
    koefisien /= math.factorial(keberhasilan) * math.factorial(percobaan - keberhasilan)
    return probabilitas_kejadian * koefisien


def gaussian(
    x: int, mu: Union[float, int] = 0.0, sigma: Union[float, int] = 1.0
) -> Union[float, error.ErrorTipeData]:
    """
    fungsi gaussian, yang biasa disebut fungsi kurva lonceng adalah fungsi
    untuk mendeskripsikan probabilitas distribusi data yang normal
    """
    if not all(
        isinstance(data, (float, int)) for data in [sigma, mu]
    ) and not isinstance(x, int):
        return error.ErrorTipeData(["float", "int"])
    return (
        1
        / np.sqrt(2 * constant.PI * sigma**2)
        * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
    )


def integral(
    f: Callable[[float], float], a: int, b: int, iterasi: int = 4
) -> Union[float, error.ErrorTipeData]:
    """
    integral merupakan suatu konsep yang merupakan operasi kebalikan dari diferensiasi.
    Integral memiliki dua bentuk utama: integral tak tentu (indefinite integral)
    dan integral tentu (definite integral).
    Args:
        f (Callable[[float],float]): fungsi input
        a (float): nilai awal
        b (float): nilai atas
        iterable (int, optional): mengatur putaran. Defaults to 4.

    """
    if not all(isinstance(data, (int)) for data in [a, b]):
        return error.ErrorTipeData(["int"])
    if not isinstance(iterasi, int):
        return error.ErrorTipeData(["int"])
    delta = (b - a) / iterasi
    result = 0.5 * (f(a) + f(b))
    for i in range(1, iterasi):
        result += f(a + i * delta)
    return round(result * delta)


def turunan(
    f: Callable[[float], float], x: Union[int, float]
) -> Union[error.ErrorTipeData, float]:
    """
    Args:
        f (Callable[[float]float]: input fungsi
        x (int) : input value
    Return:
        float : hasil dari kalkulasi apromasif
    """
    # insial nilai h
    h: float = 0.0001
    # mengecek tipe data pada nilai input pada paramter a dan b dan iterasi
    if not isinstance(x, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (f(x + h) - f(x)) / h


def volume_bola(r: Union[int, float]) -> Union[float, error.ErrorTipeData]:
    """
    Menghitung volume dari sebuah bola
    Args:
        r (Union[int, float]): input radius
    Return:
        float : volume dari bola
    """
    if not isinstance(r, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (4 / 3) * constant.PI * r**3


def mean_absolut_deviasi(
    nilai: list[int],
) -> Union[error.Error, error.ErrorTipeData, float]:
    """
    Ukuran statistik untuk menggambarkan variabilitias kumpulan data.

    Args:
        nilai (list[int]): angka yang dihitung
    Return:
        float: hasil dari variabilitias kumpulan data
        error.Error: jika list kosong
        error.ErrorTipeData: jika tipe data float maka error
    """
    if isinstance(nilai, list):
        # mengecek apakah nilai dalam list kodong
        if not nilai:
            return error.Error("List tidak boleh kosong")
        else:
            for cek_nilai in nilai:
                if not isinstance(cek_nilai, int):
                    return error.ErrorTipeData(["int"])
            rata_rata = sum(nilai) / len(nilai)
            return sum(abs(x - rata_rata) for x in nilai) / len(nilai)
    else:
        return error.ErrorTipeData(["list[int]"])
