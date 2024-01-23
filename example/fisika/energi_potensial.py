import OpenSeries.fisika as fisika

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
