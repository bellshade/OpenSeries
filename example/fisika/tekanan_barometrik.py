import OpenSeries.fisika as fisika

# tekanan udara
tekanan = 100_000.0
# memanggil fungsi dari ketinggian barometrik
hasil = fisika.ketinggian_barometrik(tekanan)
print(f"tekanan: {tekanan} Pa, Ketinggian adalah: {hasil} meter")
