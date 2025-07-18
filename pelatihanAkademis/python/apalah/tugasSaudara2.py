# Daftar menu dan harganya
menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Soto Ayam": 10000,
    "Gado-gado": 13000,
    "Es Teh": 5000,
    "Es Jeruk": 6000,
}

# Daftar pesanan
pesanan = []

# Input nama pelanggan
nama_pelanggan = input("Masukkan nama Anda: ")

# Input jumlah pesanan
jumlah_pesanan = int(input("Berapa banyak pesanan Anda? "))

# Input pesanan
for i in range(jumlah_pesanan):
    nama_menu = input("Masukkan nama menu: ")
    jumlah_menu = int(input("Masukkan jumlah menu: "))
    pesanan.append((nama_menu, jumlah_menu))

# Hitung total harga
total_harga = 0
for nama_menu, jumlah_menu in pesanan:
    total_harga += menu[nama_menu] * jumlah_menu

# Tampilkan struk
print("======================================")
print("Restoran Sederhana")
print("Jl. Sudirman No. 123")
print("======================================")
print("Nama Pelanggan:", nama_pelanggan)
print("--------------------------------------")
for nama_menu, jumlah_menu in pesanan:
    print(
        "{:20} x{:3} = {:6}".format(
            nama_menu, jumlah_menu, menu[nama_menu] * jumlah_menu
        )
    )
print("--------------------------------------")
print("Total Harga: {:6}".format(total_harga))
print("======================================")
