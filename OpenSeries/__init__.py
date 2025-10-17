from OpenSeries.dasar import bulat, akar, tan_hiperbolik, volume_kubus

if __name__ == "__main__":
    list_dasar: list = [bulat, akar, tan_hiperbolik, volume_kubus]
    for tipe in range(len(list_dasar)):
        print(type(list_dasar[tipe]))
