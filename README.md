# OpenSeries

![banner](.github/openSeries.png)

![codequality](https://img.shields.io/codacy/grade/06ba6d6d345f4c15bf8e5cc3eac19d4d?style=flat-square&logo=codacy)
![build badge](https://img.shields.io/github/actions/workflow/status/bellshade/OpenSeries/pythontesting.yml?style=flat-square&logo=github&label=Build%20(%20Linux%2C%20Windows%2C%20MacOS))

Project Untuk Menghitung Segala Jenis Persamaan atau Rumus-Rumus yang terdapat pada bangku sekolah (SMA/SMK/Sederajat).
Project ini bertujuan untuk memudahkan siswa dalam menghitung persamaan atau problem-problem yang terdapat pada pelajaran sekolah (cheat egine untuk Sekolah).

**menghitung nilai probabilitas dari suatu kejadian**

```python
import OpenSeries.matematika as matematika

nilai_A = 4
nilai_S = 20

print("menghitung probabilitas suatu kejadian")
print(f"dengan jumlah hasil yang menguntungkan :{nilai_A}")
print(f"dan dengan ukuran ruang sampel {nilai_S}")
print(
    f"probabilitas dari kejadiannya adalah: {matematika.peluang_kejadian(nilai_A, nilai_S)}\n"
)
```

## Requirements

Untuk Menjalankan Library ini, kamu harus Memiliki Python dengan versi: 3.11.6 hingga 3.12.

## Installasi

kamu bisa menginstall package `OpenSeries` via pip dengan cara

```bash
pip install git+https://github.com/bellshade/OpenSeries
```
