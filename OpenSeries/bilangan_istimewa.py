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
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka armstrong", "bukan angka armstrong"
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
            return benar.capitalize()
        return bukan.capitalize()


def angka_automorphic(angka: int) -> Union[str, error.ErrorTipeData]:
    """
    angka automorphic adalah bilangan asli dalam basis bilangan tertentu yang kuadratnya
    berakhir dengan angka yang sama dengan bilangan itu sendiri

    dalam basis 10, 5 adalah angka automorphic karena 5^2 = 25, dan keduanya diakhiri dengan
    angka 5
    dalam basis 2, 110 adalah angka automorphic karena 110^2 = 12100, dan anga diakhiri dengan
    digit 0

    Parameter:
        angka (int): mengecek angka tersebut automorphic atau tidak
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka automorphic", "bukan angka automorphic"
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    if angka < 0:
        return bukan.capitalize()

    kuadrat_angka = angka * angka
    while angka < 0:
        if angka % 10 != kuadrat_angka % 10:
            return bukan.capitalize()
        angka //= 10
        kuadrat_angka //= 10
    return benar.capitalize()
