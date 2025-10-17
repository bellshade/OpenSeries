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

from abc import ABC
from typing import Optional, Union


# mocking modul warna jika error import
try:
    from util import constant as warna
except ImportError:
    # mocking object jika module warna tidak tersedia
    class MockWarna:
        """mock class untuk warna jika modul gagal import"""

        red: str = ""
        reset_warna: str = ""

    warna = MockWarna()


class BaseError(Exception, ABC):
    def __init__(self, message: str, error_code: Optional[str] = None):
        """
        inisialisasi base exception

        Args:
            message (str): pesan error yang akan ditampilkan
            error_code (str): kode error opsional untuk identifikasi programatik
        """
        self.error_code = error_code
        super().__init__(message)

    def __str__(self) -> str:
        return self.args[0] if self.args else ""


class ErrorTipeData(BaseError, TypeError):
    """
    Kelas untuk mendeteksi error dari tipe data

    Parameter:
        expected_types (list[str]): tipe data yang dimasukkan

    Return:
        (str): pesan error tipe data sesuai dari inputan
    """

    def __init__(
        self,
        tipe_diharapkan: list[str],
        tipe_sebenarnya: Optional[str] = None,
        nama_parameter: Optional[str] = None,
    ):
        self._validate_input(tipe_diharapkan)
        self.tipe_diharapkan = tipe_diharapkan
        self.tipe_sebenarnya = tipe_sebenarnya
        self.nama_parameter = nama_parameter

        # membuat pesan error dengan memanggil method format_tipe_data
        message = self._format_message()
        super().__init__(message, error_code="TYPE_ERROR")

    def _validate_input(self, expected_types: list[str]) -> None:
        if not isinstance(expected_types, list):
            raise TypeError("expected_types harus berrupa list")
        if not expected_types:
            raise ValueError("tipe data dalam list tidak boleh kosong")
        if not all(isinstance(data, str) for data in expected_types):
            raise TypeError("semua element dalam expected_types harus string")

    def _format_message(self) -> str:
        tipe_str = " atau ".join(self.tipe_diharapkan)
        base_message = f"tipe data harus {tipe_str}"

        if self.nama_parameter:
            base_message = f"parameter `{self.nama_parameter}` {base_message}"

        if self.tipe_sebenarnya:
            base_message += f" (diterima: {self.tipe_sebenarnya})"

        return f"{warna.red}Error Tipe data:{warna.reset_warna}"


class Error(BaseError):
    """
    Kelas untuk membuat kostumisasi error

    Parameter:
        pesan (str): pesan kostum yang ingin dimasukkan
    """

    def __init__(self, pesan: str, error_code: Optional[str] = None) -> None:
        if not isinstance(pesan, str):
            raise TypeError("pesan harus berupa string")
        formatted_message = f"{warna.red}Error:{warna.reset_warna} {pesan}"
        super().__init__(formatted_message, error_code=error_code)


class IndeksError(BaseError, IndexError):
    """
    kelas untuk membuat error dari index jika tidak selaras dengan dimensi atau lain

    Parameter:
        pesan(str): pesan error dari indeks yang harus dimasukkan
    """

    def __init__(
        self, pesan: str, index: Optional[int] = None, max_index: Optional[int] = None
    ):
        if not isinstance(pesan, str):
            raise TypeError("pesan harus berupa string")

        self.index = index
        self.max_index = max_index

        detailed_message = pesan

        if index is not None:
            detailed_message += f" (indeks: {index})"
        if max_index is not None:
            detailed_message += f" (maksimum: {max_index})"

        formatted_message = (
            f"{warna.red}Indeks Error:{warna.reset_warna} {detailed_message}"
        )
        super().__init__(formatted_message, error_code="INDEX_ERROR")


class ErrorValue(BaseError, ValueError):
    """
    kelas untuk membuat error dari index dengan throw dari ValueError

    Parameter:
        pesan(str): pesan error dari value yang salah
    """

    def __init__(
        self, pesan: str, invalid_value: Optional[Union[str, int, float]] = None
    ):
        if not isinstance(pesan, str):
            raise TypeError("pesan harus string")
        self.invalid_value = invalid_value

        detailed_message = pesan
        if invalid_value is not None:
            detailed_message += f" (nilai tidak valid: {invalid_value})"

        formatted_message = (
            f"{warna.red}Error Value:{warna.reset_warna} {detailed_message}"
        )
        super().__init__(formatted_message, error_code="VALUE_ERROR")


class ErrorDibagiNol(BaseError, ZeroDivisionError):
    """
    Kelas untuk menampilkan error yang tidak bisa dibagi dengan nol
    """

    def __init__(self, operasi: Optional[str] = None, dividend: Optional[float] = None):
        self.operasi = operasi
        self.dividend = dividend

        base_message = "Tidal bisa dibagi dengan nol"
        if operasi:
            base_message += f" dalam operasi {operasi}"
        if dividend is not None:
            base_message += f" (pembilang: {dividend})"

        formatted_message = (
            f"{warna.red}Error dibagi nol:{warna.reset_warna} {base_message}"
        )
        super().__init__(formatted_message, error_code="ZERO_DIVISION_ERROR")
