def error_tipe_data(error_data: list[str]) -> str:
    """
    fungsi panggilan untuk menampilkan pesan error

    Parameter:
        error_data (list(str)): tipe data yang ingin diisi
    """
    return f"kamu memasukkan tipe data yang salah, harus {','.join(error_data)}"
