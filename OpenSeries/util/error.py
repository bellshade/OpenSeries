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

# kostum error
# file error.py berisi tentang kustomisasi error dengan beberapa tujuan antara lain:
# - mendeteksi error terkait tipe data
# - membuat error kustom dengan pesan tertentu
# - menangani error terkait indeks saat melakukan indexing pada struktur data
# - menangani error terkait dengan validasi dari values
# - menampilkan error saat mencoba dengan pembagian dengan error
from OpenSeries.util import constant as warna


class ErrorTipeData(TypeError):
    """
    Kelas untuk mendeteksi error dari tipe data

    Parameter:
        expected_types (list[str]): tipe data yang dimasukkan

    Return:
        (str): pesan error tipe data sesuai dari inputan
    """

    def __init__(self, expected_types: list[str]):
        # mengecek apakah list expected_types tidak kosong
        if not expected_types:
            raise ValueError("tipe data dalam list tidak boleh kosong")
        # mengecek apakah semua element di dalam expected_types adalah string
        if not all(isinstance(data, str) for data in expected_types):
            raise TypeError("element dari tipe data harus str (string)!")

        # membuat pesan error dengan memanggil method format_tipe_data
        tipe_str = " atau ".join(map(str, expected_types))
        super().__init__(
            f"{warna.red}Error Tipe Data:{warna.reset_warna} tipe data harus {tipe_str}"
        )


class Error(Exception):
    """
    Kelas untuk membuat kostumisasi error

    Parameter:
        pesan (str): pesan kostum yang ingin dimasukkan
    """

    def __init__(self, pesan: str):
        message = f"{warna.red}Error:{warna.reset_warna} {pesan}"
        super().__init__(message)


class IndeksError(IndexError):
    """
    kelas untuk membuat error dari index jika tidak selaras dengan dimensi atau lain

    Parameter:
        pesan(str): pesan error dari indeks yang harus dimasukkan
    """

    def __init__(self, pesan: str):
        message = f"{warna.red}Indeks Error:{warna.reset_warna} {pesan}"
        super().__init__(message)


class ErrorValue(ValueError):
    """
    kelas untuk membuat error dari index dengan throw dari ValueError

    Parameter:
        pesan(str): pesan error dari value yang salah
    """

    def __init__(self, pesan: str):
        message = f"{warna.red}Error Value:{warna.reset_warna} {pesan}"
        super().__init__(message)


class ErrorDibagiNol(ZeroDivisionError):
    """
    Kelas untuk menampilkan error yang tidak bisa dibagi dengan nol
    """

    def __init__(self):
        super().__init__(
            f"{warna.red}Error Dibagi Nol:{warna.reset_warna} Tidak bisa dibagi dengan nol"
        )
