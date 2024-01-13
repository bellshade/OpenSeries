Kami sangat senang anda telah ikut berkontribusi dalam implementasi algortima, struktur data, atau memperbaiki *error*.
Semua boleh ikut berkontribusi sekecil apapun dengan pengecualian sebagai berikut:

- Hasil pekerjaan kamu adalah buatan kamu sendiri dan tidak ada hak cipta dari orang lain. Jika kami menemukan kesamaan, maka tidak kami *merge*.
- Hasil kerja kamu akan berlisensi [MIT](LICENSE) ketika *pull request* kamu sudah di-*merge*.
- Hasil kerja kamu wajib mengikuti standar dan *style* koding dari kami.
- Hanya menerima *file* dengan ekstensi ``*.py``, selain itu dibuat pengecualian dengan menjelaskan secara detail.

# Docstrings

**Penggunaan *docstring***

Penggunaan *docstring* bertujuan untuk memudahkan pembaca membaca dan mengimplementasikan algoritma.

***Docstring* yang baik:**

```py
def adding(num1, num2):
    """
    menambahkan kedua bilangan
    num1 dan num2 dan dikembalikan hasilnya
    num1 = integer
    num2 = integer
    mengembalikan hasil yang berupa integer
    >>> adding(2, 50)
    52
    >>> adding(3, 2)
    5
    """
    return num1 + num2
```

***Docstring* yang kurang baik:**

```py
def adding(num1, num2):
    """
    num1 + num2
    """
    return num1 + num2
```

**Saran penggunaan *docstring* yang baik untuk *doctest*:**

```py
def adding(num1, num2):
  """
  menambahkan kedua bilangan
  num1 dan num2 dan dikembalikan hasilnya
  num1 = integer
  num2 = integer
  mengembalikan hasil yang berupa integer
  >>> adding(2, 3)
  5
  >>> adding(4, 2)
  6
  """
  return num1 + num2
```

**Testing**

Untuk *lint testing*, kami menyarankan kamu untuk melakukan tes lokal dengan ``flake8``:

```bash
pytest . --verbose
```

***Pull request* yang baik**

Informasi: gunakan [*issue*](https://github.com/bellshade/Python/issues) apabila ingin menambahkan kode atau implementasi algoritma, dll (*basic*) agar tidak ada konflik dengan *pull request* lainnya. Kamu juga bisa menggunakan issue jika kamu ada 
kendala atau masalah ketika melakukan pull request. Kamu juga bisa bertanya pada forum discord **WPU** dan **Kelas Terbuka** perihal bellshade.

- Lakukan penjelasan deskripsi perubahan yang anda lakukan pada repositori kami dengan membuat penjelasan di [*issue*](https://github.com/bellshade/OpenSeries/issues).
- Setelah menjelaskan perubahan anda di [*issue*](https://github.com/bellshade/OpenSeries/issues) kemudian lakukan *fork* pada repositori kami.
- Setelah melakukan *fork*, anda dibebaskan untuk mengubah atau menambah algoritma.
  - Untuk *pull request* merubah atau memperbaiki, diusahakan kamu menerapkan algoritma yang lebih baik dan lebih mudah serta memeberikan penjelasan lebih detail alasan dari perubahaan tersebut lebih baik dari sebelumnya.
- Lakukan tes dengan menggunakan ``pytest`` secara lokal.
- Setelah merubah-rubah atau menambahkan algoritma serta melakukan tes lokal kode kamu, usahakan kamu membuat *local branch* baru:
  ```bash
  git checkout -b <branch_name>
  git add . # atau git add nama_perubahan_kamu.py
  git commit -m "feat: menambahkan algoritma terbaru"
  ```
- Lakukan *push* ke *branch* kamu dan kemudian *open pull request*.

**Saran pesan commit**

- `feat:` untuk menambah algoritma atau tambahan lainnya;
- `fix:` untuk mengubah algoritma yang sudah ada atau memperbaiki;
- `docs:` untuk mengubah atau membuat dokumentasi;
- `add:` untuk menambah algoritma atau tambahan lainnya (opsional);

Catatan: pesan commit harus menjelaskan perubahan secara singkat.

Contoh yang benar:
- &#9746; feat: test_x.py
- &#9745; feat: tambah unittest untuk algoritma x

Lebih lengkapnya bisa dilihat di:
- [EN](https://www.conventionalcommits.org/en/v1.0.0/)
- [ID](https://www.conventionalcommits.org/id/v1.0.0/)

Pull request akan di-*merge* jika:

- mengikuti standar dan arahan dari `CONTRIBUTING.md`;
- lulus tes dan cek dari beberapa tes yang sudah kami siapkan.
