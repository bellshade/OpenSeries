import math


def kecepatan(jarak: float | int, waktu: float | int) -> float:
    """
    fungsi untuk menghitung kecepatan

    Parameter:
    jarak (float atau int): jarak tempuh
    waktu (float atau int): waktu tempuh (sekon)

    Return:
    float: hasil dari jarak / waktu
    """
    return jarak / waktu


def percepatan(kecepatan: float | int, waktu: float | int) -> float:
    """
    fungsi untuk menghitung percepatan

    parameter:
    kecepatan (float atau int): kecepatan (m/s)
    waktu (float atau int): waktu tempuh (sekon)

    Return:
    float: hasil dari kecepatan / waktu
    """
    return kecepatan / waktu


def gerak_lurus_beraturan(kecepatan_awal: float, a: float, t: float) -> float:
    """
    fungsi untuk menghitung jarak yang ditempuh oleh benda yang bergerak lurus beraturan

    parameter:
        kecepatan_awal (float): kecepatan awal (m/s)
        a (float): percepatan (m/s**2)
        t (float): waktu (s)
    """
    return kecepatan_awal * t + 0.5 * a * t**2


def koordinat_parabola(v0: float, y0: float, x0: float, a: float) -> float:
    """
    menghitung koordinat (x, y) dari sebuah parabola

    paremeter:
        v0: kecepatan awal (m/s)
        y0: koordinat awal y (m)
        x0: koordinat awal x (m)
        a: percepatan gravitasi (m/s**2)

    return:
        x: koordinat x (m)
    """
    y = y0 + v0 + math.sin(a) * t - (g / 2) * t**2
    x = x0 + v0 + math.cos(a) * t

    return x, y
