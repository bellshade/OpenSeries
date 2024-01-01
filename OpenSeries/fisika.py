import math
import OpenSeries.util.error as error


def kecepatan(jarak: float | int, waktu: float | int) -> float | str:
    """
    fungsi untuk menghitung kecepatan

    Parameter:
    jarak (float atau int): jarak tempuh
    waktu (float atau int): waktu tempuh (sekon)

    Return:
    float: hasil dari jarak / waktu
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(jarak, (float, int)) and isinstance(waktu, (float, int)):
        try:
            return jarak / waktu
        except ZeroDivisionError:
            # error jika hasil pembagian dibagikan dengan 0
            return erro.error_dibagi_nol()
    else:
        return error.error_tipe_data(["int", "float"])


def percepatan(kecepatan: float | int, waktu: float | int) -> float | str:
    """
    fungsi untuk menghitung percepatan

    parameter:
    kecepatan (float atau int): kecepatan (m/s)
    waktu (float atau int): waktu tempuh (sekon)

    Return:
    float: hasil dari kecepatan / waktu
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(kecepatan, (float, int)) and isinstance(waktu, (float, int)):
        try:
            return kecepatan / waktu
        except ZeroDivisionError:
            # error jika hasil pembagian dibagikan dengan 0
            return error.error_dibagi_nol()
    else:
        return error.error_tipe_data(["int", "float"])


def gerak_lurus_beraturan(kecepatan_awal: float, a: float, t: float) -> float | str:
    """
    fungsi untuk menghitung jarak yang ditempuh oleh benda yang bergerak lurus beraturan

    parameter:
        kecepatan_awal (float): kecepatan awal (m/s)
        a (float): percepatan (m/s**2)
        t (float): waktu (s)
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if (
        isinstance(kecepatan_awal, float)
        and isinstance(a, float)
        and isinstance(t, float)
    ):
        return kecepatan_awal * t + 0.5 * a * t**2
    else:
        return error.error_tipe_data(["int", "float"])


def energi_kinetik(massa: float | int, kecepatan: int | float) -> int | float | str:
    """
    menghitung energi kinetik

    parameter:
        massa (float): massa benda
        kecepatan (float atau int): kecepatan benda
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(massa, (int, float)) and isinstance(kecepatan, (int, float)):
        return 0.5 * massa * kecepatan**2
    else:
        return error.error_tipe_data(["int", "float"])


def masa_jenis(massa: int | float, volume: int | float) -> int | float | str:
    """
    menghitung masa jenis suatu benda

    parameter:
        massa (float atau int): massa benda
        volume (float atau int): volume benda
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if isinstance(massa, (int, float)) and isinstance(volume, (int, float)):
        try:
            return massa / volume
        except ZeroDivisionError:
            # error jika hasil pembagian dibagikan dengan 0
            return error.error_dibagi_nol()
    else:
        return error.error_tipe_data(["int", "float"])


def energi_potensial(
    m: int | float, g: int | float, h: int | float
) -> float | int | str:
    """
    menghitung energi potensial dengan rumus Ep = m * g * h

    Parameter:
        m (float atau int): masa benda
        g (float atau int): gravitasi bumi
        h (float atau int): ketinggian suatu benda
    """
    if (
        not isinstance(m, (float, int))
        and not isinstance(g, (float, int))
        and not isinstance(h, (float, int))
    ):
        return error.error_tipe_data(["float", "int"])
    else:
        return m * g * h


def hukum_ohm(i: float | int, r: float | int) -> float | int | str:
    """
    menghitung hukum ohm dengan besar arus listrik yang mengalir
    melalui sebuah hantaran akan berbanding lurus dengan tengangan potensial
    yang diterapkan kepadanya dan berbanding balik dengan hambatan

    Parameter:
        i (float atau int): kuat arus
        r (float atau int): hambatan (ditulis omega)
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(i, (float, int)) and not isinstance(r, (float, int)):
        return error.error_tipe_data(["float", "int"])
    else:
        return i * r
