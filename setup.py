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

from setuptools import setup, find_packages
from os import path
import io
import platform
import OpenSeries.util.constant as constant

# membuka file README
with open("README.md") as file_readme:
    readme = file_readme.read()

# buat installasi requirement dari requirements agar auto install
info = path.abspath(path.dirname(__file__))
with io.open(path.join(info, "requirements.txt"), encoding="utf-8") as file:
    core_require = file.read().split("\n")
    if platform.system == "windows":
        core_require.append("pywin32")


install_require = [x.strip() for x in core_require if "git+" not in x]

# setup nama project
setup(
    # nama dari project
    name=f"{constant.NAMA_PROJECT}",
    # versi dari project
    version=f"{constant.VERSI_LIBRARY}",
    # deskripsi singkat dari project
    description=f"{constant.DESCRIPTION}",
    # deskripsi detail tentang project
    long_description=str(readme),
    # url atau sumber dari projek
    url=f"{constant.WEBSITE}",
    # maintainer, developer yang membuat dari project
    author=", ".join(constant.AUTHOR),
    packages=find_packages(),
    # jika ada folder tambahan dari project ditambahkan dalam dictionary
    package_data={"OpenSeries": ["util/*"]},
    # minimum python yang dibutuhkan untuk menginstall dari project ini
    python_requires=">=3.10",
    # mengklasifikasi project dari OpenSeries
    classifiers=[
        "Intended Audience :: Developers",
        f"License :: OSI Approved :: {constant.OPENSERIES_BELLSHADE_LISENSI} License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    # fungsi untuk menginstall package tambahan dari requirements
    install_requires=install_require,
    # lisensi dari project
    license=f"{constant.OPENSERIES_BELLSHADE_LISENSI} License",
    project_urls={
        "Bug Reports": f"{constant.OPENSERIES_BELLSHADE_LISENSI}",
        "Source": f"{constant.WEBSITE}",
    },
)
