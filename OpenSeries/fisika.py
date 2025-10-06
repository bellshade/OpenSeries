import numpy
from .util import error as error
from typing import Union
from .fisika_calc import kecepatan_calc


def kecepatan(
    jarak: Union[float, int, list[Union[float, int]], numpy.ndarray],
    waktu: Union[float, int, list[Union[float, int]], numpy.ndarray],
) -> Union[
    float,
    list[Union[float, error.ErrorDibagiNol, error.ErrorTipeData, error.Error]],
    error.ErrorDibagiNol,
    error.ErrorTipeData,
    error.Error,
]:
    """
    fungsi menghitung kecepatan benda antara satu dan lainnya

    Parameter:
        jarak (list, numpy.ndarray, float, int): jarak yang ditempuh
        waktu (list, numpy.ndarray, float, int): waktu yang ditempuh

    Return:
        (list, numpy.ndarray, float, int): hasil perhitungan antara jarak dan waktu
            menggunakan pendekatan rumus v = s / t

    Example:

    >>> kecepatan(100, 10)
    10.0

    >>> kecepatan([100, 200, 300], [10, 20, 30])
    [10.0, 10.0, 10.0]

    >>> import numpy as np
    >>> kecepatan(np.array([100, 20]), np.array([10, 20]))
    [10.0, 10.0]
    """
    processor = kecepatan_calc.KecepatanService.get_instance()
    if isinstance(jarak, (int, float, numpy.integer, numpy.floating)) and isinstance(
        waktu, (int, float, numpy.integer, numpy.floating)
    ):
        return processor.hitung_single(jarak, waktu)
    elif isinstance(jarak, (list, numpy.ndarray)) and isinstance(
        waktu, (list, numpy.ndarray)
    ):
        return processor.hitung_multiple(jarak, waktu)
    else:
        return error.ErrorTipeData(
            tipe_diharapkan=["sama-sama single atau sama-sama vektor"],
            tipe_sebenarnya=f"jarak: {type(jarak).__name__}, waktu: {type(waktu).__name__}",
            nama_parameter="jarak dan waktu",
        )


def percepatan(
    kecepatan: Union[float, int], waktu: Union[float, int]
) -> Union[float, error.ErrorDibagiNol, error.ErrorTipeData]:
    """
    fungsi untuk menghitung percepatan

    parameter:
        kecepatan (float atau int): kecepatan (m/s)
        waktu (float atau int): waktu tempuh (sekon)

    Return:
        float: hasil dari kecepatan / waktu
        error.ErrorTipeData: error jika tipe data data salah
        error.ErrorDibagiNol: jika angka dibagikan dengan 0
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
) -> Union[float, error.ErrorTipeData]:
    """
    fungsi untuk menghitung jarak yang ditempuh oleh benda yang bergerak lurus beraturan

    Parameter:
        kecepatan_awal (float): kecepatan awal (m/s)
        a (float): percepatan (m/s**2)
        t (float): waktu (s)

    Return:
        float: jarak yang ditempuh oleh benda
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float)) for data in [kecepatan_awal, a, t]):
        return kecepatan_awal * t + 0.5 * a * t**2
    else:
        return error.ErrorTipeData(["float"])


def energi_kinetik(
    massa: Union[float, int], kecepatan: Union[int, float]
) -> Union[int, float, error.ErrorTipeData]:
    """
    menghitung energi kinetik

    Parameter:
        massa (float): massa benda
        kecepatan (float atau int): kecepatan benda

    Return:
        (int, float): hasil dari perhitungan energi kinetik
        error.ErrorTipeData: error jika tipe data data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float, int)) for data in [massa, kecepatan]):
        return 0.5 * massa * kecepatan**2
    else:
        return error.ErrorTipeData(["int", "float"])


def masa_jenis(
    massa: Union[int, float], volume: Union[int, float]
) -> Union[int, float, error.ErrorDibagiNol, error.ErrorTipeData]:
    """
    menghitung masa jenis suatu benda

    Parameter:
        massa (float atau int): massa benda
        volume (float atau int): volume benda

    Return:
        (int, float): hasil dari kalkulasi fungsi dari masa jenis
        error.ErrorTipeData: error jika tipe data data salah
        error.ErrorDibagiNol: error jika angka dibagikan dengan 0
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


