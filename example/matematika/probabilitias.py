import OpenSeries.matematika as matematika

nilai_A = 5
nilai_S = 10

print("menghitung probabilitas suatu kejadian")
print(f"dengan jumlah hasil yang menguntungkan :{nilai_A}")
print(f"dan dengan ukuran ruang sampel {nilai_S}")
print(
    f"probabilitas dari kejadiannya adalah: {matematika.peluang_kejadian(nilai_A, nilai_S)}\n"
)
