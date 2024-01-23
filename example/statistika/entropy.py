from OpenSeries import statistika as statistika

# contoh dari entropy
label = [1, 1, 2, 2, 3, 3]
hasil_base_2 = statistika.entropy(label, base=2)
print(hasil_base_2)