def kecepatan_sudut(
    sudut: Union[int, float], time: Union[int, float]
) -> Union[int, float, error.ErrorTipeData, error.ErrorDibagiNol]:
    """
    Menghitung kecepatan sudut

    Parameter:
        sudut (float atau int): sudut tempuh benda
        time (float atau int): waktu tempuh benda

    Return:
        (int,float): hasil dari kalkulasi fungsi kecepatan sudut
        error.ErrorTipeData : error jika tipe data salah
        error.ErrorDibagiNol: error jika angka dibagikan dengan 0
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float, int)) for data in [sudut, time]):
        try:
            return sudut / time
        except ZeroDivisionError:
            return error.ErrorDibagiNol()
    else:
        return error.ErrorTipeData(["int", "float"])


def percepatan_sudut(
    w_sudut: Union[int, float], time: Union[int, float]
) -> Union[int, float, error.ErrorTipeData, error.ErrorDibagiNol]:
    """
    Menghitung percepatan sudut

    Parameter:
        w_sudut (int atau float) : kecepatan sudut
        time    (int atau float) : waktu

    Return:
        (int,float): hasil dari kalkulasi fungsi percepatan sudut
        error.ErrorTipeData : error jika tipe data salah
        error.DibagiNol : error jika angka dibagikan dengan 0
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float, int)) for data in [w_sudut, time]):
        try:
            return w_sudut / time
        except ZeroDivisionError:
            return error.ErrorDibagiNol()
    else:
        return error.ErrorTipeData(["int", "float"])


def percepatan_sentripetal_linear(
    kecepatan: Union[int, float], jari_jari: Union[int, float]
) -> Union[int, float, error.ErrorTipeData, error.ErrorDibagiNol]:
    """
    Menghitung percepatan sentripetal linear

    Parameter :
        kecepatan (int,float) : kecepatan
        jari_jari (int,float) : jari-jari lintasan
    Return :
        (int,float) : hasil kalkulasi percepatan sentripetal linear
        error.ErrorTipeData : error jika tipe data salah
        error.ErrorDibagiNol : error jika dibagi dengan nol
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (float, int)) for data in [kecepatan, jari_jari]):
        try:
            return kecepatan**2 / jari_jari
        except ZeroDivisionError:
            return error.ErrorDibagiNol()
    else:
        return error.ErrorTipeData(["int", "float"])


def percepatan_sentripetal_sudut(
    jari_jari: Union[int, float], kecepatan_sudut: Union[int, float]
) -> Union[int, float, error.ErrorTipeData]:
    """
    Menghitung percepatan sentripetal sudut

    Parameter :
        kecepatan_sudut (int,float) : kecepatan sudut
        jari_jari (int,float) : jari-jari lintasan
    Return :
        (int,float) : hasil kalkulasi percepatan sentripetal sudut
        error.ErrorTipeData : error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if all(isinstance(data, (int, float)) for data in [kecepatan_sudut, jari_jari]):
        return jari_jari * (kecepatan_sudut**2)
    else:
        return error.ErrorTipeData(["int", "float"])


def gerak_melingkar_beraturan(
    w_awal: Union[int, float], a_sudut: Union[int, float], t: Union[int, float]
) -> Union[int, float, error.Error, error.ErrorTipeData]:
    """
    menghitung hasil dari gerak melingkar beraturan

    Parameter:
        w_awal (float atau int) : kecepatan sudut awal
        a_sudur (float atau int): percepatan sudut
    Return:
        (int atau float) : hasil kalkulasi dari gerak melingkar beraturan
        error.ErrorTipeData : error jika tipe data salah
        error.Errorvalue : error jika waktu kurang dari 0
    """
    if all(isinstance(data, (int, float)) for data in [w_awal, a_sudut, t]):
        return w_awal + a_sudut * t
    else:
        return error.ErrorTipeData(["Tipe data tidak sesuai"])


