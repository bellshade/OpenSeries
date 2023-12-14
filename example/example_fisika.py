import OpenSeries.fisika as fisika

print("hitung kecepatan")
result_kecepatan = fisika.kecepatan(4, 2.3)
print(f"hasil dari kecepatan adalah: {result_kecepatan}")

print("hitung percepatan")
result_percepatan = fisika.percepatan(4, 2.3)
print(f"hasil dari percepatan adalah: {result_percepatan}")

print("hitung glbb (gerak lurus beraturan)")
result_glbb = fisika.gerak_lurus_beraturan(10, 2, 3)
print(f"hasil dari glbb adalah: {result_glbb}")

massa_benda = 14
kecepatan_benda = 23.4
print(
    f"menghitung energi kinetik pada benda {massa_benda} kg dengan kecepatan {kecepatan_benda} m/s"
)
print(f"hasilnya adalah : {fisika.energi_kinetik(massa_benda, kecepatan_benda)} joule")

volume_benda = 8
print(
    f"menghitung massa jenis benda dengan massa benda {massa_benda} gram, dan volume benda {volume_benda} cm3"
)
print(f"hasilnya adalah : {fisika.masa_jenis(massa_benda, volume_benda)}")
