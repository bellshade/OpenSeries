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

from colorama import Fore, Style

# nilai constant untuk bellshade
VERSI_LIBRARY = "1.9.2"
OPENSERIES_BELLSHADE_LISENSI = "MIT"
NAMA_PROJECT = "OpenSeries"
DESCRIPTION = "Library untuk membantu siswa SMA / SMK / Sederajat"
AUTHOR = ["bellshade", "wpu", "warga slowy"]
WEBSITE = "https://github.com/bellshade/OpenSeries"
ISSUE_WEBSITE = "https://github.com/bellshade/OpenSeries/issues"

# bilangan pi adalah nilai konstant dalam matematika yang merupakan perbandingan keliling
# lingkaran dengan diameternya
PI: float = 3.14159265358979323846

# bilangan euler adalah nilai konstant yang dimana nilai kira-kiranya sama dengan 2.71828
# dan dikarakterisasi dalam berbagai cara
BILANGAN_EULER: float = 2.718281828459045235360

# variable ini juga mewakili dari konstanta planck, tetapi dinyatan dalam satuan
# elektron volt per detik (eV/s) nilainya adalah 4.1357 × 10⁻¹⁵ eV s⁻¹
KONSTANTA_PLANCK: float = 4.1357 * pow(10, -15)

# default error dari warna menggunakan kode ANSI escape
# merah
red: str = Fore.RED
# reset kembali warna ke default
reset_warna: str = Style.RESET_ALL
