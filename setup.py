from setuptools import setup, find_packages
from os import path
import io
import platform

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
    name="OpenSeries",
    # versi dari project
    version="1.6.6",
    # deskripsi singkat dari project
    description="library untuk membantu temen-temen SMA/SMK/Sederajat",
    # deskripsi detail tentang project
    long_description=str(readme),
    # url atau sumber dari projek
    url="https://github.com/bellshade/OpenSeries",
    # maintainer, developer yang membuat dari project
    author="bellshade, wpu, kelas terbuka",
    packages=find_packages(),
    # jika ada folder tambahan dari project ditambahkan dalam dictionary
    package_data={"OpenSeries": ["util/*"]},
    # minimum python yang dibutuhkan untuk menginstall dari project ini
    python_requires=">=3.10",
    # mengklasifikasi project dari OpenSeries
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    # fungsi untuk menginstall package tambahan dari requirements
    install_requires=install_require,
    # lisensi dari project
    license="MIT License",
    project_urls={
        "Bug Reports": "https://github.com/bellshade/OpenSeries/issues",
        "Source": "https://github.com/bellshade/OpenSeries",
    },
)
