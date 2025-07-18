from datetime import datetime

print("Selamat Datang di Restoran Kita!")

# -Wajib terdapat list
menu = ["Nasi Goreng", "Mie Goreng", "Ayam Bakar", "Es Teh"]
harga = [15000, 14000, 18000, 5000]

nama_pemesan = input("Masukkan nama pemesan: ")

# -Wajib terdapat input serta variabel
pesanan = []
total_harga = 0

# - Wajib terdapat perulangan
while True:
    print("\nMenu Makanan")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]} (Rp{harga[i]:,})")

    pilih = int(input("Silahkan pilih menu (0 jika selesai): "))

    # -Wajib terdapat percabangan
    if pilih == 0:
        break
    else:
        nama_menu = menu[pilih - 1]
        harga_menu = harga[pilih - 1]

        pesanan.append(nama_menu)
        total_harga += harga_menu

print(f"\nPemesan: {nama_pemesan}")
print(f"Tanggal: {datetime.now().strftime('%d %b %Y')}\n")

# - Tampilan diformat menggunakan pemformatan string agar rapi
print("Pesanan:")
for menu in pesanan:
    print(f"- {menu}")

print(f"Total harga: Rp{total_harga:,}")
print("\nTerima kasih sudah berkunjung!")
