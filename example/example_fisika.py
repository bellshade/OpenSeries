import OpenSeries.fisika as fisika

print("hitung kecepatan")
result_kecepatan = fisika.kecepatan(4, 2.3)
print(f"hasil dari kecepatan adalah: {result_kecepatan}")

print("hitung percepatan")
result_percepatan = fisika.percepatan(4, 2.3)
print(f"hasil dari percepatan adalah: {result_percepatan}")

print("hitung glbb (gerak lurus beraturan)")
result_glbb = fisika.rumus_glbb(10, 2, 3)
print(f"hasil dari glbb adalah: {result_glbb}")

print("menghitung koordinat parabola (x, y)")
result_parabola = fisika.koordinat_parabola(2.0, 3.2, 2.0, 3.0)
print(f"hasil dari koordinat parabola adalah {result_parabola}")
