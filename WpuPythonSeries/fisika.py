def kecepatan(jarak: float | int, waktu: float | int) -> float:
    """
    fungsi untuk menghitung kecepatan

    Parameter:
    jarak (float atau int): jarak tempuh
    waktu (float atau int): waktu tempuh (sekon)

    Return:
    float: hasil dari jarak / waktu
    """
    return jarak / waktu


def percepatan(kecepatan: float | int, waktu: float | int) -> float:
    """
    fungsi untuk menghitung percepatan

    parameter:
    kecepatan (float atau int): kecepatan (m/s)
    waktu (float atau int): waktu tempuh (sekon)

    Return:
    float: hasil dari kecepatan / waktu
    """
    return kecepatan / waktu
