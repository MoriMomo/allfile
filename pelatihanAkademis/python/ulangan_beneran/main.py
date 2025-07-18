import volume
import luas_segitiga
import bilangan_ganjil_genap

# Input nilai variabel yang dibutuhkan
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

alas = float(input("Masukkan alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))

# Hitung volume balok dan tampilkan hasil beserta status bilangan ganjil/genap
hasil_volume = volume.hitung_volume_balok(panjang, lebar, tinggi)
print("Volume balok:", hasil_volume)
print(
    "Status bilangan ganjil/genap:",
    bilangan_ganjil_genap.cek_bilangan(int(hasil_volume)),
)
print(hasil_volume)

# Hitung luas segitiga dan tampilkan hasil beserta status bilangan ganjil/genap
hasil_luas_segitiga = luas_segitiga.hitung_luas_segitiga(alas, tinggi_segitiga)
print("Luas segitiga:", hasil_luas_segitiga)
print(
    "Status bilangan ganjil/genap:",
    bilangan_ganjil_genap.cek_bilangan(int(hasil_luas_segitiga)),
)
print(hasil_luas_segitiga)