def inersia(
    m: Union[float, int], r: Union[float, int]
) -> Union[float, int, error.Error, error.ErrorTipeData]:
    """
    Menghitung inersia dari suatu benda

    Parameter:
        m (float atau int): massa benda
        r (float atau int): jari-jari

    Return:
        (int atau float) : hasil dari kalkulasi fungsi inersia
        error.ErrorValue : error jika massa kurang dari 0
        error.ErrorTipeData : error jika tipe data salah
    """
    if all(isinstance(data, (float, int)) for data in [m, r]):
        return m * (r**2)
    else:
        return error.ErrorTipeData(["int", "float"])


def energi_kinetik_rotasi(
    inersia: Union[float, int], kecepatan_sudut: Union[int, float]
) -> Union[int, float, error.ErrorTipeData]:
    """
    menghitung energi kinetik rotasi

    Parameter:
        inersia (float atau int): inersia benda
        kecepatan_sudut (float atau int): kecepatan benda
    Return:
        (int atau float) : hasil kalkulasi dari energi kinetik rotasi
        error.ErrorTipeData : error jika tipe data salah
    """
    if all(isinstance(data, (float, int)) for data in [inersia, kecepatan_sudut]):
        return (1 / 2) * inersia * (kecepatan_sudut**2)
    else:
        return error.ErrorTipeData(["int", "float"])


def energi_potensial(
    m: Union[int, float], g: Union[int, float], h: Union[int, float]
) -> Union[float, int, error.ErrorTipeData]:
    """
    menghitung energi potensial dengan rumus Ep = m * g * h

    Parameter:
        m (float atau int): masa benda
        g (float atau int): gravitasi bumi
        h (float atau int): ketinggian suatu benda

    Return:
        (float, int): hasil dari kalkulasi energei potensial
        error.ErrorTipeData: error jika tipe data data salah
    """
    # melakukan pengecekan apakah semua parameter memiliki tipe data dari float atau int
    if not all(isinstance(data, (float, int)) for data in [m, g, h]):
        return error.ErrorTipeData(["float", "int"])
    else:
        return m * g * h


def hukum_ohm(
    i: Union[float, int], r: Union[float, int]
) -> Union[float, int, error.ErrorTipeData]:
    """
    menghitung hukum ohm dengan besar arus listrik yang mengalir
    melalui sebuah hantaran akan berbanding lurus dengan tengangan potensial
    yang diterapkan kepadanya dan berbanding balik dengan hambatan

    Parameter:
        i (float atau int): kuat arus
        r (float atau int): hambatan (ditulis omega)

    Return:
        (float, int): hasil dari kalkulasi dari hukum ohm
        error.ErrorTipeData: error jika tipe data data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not all(isinstance(data, (float, int)) for data in [i, r]):
        return error.ErrorTipeData(["float", "int"])
    else:
        return i * r


def ketinggian_barometrik(
    tekanan: float,
) -> Union[float, error.ErrorTipeData, error.Error]:
    """
    fungsi untuk menghitung perkiraan ketinggian berdasarkan dari
    tekanan udara yang menggunakan rumus barometrik

    Parameter:
        tekanan (float): tekanan udara

    Return:
        (float): hasil dari kalkulasi ketinggian barometrik
        error.ErrorTipeData: error jika tipe data data salah
        error.Error: jika nilai lebih tinggi dari tekanan di permukaan laut
        error.Error: jika tekanan atmosfir tidak bisa negatif
    """
    # mengecek apakah variable tersebut bertipe data float
    # jika tidak maka error
    if not isinstance(tekanan, float):
        return error.ErrorTipeData(["float"])
    else:
        if tekanan > 101325:
            return error.Error("nilai lebih tinggi dari tekanan di permukaan laut")
        if tekanan < 0:
            return error.Error("tekanan atmosfir tidak bisa negatif")
        else:
            hasil = 44_330 * (1 - (tekanan / 101_325) ** (1 / 5.5255))
    return hasil


def gaya_sentripental(
    massa: Union[float, int], velocity: Union[float, int], radius: Union[float, int]
) -> Union[float, int, error.Error, error.ErrorTipeData]:
    """
    fungsi untuk menghitung gaya sentripental. gaya sentripental adalah gaya yang bekerja
    pada benda dalam gerak lengkung arahnya menuju ke sumbu rotasi atau pusat kelengkungan

    Parameter:
        massa (float): masa benda
        v (float): kecepatan dari benda
        radius (float): jari-jari lintasan melingkar

    Return:
        (float, int): hasil dari kalkulasi nilai sentripental
        error.ErrorTipeData: error jika tipe data data salah
        error.Error: jika massa negatif
        error.Error: jika radius negatif
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not all(isinstance(data, (float, int)) for data in [massa, velocity, radius]):
        return error.ErrorTipeData(["float", "int"])
    if massa < 0:
        return error.Error("Massa tidak boleh negatif")
    if radius <= 0:
        return error.Error("Radius selalu angka positif")
    return (massa * (velocity) ** 2) / radius


