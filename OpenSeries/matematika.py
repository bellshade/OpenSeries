from OpenSeries.util import constant
import math


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
        return "kamu memasukkan tipe data yang salah"


def keliling_lingkaran(jari: float | int) -> float:
    """
    menghitung keliling lingkaran

    parameter:
        jari (float atau integer); jari-jari lingkaran
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jari, (float, int)):
        return 2 * constant.pi * jari
    else:
        return "kamu memasukkan tipe data yang salah"


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
        return "kamu memasukkan tipe data yang salah"


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
        return "kamu memasukkan tipe data yang salah"


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
                return "kamu memasukkan tipe data yang salah, harus int atau float"
    else:
        return "kamu memasukkan tipe data yang salah"


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
        return "kamu memasukkan tipe data yang salah"


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
        return "kamu memasukkan tipe data yang salah"


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
        return "kamu memasukkan tipe data yang salah"


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
        return "kamu memasukkan tipe data yang salah"
