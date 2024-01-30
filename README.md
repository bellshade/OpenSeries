# OpenSeries

![banner](.github/openSeries.png)

![codequality](https://img.shields.io/codacy/grade/06ba6d6d345f4c15bf8e5cc3eac19d4d?style=flat-square&logo=codacy)
![build badge](https://img.shields.io/github/actions/workflow/status/bellshade/OpenSeries/pythontesting.yml?style=flat-square&logo=github&label=Build%20(%20Linux%2C%20Windows%2C%20MacOS))

Project Untuk Menghitung Segala Jenis Persamaan atau Rumus-Rumus yang terdapat pada bangku sekolah (SMA/SMK/Sederajat) dan jenjang yang lebih lanjut.
Project ini bertujuan untuk memudahkan siswa dalam menghitung persamaan atau problem-problem yang terdapat pada pelajaran sekolah (cheat egine untuk hitung-menghitung).

**Menghitung nilai probabilitas dari suatu kejadian**

```python
import OpenSeries.matematika as matematika

nilai_a = 4
nilai_s = 20

print("menghitung probabilitas suatu kejadian")
print(f"dengan jumlah hasil yang menguntungkan :{nilai_a}")
print(f"dan dengan ukuran ruang sampel {nilai_s}")
print(
    f"probabilitas dari kejadiannya adalah: {matematika.peluang_kejadian(nilai_a, nilai_s)}\n"
)
```

## Requirements

Untuk Menjalankan Library ini, kamu harus Memiliki Python dengan versi: 3.11.6 hingga 3.12.

## Installasi

kamu bisa menginstall package `OpenSeries` via pip dengan cara

```bash
pip install OpenSeriesBellshade
```

## Docker
kamu juga bisa testing package via `docker`` dengan cara

```bash
bash docker.sh
```
> Note: untuk windows kalian bisa install dulu dockernya dengan panduan yang ada di [`Docker Docs`](https://docs.docker.com/desktop/install/windows-install/)

Informasi:

kamu bisa melihat pada [wiki](https://github.com/bellshade/OpenSeries/wiki) atau ke [website](openseries.pages.dev/), untuk dokumentasi installasi dan pengunaan dari `OpenSeries`

## 🤩 Ayo ikut kami dan berkontribusi! 🤩

Bantuan kalian diperlukan Agar Bellshade dapat lebih jauh lagi mengembangan Project ini, kita butuh tenaga kalian!

Kami sangat senang bilat kalian melakukan kontribusi project **OpenSeries** ini. Tapi, sebelum itu, silahkan baca terlebih dahulu [peraturan dan pedomannya](CONTRIBUTING.md) yang telah kami siapkan. Terima kasih

Untuk informasi lebih lanjut, mari gabung dalam komunitas [Discord Channel WPU](http://discord.gg/S4rrXQU) dan [Discord Channel Kelas Terbuka](https://discord.gg/eavqxxTU)
