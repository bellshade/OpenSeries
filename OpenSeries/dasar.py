import OpenSeries.util.error as error
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
