import OpenSeries.matematika as matematika

nilai_suku = 5
suku_pertama = 3
selisih_suku = 2
print("menghitung jumlah deret aritmatika")
print(f"dengan nilai suku: {nilai_suku}")
print(f"suku pertama: {suku_pertama}")
print(f"selisih suku: {selisih_suku}")
print(
    f"hasilnya adalah: {matematika.hitung_jumlah_deret(nilai_suku, suku_pertama, selisih_suku)}\n"
)
