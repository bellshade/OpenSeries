import OpenSeries.fisika as fisika

# fungsi menghitung energi kinetik
massa_benda = 14
kecepatan_benda = 23.4
print(
    f"menghitung energi kinetik pada benda {massa_benda} kg dengan kecepatan {kecepatan_benda} m/s"
)
print(
    f"hasilnya adalah : {fisika.energi_kinetik(massa_benda, kecepatan_benda)} joule\n"
)
