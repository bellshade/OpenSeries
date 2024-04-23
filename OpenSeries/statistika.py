import numpy as np
from typing import Union
from OpenSeries.util import error as error


def entropy(
    label: list[int], base: int
) -> Union[float, int, error.Error, error.ErrorTipeData]:
    """
    fungsi menghitung entropy dari suatu fitur pada suatu dataset

    Parameter:
        label (list (int)): label fitur yang akan di hitung entropynya
        base (int): label dari entropy

    Return:
        (float, int): hasil dari kalkulasi dari entropy
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika nilai label yang diberikan kosong
    """
    if not isinstance(label, (list)):
        return error.ErrorTipeData(["list"])
    if not label:
        return error.Error("label tidak boleh kosong")
    if not all(isinstance(cek_nilai, int) for cek_nilai in label):
        return error.ErrorTipeData(["int"])
    _, count = np.unique(label, return_counts=True)
    probabilitas = count / len(label)
    probabilitas[probabilitas == 0] = 1

    log = np.log(probabilitas) if base is None else np.log(probabilitas) / np.log(base)
    return np.sum(abs(probabilitas * log))


def standar_deviasi(
    vektor: np.ndarray,
) -> Union[float, error.Error, error.ErrorTipeData]:
    """
    fungsi untuk mengukur penyebaran data terhadap nilai rata-ratanya

    Parameter:
        vektor (np.array)

    Return:
        (float): hasil dari kalkulasi standar deviasi
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika vektor yang diberikan kosong
    """
    if not isinstance(vektor, np.ndarray):
        return error.ErrorTipeData(["numpy array"])
    if len(vektor) == 0:
        return error.Error("vektor tidak boleh kosong")

    mean_value = np.mean(vektor)
    squared_diff = np.square(vektor - mean_value)
    variansi = np.mean(squared_diff)
    std_deviasi = np.sqrt(variansi)
    return std_deviasi


def variance(
    data: list[Union[int, float]],
) -> Union[float, error.ErrorTipeData, error.Error]:
    """
    variance merupakan konsep matematika untuk mengetahui keragamaman
    nilai pada data terhadap penyebaran nilai rata-rata.
    Parameter:
        data (list (int, float)): input data yang masuk

    Return:
        (float): hasil dari kalkulasi varian
        error.ErrorTipeData: error jika tipe data salah
        error.Error: jika vektor yang diberikan kosong
    """
    # initial result
    result: float = 0.0
    if isinstance(data, list):
        # mengecek apakah nilai dalam list kodong
        if not data:
            return error.Error("List tidak boleh kosong")
        # membuat looping untuk memecah nilai yang terdapat pada list
        for cek_nilai in data:
            # mengecek nilai dalam list apakah semua tipe data berbentuk int
            # atau float, jika tidak error
            if not isinstance(cek_nilai, (int, float)):
                return error.ErrorTipeData(["float", "int"])
            result += (cek_nilai - np.mean(data)) * (cek_nilai - np.mean(data))
        return result / len(data)
