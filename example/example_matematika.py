import OpenSeries.matematika as matematika

print("hitung jari jari lingkaran")
hasil_jari_lingkaran = matematika.luas_lingkaran(4.5)
print(f"hasil dari hitung jari jari lingkaran: {hasil_jari_lingkaran}\n")

nilai_rata = [2, 3, 5, 5, 6, 1, 2, 3]
print(f"menghitung nilai rata-rata dari {nilai_rata}")
print(f"hasilnya adalah: {matematika.rata_rata(nilai_rata)}\n")

nilai_faktorial = 25
print(f"menghitung nilai faktorial dari angka {nilai_faktorial}")
print(f"hasilnya adalah : {matematika.faktorial(nilai_faktorial)}\n")

nilai_permutasi = 12
print(f"menghitung nilai permutasi dari {nilai_permutasi}")
print(f"hasilnya adalah : {matematika.permutasi(nilai_permutasi, 2)}\n")

nilai_kombinasi = 15
print(f"menghitung nilai kombinasi dari {nilai_kombinasi}")
print(f"hasilnya adalah : {matematika.kombinasi(nilai_kombinasi, 3)}\n")

nilai1 = 24
nilai2 = 40
print(
    f"hitung nilai fpb (faktor persekutuan terbesar) dari nilai {nilai1} dan {nilai2}"
)
print(f"hasilnya adalah : {matematika.fpb(nilai1, nilai2)}\n")

rentang_nilai = 300
print(
    f"rentang nilai {rentang_nilai} faktor prima adalah {matematika.faktor_prima(rentang_nilai)}\n"
)
