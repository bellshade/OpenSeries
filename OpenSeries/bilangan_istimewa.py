import OpenSeries.util.error as error
from typing import Union


def angka_armstrong(angka: int) -> Union[str, error.ErrorTipeData]:
    """
    angka armstrong adalah bilangan bulat positif yang sama dengan jumlah
    pangkat tiga dari digit-digitnya

    contoh:
    153 = 1^3 + 5^3 + 3^3 = 153

    Parameter:
        angka(int): angka yang akan di cek
    """
    # cek tipe data dari variable angka
    if isinstance(angka, (float, str)):
        return error.ErrorTipeData(["int"])
    else:
        total = 0
        number_of_digit = 0
        temp = angka

        number_of_digit = len(str(angka))
        temp = angka
        while temp > 0:
            rem = temp % 10
            total += rem**number_of_digit
            temp //= 10
        if angka == total:
            return "Angka armstrong"
        return "Bukan Angka armstrong"
