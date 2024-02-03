# Website OpenSeries

Selamat datang di repositori OpenSeries! Repositori ini berisi kode sumber untuk website OpenSeries. Kami menggunakan runtime dan package manager dari Bun, jadi jika Anda ingin berkontribusi, pastikan untuk menginstal Bun terlebih dahulu dengan mengacu pada dokumentasi resmi di [https://bun.sh/](https://bun.sh/).

## Memulai

Untuk berkontribusi pada website OpenSeries, ikuti langkah-langkah berikut:

1. **Clone Repositori:**

    ```bash
    git clone https://github.com/username-anda/openseries-website.git
    ```

2. **Instal Dependencies:**

    ```bash
    bun install
    ```

3. **Jalankan Proyek:**

    ```bash
    bun dev
    ```

    Perintah ini akan memulai server pengembangan, dan Anda dapat melihat website di [http://localhost:3000](http://localhost:3000).

4. **Sebelum Commit:**

    - Jalankan pemeriksaan linting:

        ```bash
        bun lint
        ```

    - Jalankan prettier untuk pemformatan kode:
        ```bash
        bun prettier
        ```

    Pastikan kode Anda sesuai dengan standar kami.

5. **Pesan Commit:**
   Gunakan awalan berikut dalam pesan commit Anda:

    - `feat`: untuk fitur baru
    - `fix`: untuk perbaikan bug
    - `docs`: untuk pembaruan dokumentasi
    - `add`: untuk menambahkan file atau komponen baru

    Contoh:

    ```bash
    git commit -m "feat: menambahkan fitur baru ke halaman utama"
    ```

## Kontributor

Terima kasih kepada semua kontributor yang telah membantu meningkatkan website OpenSeries! Jika Anda tertarik berkontribusi, silakan fork repositori ini dan kirim pull request ke branch `develop`.

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](LICENSE).
