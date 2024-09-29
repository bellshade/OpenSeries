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

from OpenSeries.util import error
from typing import Union


class Validasi:
    """
    Kelas untuk memvalidasi nilai dari yang diberikan. nilai tersebut akan di proses
    di method dalam kelas dan throw error jika tipe data yang nantinya diberikan tidak
    sesuai, jika benar akan dikonversikan
    """

    def __init__(self, tipe_data):
        self.tipe_data = tipe_data

    def validasi_nilai_float(self) -> float:
        """
        Validasi nilai dan konversi ke float

        Parameter:
            nilai (float): nilai yang akan di konversi
        """
        if not isinstance(self.tipe_data, float):
            raise error.ErrorTipeData(["float"])
        return float(self.tipe_data)

    def validasi_nilai_int(self) -> int:
        """
        Validasi nilai dan konversi ke integer

        Throw:
            error.ErrorTipeData: jika tipe data tidak sesuai
        """
        if not isinstance(self.tipe_data, int):
            raise error.ErrorTipeData(["int"])
        return int(self.tipe_data)

    def validasi_nilai_int_float(self) -> Union[float, int]:
        """
        Validasi nilai dan konversi ke integer atau float
        """
        if not isinstance(self.tipe_data, (float, int)):
            raise error.ErrorTipeData(["int, float"])
        return self.tipe_data

    def validasi_nilai_list_integer(self) -> list[int]:
        """
        Validasi nilai dan konversi ke list dengan elemen tipe data
        integer

        Throw:
            error.ErrorTipeData: jika tipe data tidak sesuai
        """
        if not isinstance(self.tipe_data, list):
            raise error.ErrorTipeData(["list[int]"])
        for indeks, nilai_element in enumerate(self.tipe_data):
            if not isinstance(nilai_element, int):
                raise error.ErrorTipeData(
                    [f"list[int] elemen indeks ke: {indeks}\nList: {self.tipe_data}"]
                )
        hasil: list[int] = [int(hasil_konversi) for hasil_konversi in self.tipe_data]
        return list(hasil)

    def validasi_nilai_list_float(self) -> list[float]:
        """
        Validasi nilai dan konversi ke list dengan elemen tipe data
        float

        Throw:
            error.ErrorTipeData: jika tipe data tidak sesuai
        """
        if not isinstance(self.tipe_data, list):
            raise error.ErrorTipeData(["list[int]"])
        for indeks, nilai_element in enumerate(self.tipe_data):
            if not isinstance(nilai_element, float):
                raise error.ErrorTipeData(
                    [f"list[int] elemen indeks ke: {indeks}\nList: {self.tipe_data}"]
                )
        hasil: list[float] = [
            float(hasil_konversi) for hasil_konversi in self.tipe_data
        ]
        return list(hasil)

    def validasi_nilai_list_float_int(self) -> list[Union[float, int]]:
        """
        Validasi nilai dan konversi ke list dengan elemen tipe data
        float atau integer, (float, integer)

        Throw:
            error.ErrorTipeData: jika tipe data tidak sesuai
        """
        if not isinstance(self.tipe_data, list):
            raise error.ErrorTipeData(["list[float, int]"])
        for indeks, nilai_element in enumerate(self.tipe_data):
            if not isinstance(nilai_element, (float, int)):
                raise error.ErrorTipeData(
                    [
                        f"list[int, float] elemen indeks ke: {indeks}\nList: {self.tipe_data}"
                    ]
                )
        hasil: list[Union[float, int]] = [
            hasil_konversi for hasil_konversi in self.tipe_data
        ]
        return list(hasil)
