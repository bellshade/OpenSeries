Kami sangat berterima kasih karena telah ikut berkontribusi dalam proyek `OpenSeries`, Semua boleh ikut berkontribusi sekecil apapun dengan pengecualian sebagai berikut:

- Hasil pekerjaan kamu adalah buatan kamu sendiri dan tidak ada hak cipta dari orang lain. Jika kami menemukan kesamaan, maka tidak kami _merge_.
- Hasil kerja kamu akan berlisensi [MIT](LICENSE) ketika _pull request_ kamu sudah di-_merge_.
- Hasil kerja kamu wajib mengikuti standar dan _style_ koding dari kami.
- Hanya menerima _file_ dengan ekstensi `*.py`, selain itu dibuat pengecualian dengan menjelaskan secara detail.

# Docstrings

**Penggunaan _docstring_**

Penggunaan _docstring_ bertujuan untuk memudahkan pembaca membaca dan mengimplementasikan algoritma. docstring harus memiliki (minimal) penjelasan dari fungsi hingga penjelasan dari parameter dari fungsi tersebut.

**_Docstring_ yang baik:**

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

**_Docstring_ yang kurang baik:**

```py
def adding(num1, num2):
    """
    num1 + num2
    """
    return num1 + num2
```

**Saran penggunaan _docstring_ yang baik untuk _doctest_:**

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

kemudian testing kode python dengan pytest dan pre-commit

install terlebih dahulu dari library pre-commit

```bash
pip install pre-commit
```

jika ada kendala berupa

```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try 'apt-get or pacman -S yum dnf xbps', where xyz is the package you are trying to
    install.

    If you wish to install a non-OS-packaged Python package,
    create a virtual environment using 'python -m venv path/to/venv'.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip.

    If you wish to install a non-OS packaged Python application,
    it may be easiest to use 'pipx install xyz', which will manage a
    virtual environment for you. Make sure you have python-pipx
    installed via pacman.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

kamu bisa menginstallnya dengan cara

```bash
pip install pre-commit --break-system-packages
```

kemudian lakukan installasi dari pre-commit deangan cara

```bash
pre-commit install
```

kemudian jalankan perintah

```bash
pre-commit run --all-files
```

jika sukses, lakukan testing kode dengan perintah

```bash
pytest . --verbose
```

**_Pull request_ yang baik**

Informasi: gunakan [_issue_](https://github.com/bellshade/Python/issues) apabila ingin menambahkan kode atau implementasi algoritma, dll (_basic_) agar tidak ada konflik dengan _pull request_ lainnya. Kamu juga bisa menggunakan issue jika kamu ada
kendala atau masalah ketika melakukan pull request. Kamu juga bisa bertanya pada forum discord **WPU** dan **Kelas Terbuka** perihal bellshade.

- Lakukan penjelasan deskripsi perubahan yang anda lakukan pada repositori kami dengan membuat penjelasan di [_issue_](https://github.com/bellshade/OpenSeries/issues).
- Setelah menjelaskan perubahan anda di [_issue_](https://github.com/bellshade/OpenSeries/issues) kemudian lakukan _fork_ pada repositori kami.
- Setelah melakukan _fork_, anda dibebaskan untuk mengubah atau menambah algoritma.
  - Untuk _pull request_ merubah atau memperbaiki, diusahakan kamu menerapkan algoritma yang lebih baik dan lebih mudah serta memeberikan penjelasan lebih detail alasan dari perubahaan tersebut lebih baik dari sebelumnya.
- Lakukan tes dengan menggunakan `pytest` secara lokal.
- Setelah merubah-rubah atau menambahkan algoritma serta melakukan tes lokal kode kamu, usahakan kamu membuat _local branch_ baru:
  ```bash
  git checkout -b <branch_name>
  git add . # atau git add nama_perubahan_kamu.py
  git commit -m "feat: menambahkan algoritma terbaru"
  ```
- Lakukan _push_ ke _branch_ kamu dan kemudian _open pull request_.

> [!IMPORTANT]
> Lakukan pull request ke branch ``develop-library`` jika ingin pull request library dan ``develop`` untuk pull request ke web dari  OpenSeries.

> [!CAUTION]
> Pull request akan di close jika mengarah ke branch ``main`` atau ``web``.

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

Pull request akan di-_merge_ jika:

- mengikuti standar dan arahan dari `CONTRIBUTING.md`;
- lulus tes dan cek dari beberapa tes yang sudah kami siapkan.

