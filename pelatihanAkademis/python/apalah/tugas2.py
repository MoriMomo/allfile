# Nomor 1
def tampilkan_kota_asal(kota):
    print("Kota asal saya " + kota)


tampilkan_kota_asal("Jakarta")


# Nomor 2
def print_kota_asal(kota):
    print("Kota saya asal:", kota)


# Daftar nama kota
daftar_kota = ["Jakarta", "Bandung", "Surabaya", "Medan", "Bali"]

# Perulangan untuk mencetak nama kota
for kota in daftar_kota:
    print_kota_asal(kota)


# Nomor 3
def print_hasil_perkalian(angka1, angka2):
    hasil = angka1 * angka2
    print("Hasil perkalian 2 angka:", hasil)


# Perulangan untuk mencetak hasil perkalian 2 angka
for i in range(1, 6):
    for j in range(1, 6):
        print_hasil_perkalian(i, j)


# nomor 4
def print_keyword_argument(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


print_keyword_argument(arg1="a", arg2="b", arg3="c", arg4="d")