def efek_doppler(
    org_frek: Union[float, int],
    gelombang_vel: Union[float, int],
    obs_vel: Union[float, int],
    src_vel: Union[float, int],
) -> Union[float, error.ErrorDibagiNol, error.ErrorTipeData, error.Error]:
    """
    fungsi untuk menghitung efek doppler

    Parameter:
        org_frek (int atau float): frekuensi gelombang sumber diam
        gelombang_vel_vel (int atau float): kecepatan gelombang dalam medium
        obs_vel (int atau float): kecepatan pengamatan
        src_vel (int atau float): kecepatan sumber

    Return:
        (float): hasil dari kalkulasi efek doppler
        error.ErrorTipeData: error jika tipe data data salah
        error.Error: jika nilai doppler negatif
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not all(
        isinstance(data, (float, int))
        for data in [org_frek, gelombang_vel, obs_vel, src_vel]
    ):
        return error.ErrorTipeData(["int", "float"])
    if gelombang_vel == src_vel:
        return error.ErrorDibagiNol()
    doppler = (org_frek * (gelombang_vel + obs_vel)) / (gelombang_vel - src_vel)
    if doppler <= 0:
        return error.Error(
            "frekuensi tidak positif, kecepatan sumber relatif lebih besar dari kecepatan gelombang dalam medium"
        )
    return doppler


def celcius_farenheit(celcius: Union[int, float]) -> Union[float, int]:
    """
    mengubah nilai celcius ke farenheit

    Paramieter:
        celcius (float atau int): nilai celcius

    Return:
        (float atau int): hasil dari kalkulasi celcius ke farenheit
        error.ErrorTipeData: error jika tipe data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(celcius, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return celcius * (9 / 5) + 32


def farenheit_celcius(farenheit: Union[int, float]) -> Union[int, float]:
    """
    mengubah nilai farenheit ke celcius

    Parameter:
        farenheit(int atau float): nilai farenheit

    Return:
        (float atau int): hasil dari kalkulasi farenheit ke celcius
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(farenheit, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (farenheit - 32) * (5 / 9)


def celcius_reaumur(celcius: Union[int, float]) -> Union[int, float]:
    """
    mengubah nilai celcius ke reaumur

    Parameter:
        celcius(int atau float): nilai celcius

    Return:
        (float atau int): hasil dari kalkulasi celcius ke reaumur
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(celcius, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return celcius * (4 / 5)


def reamur_celcius(reamur: Union[int, float]) -> Union[int, float]:
    """
    mengubah nilai reamur ke celcius

    Parameter:
        reamur(int atau float): nilai reamur

    Return:
        (float atau int): hasil dari kalkulasi celcius ke reamur
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(reamur, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return reamur * (5 / 4)


def celcius_kelvin(celcius: Union[int, float]) -> Union[int, float]:
    """
    mengubah nilai celcius ke reaumur

    Parameter:
        celcius(int atau float): nilai celcius

    Return:
        (float atau int): hasil dari kalkulasi celcius ke kelvin
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(celcius, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return celcius + 273.15


def kelvin_celcius(kelvin: Union[int, float]) -> Union[int, float, error.Error]:
    """
    mengubah celcius ke kelvin

    Parameter:
        kelvin(int atau float): nilai kelvin

    Return:
        (float atau int): hasil dari kalkulasi kelvin ke celcius
        error.ErrorTiperData: error jika data salah
        erro.Error: error jika nilai kelvin kurang dari nol
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(kelvin, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    elif kelvin < 0:
        return error.Error("Nilai kelvin tidak boleh kurang dari 0")
    else:
        return 273.15 - kelvin


def kelvin_fahrenheit(kelvin: Union[int, float]) -> Union[int, float, error.Error]:
    """
    mengubah kelvin ke fahrenheit

    Parameter:
        kelvin(int atau float): nilai kelvin

    Return:
        (float atau int): hasil dari kalkulasi kelvin ke fahrenheit
        error.ErrorTiperData: error jika data salah
        errot.Error ; error jika nilai kelvin kurang dari nol
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(kelvin, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    elif kelvin < 0:
        return error.Error("Kelvin tidak boleh kurang dari 0")
    else:
        return kelvin * (9 / 5) - 459.67


def fahrenheit_kelvin(fahrenheit: Union[int, float]) -> Union[int, float]:
    """
    mengubah fahrenheit ke kelvin

    Parameter:
        fahrenheit(int atau float): nilai fahrenheit

    Return:
        (float atau int): hasil dari kalkulasi fahrenheit ke kelvin
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(fahrenheit, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (fahrenheit + 459.67) * (5 / 9)


def kelvin_reamur(kelvin: Union[int, float]) -> Union[int, float, error.Error]:
    """
    mengubah kelvin ke reamur

    Parameter:
        kelvin(int atau float): nilai kelvin

    Return:
        (float atau int): hasil dari kalkulasi kelvin ke reamur
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(kelvin, (float, int)):
        return error.ErrorTipeData(["int", "float"])
    elif kelvin < 0:
        return error.Error("Kelvin tidak boleh kurang dari 0")
    else:
        return (kelvin - 273.15) * (4 / 5)


def reamur_kelvin(reamur: Union[int, float]) -> Union[int, float]:
    """
    mengubah reamur ke kelvin

    Parameter:
        reamur(int atau float): nilai reamur

    Return:
        (float atau int): hasil dari kalkulasi reamur ke kelvin
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(reamur, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (reamur * (5 / 4)) + 273.15


def reamur_fahrenheit(reamur: Union[int, float]) -> Union[int, float]:
    """
    mengubah reamur ke fahrenheit

    Parameter:
        reamur(int atau float): nilai reamur

    Return:
        (float atau int): hasil dari kalkulasi reamur ke fahrenheit
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(reamur, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (reamur * (9 / 4)) + 32


def fahrenheit_reamur(fahrenheit: Union[int, float]) -> Union[int, float]:
    """
    mengubah fahrenheit ke reamur

    Parameter:
        fahrenheit(int atau float): nilai fahrenheit

    Return:
        (float atau int): hasil dari kalkulasi fahrenheit ke reamur
        errot.ErrorTiperData: error jika data salah
    """
    # mengecek apakah variable tersebut bertipe data int atau float
    # jika tidak maka error
    if not isinstance(fahrenheit, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    else:
        return (fahrenheit - 32) * (4 / 9)
