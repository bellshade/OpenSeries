def error_tipe_data(error_data: list[str]) -> str:
    """
    fungsi panggilan untuk menampilkan pesan error

    Parameter:
        error_data (list(str)): tipe data yang ingin diisi
    """
    return f"Kamu memasukkan tipe data yang salah, harus {','.join(error_data)}"


def error_format(format_string: str) -> str:
    """
    fungsi untuk menampilkan format error
    sesuai keinginan dari pesan error

    parameter:
        format_string (str): pesan yang akan diisi
    """
    return "Error: " + format_string


def error_dibagi_nol():
    """
    fungsi panggilan untuk menampilkan pesan error
    pesan error berupa `tidak bisa dibagikan dengan 0
    """
    return "Tidak bisa dibagikan dengan 0"
