from OpenSeries.util import error as error
from typing import Union


def kecepatan(jarak: Union[float, int], waktu: Union[float, int]) -> Union[float, str]:
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
    if all(isinstance(data, (float, int)) for data in [jarak, waktu]):
        try:
            return jarak / waktu
        except ZeroDivisionError:
            # error jika hasil pembagian dibagikan dengan 0
            return error.ErrorDibagiNol()
    else:
        return error.ErrorTipeData(["int", "float"])


def percepatan(
    kecepatan: Union[float, int], waktu: Union[float, int]
) -> Union[float, str]:
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
    if all(isinstance(data, (float, int)) for data in [kecepatan, waktu]):
        try:
            return kecepatan / waktu
        except ZeroDivisionError:
            # error jika hasil pembagian dibagikan dengan 0
            return error.ErrorDibagiNol()
    else:
        return error.ErrorTipeData(["int", "float"])


def gerak_lurus_beraturan(
    kecepatan_awal: float, a: float, t: float
) -> Union[float, str]:
    """
    fungsi untuk menghitung jarak yang ditempuh oleh benda yang bergerak lurus beraturan

    parameter:
        kecepatan_awal (float): kecepatan awal (m/s)
        a (float): percepatan (m/s**2)
        t (float): waktu (s)
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float)) for data in [kecepatan_awal, a, t]):
        return kecepatan_awal * t + 0.5 * a * t**2
    else:
        return error.ErrorTipeData(["float"])


def energi_kinetik(
    massa: Union[float, int], kecepatan: Union[int, float]
) -> Union[int, float, str]:
    """
    menghitung energi kinetik

    parameter:
        massa (float): massa benda
        kecepatan (float atau int): kecepatan benda
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float, int)) for data in [massa, kecepatan]):
        return 0.5 * massa * kecepatan**2
    else:
        return error.ErrorTipeData(["int", "float"])


def masa_jenis(
    massa: Union[int, float], volume: Union[int, float]
) -> Union[int, float, str]:
    """
    menghitung masa jenis suatu benda

    parameter:
        massa (float atau int): massa benda
        volume (float atau int): volume benda
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float, int)) for data in [massa, volume]):
        try:
            return massa / volume
        except ZeroDivisionError:
            # error jika hasil pembagian dibagikan dengan 0
            return error.ErrorDibagiNol()
    else:
        return error.ErrorTipeData(["int", "float"])


def energi_potensial(
    m: Union[int, float], g: Union[int, float], h: Union[int, float]
) -> Union[float, int, str]:
    """
    menghitung energi potensial dengan rumus Ep = m * g * h

    Parameter:
        m (float atau int): masa benda
        g (float atau int): gravitasi bumi
        h (float atau int): ketinggian suatu benda
    """
    if not all(isinstance(data, (float, int)) for data in [m, g, h]):
        return error.ErrorTipeData(["float", "int"])
    else:
        return m * g * h


def hukum_ohm(i: Union[float, int], r: Union[float, int]) -> Union[float, int, str]:
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
    if not all(isinstance(data, (float, int)) for data in [i, r]):
        return error.ErrorTipeData(["float", "int"])
    else:
        return i * r


def ketinggian_barometrik(tekanan: float) -> Union[float, str]:
    """
    fungsi untuk menghitung perkiraan ketinggian berdasarkan dari
    tekanan udara yang menggunakan rumus barometrik

    Parameter:
        tekanan (float): tekanan udara
    """
    if not isinstance(tekanan, float):
        return error.ErrorTipeData(["float"])
    else:
        if tekanan > 101325:
            return error.Error(
                "nilai lebih tinggi dari tekanan di permukaan laut"
            )
        if tekanan < 0:
            return error.Error("tekanan atmosfir tidak bisa negatif")
        else:
            hasil = 44_330 * (1 - (tekanan / 101_325) ** (1 / 5.5255))
    return hasil
