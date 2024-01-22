import numpy as np
from typing import Union
from OpenSeries.util import error as pesan_error


def entropy(label: list[int], base: int = None) -> Union[float, int, str]:
    """
    fungsi menghitung entropy dari suatu fitur pada suatu dataset

    parameter:
        label (list (int)): label fitur yang akan di hitung entropynya
    """
    if not isinstance(label, (list)):
        return pesan_error.error_tipe_data(["list"])
    if not label:
        return pesan_error.error_format("label tidak boleh kosong")
    if not all(isinstance(cek_nilai, int) for cek_nilai in label):
        return pesan_error.error_tipe_data(["int"])
    _, count = np.unique(label, return_counts=True)
    probabilitas = count / len(label)
    probabilitas[probabilitas == 0] = 1

    log = np.log(probabilitas) if base is None else np.log(probabilitas) / np.log(base)
    return np.sum(abs(probabilitas * log))


def standar_deviasi(vektor: np.ndarray) -> Union[float, str]:
    """
    fungsi untuk mengukur penyebaran data terhadap nilai rata-ratanya

    parameter:
        vektor (np.array)
    """
    if not isinstance(vektor, np.ndarray):
        return pesan_error.error_tipe_data(["numpy array"])
    if len(vektor) == 0:
        return pesan_error.error_format("vektor tidak boleh kosong")

    mean_value = np.mean(vektor)
    squared_diff = np.square(vektor - mean_value)
    variansi = np.mean(squared_diff)
    std_deviasi = np.sqrt(variansi)
    return std_deviasi
