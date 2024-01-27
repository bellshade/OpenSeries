from OpenSeries.util import constant as warna


class ErrorTipeData(TypeError):
    """
    kelas untuk mendeteksi error dari tipe data

    parameter:
        expected_types (list[str]): tipe data yang dimasukkan

    return:
        (str): pesan error tipe data sesuai dari inputan
    """

    def __init__(self, expected_types: list[str]):
        message = f"{warna.red}Error:{warna.reset_warna} tipe data Harus {' atau '.join(expected_types)}"
        super().__init__(message)


class Error(Exception):
    """
    kelas untuk membuat kostumisasi error

    parameter:
        pesan (str): pesan kostum yang ingin dimasukkan
    """

    def __init__(self, pesan: str):
        message = f"{warna.red}Error:{warna.reset_warna} {pesan}"
        super().__init__(message)


class ErrorDibagiNol(ZeroDivisionError):
    """
    kelas untuk menampilkan error yang tidak bisa dibagi dengan nol
    """

    def __init__(self):
        super().__init__(
            f"{warna.red}Error:{warna.reset_warna} Tidak bisa dibagi dengan nol"
        )
