import numpy as np
from typing import Union,List
from OpenSeries.util import error as error


def nilai_tengah(vector: Union[List[Union[int, float]], np.ndarray]):
    # check data type
    if not isinstance(vector,(list,np.ndarray)):
        return error.ErrorTipeData(["List"])
    # check length data
    n = len(vector)
    if n == 0:
        return error.Error("vektor tidak boleh kosong")
    # if length data is odd
    if n%2 != 0:
        idx = n//2
        return vector[idx]
    elif n%2 ==0 :
        idx = n//2
        return np.mean(vector[idx-1:idx+1])
    

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

def varian(vector:np.ndarray)-> Union[float,error.Error,
                                      error.ErrorTipeData]:
    if not isinstance(vector,np.ndarray):
        return error.ErrorTipeData(["Numpy array"])
    if len(vector) == 0:
        return error.Error("Vector tidak boleh kosong")
    mean_value = np.mean(vector)
    squared_diff = np.square(vector - mean_value)
    return np.mean(squared_diff)
    