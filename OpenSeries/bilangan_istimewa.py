import OpenSeries.util.error as error
from typing import Union
import numpy as np


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

    Return:
        str: mengembalikan informasi jika benar atau bukan
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka automorphic", "bukan angka automorphic"
    # cek dari tipe data angka
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


def angka_pronic(angka: int) -> Union[str, error.ErrorTipeData]:
    """
    angka pronic adalah bilangan bulat positif yang merupakan hasil perkalian
    dari dua bilangan bulat berurutan
    6 = 2 * (2 + 1) = 2 * 3 = 6
    12 = 3 * (3 + 1) = 3 * 4 = 12
    20 = 4 * (4 + 1) = 4 * 5 = 20

    Parameter:
        angka(int): angka yang akan di cek

    Return:
        str: mengembalikan informasi jika benar atau bukan
        error.ErrorTipeData: jika tipe data yang dimasukkan salah
    """
    benar, bukan = "angka pronic", "bukan angka pronic"
    # cek dari tipe data angka
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    if angka < 0 or angka % 2 == 1:
        return bukan.capitalize()
    angka_pangkat = int(angka**0.5)
    return (
        benar.capitalize()
        if angka == angka_pangkat * (angka_pangkat + 1)
        else bukan.capitalize()
    )


def angka_segitiga(angka: int) -> Union[int, error.ErrorTipeData, error.Error]:
    """
    bilangan segitiga adalah bilangan yang dapat disusun dalam bentuk segitiga sama sisi

    Parameter:
        angka (int): angka yang ingin dimasukkan

    Return:
        int: angka segitiga di posisi yang ditentukan
        error.Error: jika angka negatif
        error.ErrorTipeData: jika tipe data salah
    """
    # jika tipe data dari angka tidak integer
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    # jika value dari angka diisi nilai negatif
    if angka < 0:
        return error.Error("angka tidak boleh negatif")
    return angka * (angka + 1) // 2


def angka_polindrom(angka: int) -> Union[str, error.ErrorTipeData, error.Error]:
    """
    angka polindrom adalah angka yang jika di balik akan memiliki bentuk yang sama

    Parameter:
        angak(int): angka yang di masukkan

    Return:
        str : mengembalika informasi angka polindorm
        error.ErrorTipeData : error jika tipe data salah
        error.Error : jika angka yang dimasukkan negatif
    """
    benar, bukan = "angka polindrom", "bukan angka polindrom"
    if isinstance(angka, (int)):
        sisa = 0
        digit_angka = abs(angka)
        while digit_angka != 0:
            sisa = (sisa * 10) + (digit_angka % 10)
            digit_angka = digit_angka // 10
        if sisa == abs(angka):
            return benar.capitalize()
        return bukan.capitalize()
    if angka < 0:
        return error.Error("angka tidak boleh negatif")
    else:
        return error.ErrorTipeData(["int"])


def angka_prima(angka: int) -> Union[str, error.ErrorTipeData, error.Error]:
    """
    Angka Prima adalah angka yang habis di bagi oleh satu dan
    dirinya sendiri

    Parameter :
        angka(int) = angka yang akan di cek

    Return:
        str : mengembalikan informasi angka prima
        error.ErrorTipeData : error jika tipe data salah
        error.Error : error jika nilai negatif
    """
    benar, bukan = "angka prima", "bukan angka prima"
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    if angka < 0:
        return error.Error("angka tidak boleh negatif")
    else:
        if angka < 2:
            return bukan.capitalize()

        print_sieve = [True] * (angka + 1)
        print_sieve[0] = print_sieve[1] = False
        for x in range(2, int(np.sqrt(angka)) + 1):
            if print_sieve[x]:
                for k in range(x * x, angka + 1, x):
                    print_sieve[k] = False
        if print_sieve[angka]:
            return benar.capitalize()
        else:
            return bukan.capitalize()


def angka_kaprekar(angka: int) -> Union[str, error.ErrorTipeData, error.Error]:
    """
    angka kaprekar adalah angka yang bukan negatif,lalu di kuadratkan dan
    angka dibagi menjadi dua bagian lalu di jumlahkan adalah bilangan asli itu
    sendiri.
    99 = (99)^2 = 9801 = 98+01 = 99
    55 = (55)^2 = 3025 = 30+25 = 55
    45 = (45)^2 = 2025 = 20+25 = 45
    9 = 9^2 = 81 = 8+1 = 9
    Parameter:
        angka(int) : angka yang akan di cek

    Return:
        str : mengembalikan informasi angka kaprekar
        error.ErrorTipeData = error jika tipe data tidak sesuai
        error.Error = error jika angka negatif
    """
    benar, bukan = "angka kaprekar", "bukan angka kaprekar"
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    if angka < 0:
        return error.Error("Angka tidak boleh negatif")
    else:
        if angka == 1:
            return benar.capitalize()
        sq_angka = angka * angka
        cout_digit = 0
        while sq_angka != 0:
            cout_digit = cout_digit + 1
            sq_angka = sq_angka // 10
        sq_n = angka * angka
        r_digits = 0
        while r_digits < cout_digit:
            r_digits = r_digits + 1
            eq_parts = int(np.pow(10, r_digits))
            sum = sq_n // eq_parts + sq_n % eq_parts
            if sum == angka:
                return benar.capitalize()
        return bukan.capitalize()


def angka_tetrahedral(angka: int) -> Union[int, error.ErrorTipeData, error.Error]:
    """
    Angka tetrahedral adalah angka yang dapat disusun sebagai piramid
    dengan dasar segitiga dan tiga sisi.

    Parameter :
        angka(int) : Angka yang akan dikalkulasi
    Return :
        int : Hasil kalkulasi angka tetrahedral
        error.ErrorTipeData : error jika tipe data tidak sesuai
        error.Error : error jika nilai negatif
    """
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    if angka < 0:
        return error.Error("angka tidak boleh negatif")
    else:
        return (angka * (angka + 1) * (angka + 2)) // 6


def angka_pentatope(angka: int) -> Union[int, error.Error, error.ErrorTipeData]:
    """
    Angka Pentatope adalah angka yang menghitung jumlah titik yang bisa
    di bentuk piramida dalam skala 4 dimensi

    Parameter :
        angka(int) : angka yang akan dikalkulasi

        Return :
        int : Hasil kalkulasi angka pentatope
        error.ErrorTipeData : error jika tipe data tidak sesuai
        error.Error : error jika nilai negatif
    """
    if not isinstance(angka, int):
        return error.ErrorTipeData(["int"])
    if angka < 0:
        return error.Error("Angka tidak boleh negatif")
    else:
        return (angka * (angka + 1) * (angka + 2) * (angka + 3)) // 24
