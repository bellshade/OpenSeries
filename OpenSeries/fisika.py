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
    if isinstance(jarak, (float, int)) and isinstance(waktu, (float, int)):
        try:
            return jarak / waktu
        except ZeroDivisionError:
            print("tidak bisa dibagikan dengan 0")
    else:
        print("kamu memasukkan tipe data yang salah")
    return None


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


def energi_kinetik(massa: float, kecepatan: int | float) -> int | float:
    """
    menghitung energi kinetik

    parameter:
        massa (float): massa benda
        kecepatan (float atau int): kecepatan benda
    """
    return 0.5 * massa * kecepatan**2


def masa_jenis(massa: int | float, volume: int | float) -> int | float:
    """
    menghitung masa jenis suatu benda

    parameter:
        massa (float atau int): massa benda
        volume (float atau int): volume benda
    """
    return massa / volume
