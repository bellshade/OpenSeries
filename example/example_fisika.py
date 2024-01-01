# contoh sederhana dari fungsi-fungsi fisika
# sumber file: OpenSeries/fisika.py
import OpenSeries.fisika as fisika

# fungsi menghitung kecepatan
print("hitung kecepatan")
result_kecepatan = fisika.kecepatan(4, 2.3)
print(f"hasil dari kecepatan adalah: {result_kecepatan}\n")

# fungsi menghitung percepatan
print("hitung percepatan")
result_percepatan = fisika.percepatan(4, 2.3)
print(f"hasil dari percepatan adalah: {result_percepatan}\n")

# fungsi menghitung glbb
print("hitung glbb (gerak lurus beraturan)")
result_glbb = fisika.gerak_lurus_beraturan(10, 2, 3)
print(f"hasil dari glbb adalah: {result_glbb}\n")

# fungsi menghitung energi kinetik
massa_benda = 14
kecepatan_benda = 23.4
print(
    f"menghitung energi kinetik pada benda {massa_benda} kg dengan kecepatan {kecepatan_benda} m/s"
)
print(
    f"hasilnya adalah : {fisika.energi_kinetik(massa_benda, kecepatan_benda)} joule\n"
)

# menghitung masa jenis benda
volume_benda = 8
print(
    f"menghitung massa jenis benda dengan massa benda {massa_benda} gram, dan volume benda {volume_benda} cm3"
)
print(f"hasilnya adalah : {fisika.masa_jenis(massa_benda, volume_benda)}\n")

# menghitung energi potensial
massa_benda_potensial = 12
gravitasi_bumi = 9.78
ketinggian_benda = 400
print("menghitung energi potensial dari suatu benda")
print(f"dengan massa benda adalah: {massa_benda_potensial}")
print(f"gravitasi bumi {gravitasi_bumi}")
print(f"dan ketinggian benda adalah {ketinggian_benda}")
print(
    f"hasilnya adalah: {fisika.energi_potensial(massa_benda_potensial, gravitasi_bumi, ketinggian_benda)}\n"
)

# menghitung hukum arus ohm
kuat_arus = 30
hambatan = 3
print("menghitung hukum ohm")
print(f"dengan kuat arus {kuat_arus}")
print(f"hambatan {hambatan}")
print(f"hasilnya adalah: {fisika.hukum_ohm(kuat_arus, hambatan)}\n")
