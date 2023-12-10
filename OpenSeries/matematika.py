from OpenSeries.util import constant
import math


def luas_lingkaran(jari: float | int) -> float:
    """
    menghitung luas lingkaran

    Parameter:
    jari-jari (float atau integer): jari jari yang akan dihitung
    """
    return constant.pi * jari**2


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
