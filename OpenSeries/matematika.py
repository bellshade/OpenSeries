from OpenSeries.util import constant
import math


def luas_lingkaran(jari: float | int) -> float:
    """
    menghitung luas lingkaran

    Parameter:
    jari-jari (float atau integer): jari jari yang akan dihitung
    """
    return constant.pi * jari**2


def keliling_lingkaran(jari: float | int) -> float:
    """
    menghitung keliling lingkaran

    parameter:
        jari (float atau integer); jari-jari lingkaran
    """
    return 2 * constant.pi * jari


def diameter_lingkaran(jari: float | int) -> float:
    """
    menghitung diameter lingkaran

    parameter:
        jari (float atau integer): jari-jari lingkaran
    """
    return 2 * jari


def persamaan_linear(a: int | float, b: int | float, c: int | float) -> int | float:
    """
    menghitung persamaan linear

    parameter:
        a (float atau integer): nilai a
        b (float atau integer): nilai b
        c (float atau integer): nilai c

    return:
        (float atau integer): hasil persamaan linear dari 3 bilangan a, b, dan c
    """
    return (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a


def rata_rata(nilai: list[int | float]) -> list[int | float]:
    """
    menghitung nilai rata-rata

    parameter:
        nilai (list(float atau integer)): nilai yang dihitung
    """
    return sum(nilai) / len(nilai)


def faktorial(nilai: int) -> int:
    """
    menghitung produk dari semua bilangan bulat positif
    contoh `4! = 24 = 4 x 3 x 2 x 1`

    parameter:
        nilai (int): nilai yang akan di faktorial
    """
    if nilai == 0 or nilai == 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)


def permutasi(nilai: int, r: int) -> int | float:
    """
    menghitung nilai permutasi dari n objek yang diambil dari r

    parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil
    """
    return faktorial(nilai) / faktorial(nilai - r)


def kombinasi(nilai: int, r: int) -> int | float:
    """
    menghitung nilai kombasi dari n objek yang diambil dari r

    parameter:
        nilai (int): nilai objek
        r (int): jumlah objek yang diambil
    """
    return faktorial(nilai) / (faktorial(r) * faktorial(nilai - r))


def fpb(bilangan_pertama: int | float, bilangan_kedua: int | float) -> int | float:
    """
    menghitung faktor persekutuan terbesar dari dua buah bilangan

    parameter:
        bilangan_pertama (float atau integer): bilagan pertama
        bilangan_kedua (float atau integer): bilangan kedua
    """
    while bilangan_kedua:
        bilangan_pertama, bilangan_kedua = (
            bilangan_kedua,
            bilangan_pertama % bilangan_kedua,
        )
    return abs(bilangan_pertama)
