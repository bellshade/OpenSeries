# Website OpenSeries

Selamat datang di repositori OpenSeries! Repositori ini berisi kode sumber untuk website OpenSeries. Kami menggunakan runtime dan package manager dari Bun, jadi jika Anda ingin berkontribusi, pastikan untuk menginstal Bun terlebih dahulu dengan mengacu pada dokumentasi resmi di https://bun.sh/.

## Memulai

Untuk berkontribusi pada website OpenSeries, ikuti langkah-langkah berikut:

1. Fork repositori ini di GitHub.

2. Clone repositori yang telah di-fork ke mesin lokal Anda:

    ```bash
    git clone https://github.com/nama-anda/OpenSeries.git
    ```

3. Pindah ke direktori proyek:

    ```bash
    cd OpenSeries
    ```

4. Pastikan branch Anda diatur ke `develop`:

    ```bash
    git checkout develop
    ```

5. Buat branch baru untuk fitur atau perbaikan bug:

    ```bash
    git checkout -b nama-fitur
    ```

## Alur Pengembangan

1. Instal paket yang diperlukan menggunakan Bun:

    ```bash
    bun install
    ```

2. Jalankan proyek menggunakan Bun:

    ```bash
    bun dev
    ```

3. Sebelum melakukan commit, jalankan linter Bun untuk memastikan kualitas kode:

    ```bash
    bun lint
    ```

4. Format kode menggunakan Bun Prettier:

    ```bash
    bun format
    ```

5. Lakukan commit perubahan Anda dengan menggunakan salah satu awalan pesan commit berikut:

    - `feat:` untuk fitur baru
    - `fix:` untuk perbaikan bug
    - `docs:` untuk perubahan dokumentasi
    - `add:` untuk menambahkan file atau aset

    Contoh commit:

    ```bash
    git commit -m "feat: menambahkan fitur baru"
    ```

## Pull Request

Setelah membuat perubahan, dorong branch ke fork Anda di GitHub dan buat pull request yang dituju ke branch develop repositori ini.

## Kontributor

Terima kasih kepada semua kontributor yang telah membantu meningkatkan website OpenSeries! Jika Anda tertarik berkontribusi, silakan fork repositori ini dan kirim pull request ke branch develop.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.
