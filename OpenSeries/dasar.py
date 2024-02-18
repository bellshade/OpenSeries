import OpenSeries.util.error as error
import numpy as np
from typing import Union
import math


def bulat(
    angka: Union[int, float], cek: bool = False
) -> Union[int, bool, error.ErrorTipeData]:
    """
    membuat fungsi untuk membulatkan angka

    Parameter:
        angka (int atau float): angka yang akan dibulatkan

    Return:
        int: hasil angka yang sudah dibulatkan
        bool: jika di set true maka akan mengecek sebuah angka
        error.ErrorTipeData: error jika tipe data tidak sesuai
    """
    if not isinstance(angka, (int, float)):
        return error.ErrorTipeData(["int", "float"])
    if cek is True:
        return int(angka) if angka - int(angka) >= 0 else int(angka) - 1
    else:
        return math.ceil(angka)


def akar(
    value: Union[int, float], iterasi: int = 4
) -> Union[float, error.ErrorTipeData]:
    """
    apromasi nilai akar pada angka
    Args:
        value (Union[int,float]): input nilai
        iterasi (Optional[int]): mengsetup iterasi apporamasi. Defaults to 4.

    Returns:
        float: output dari angka yang telah di prediksi
        error.ErrorTipeData: error jika data yang dimasukkan salah
    """

    # ngecheck tipe data pada value
    if not isinstance(value, (int, float)):
        raise error.ErrorTipeData(["int", "float"])
    # ngecheck tipe data pada iterasi
    if not isinstance(iterasi, int):
        raise error.ErrorTipeData(["int"])
    result = value
    for _ in range(iterasi + 1):
        result = (result + (value / result)) / 2
    return round(result, 2)


def tan_hiperbolik(x: np.ndarray) -> Union[np.ndarray, error.ErrorTipeData]:
    """
    fungsi tangen hiperbolik

    Parameter:
        x (np.ndarray): nilai input yang ingin dikalkulasikan

    Return:
        np.ndarray: hasil dari kalkulasi tangen hiperbolik
        error.ErrorTipeData: error jika tipe data yang diberikan salah
    """
    if not isinstance(x, np.ndarray):
        return error.ErrorTipeData(["numpy.ndarray"])
    return (2 / (1 + np.exp(-2 * x))) - 1


def volume_kubus(
    panjang_sisi: Union[float, int],
) -> Union[float, int, error.ErrorTipeData, error.Error]:
    """
    menghitung volume kubus

    Parameter:
        panjang_sisi (int atau float): sisi yang akan dihitung

    return:
        float atau int: hasil dari perhitungan
        ErrorTipeData: error jika diberikan tipe data yang salah
        Error: error jika nilai yang diberikan negatif
    """
    if not isinstance(panjang_sisi, (float, int)):
        return error.ErrorTipeData(["float", "int"])
    if panjang_sisi < 0:
        return error.Error("panjang_sisi hanya menerima nilai positif")
    return pow(panjang_sisi, 3)
