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
