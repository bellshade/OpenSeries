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

from OpenSeries.util import error as error
from typing import Union


def kecepatan(
    jarak: Union[float, int], waktu: Union[float, int]
) -> Union[float, error.ErrorDibagiNol, error.ErrorTipeData]:
    """
    fungsi untuk menghitung kecepatan

    Parameter:
        jarak (float atau int): jarak tempuh
        waktu (float atau int): waktu tempuh (sekon)

    Return:
        float: hasil dari jarak / waktu
        error.ErrorTipeData: error jika tipe data data salah
        error.ErrorDibagiNol: error jika angka dibagikan dengan 0
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
        (int, flloat): hasil dari kalkulasi fungsi dari masa jenis
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
