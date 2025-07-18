import numpy as np

# Data pengeluaran bulanan dalam ribu rupiah
pengeluaran_makanan = np.array([1000, 1200, 800, 950])
pengeluaran_transportasi = np.array([500, 600, 450, 700])
pengeluaran_tagihan = np.array([300, 350, 320, 380])

# Menghitung total pengeluaran bulanan
total_makanan = np.sum(pengeluaran_makanan)
total_transportasi = np.sum(pengeluaran_transportasi)
total_tagihan = np.sum(pengeluaran_tagihan)

# Menghitung total pengeluaran keseluruhan
total_pengeluaran = total_makanan + total_transportasi + total_tagihan

print("Pengeluaran Makanan:", pengeluaran_makanan)
print("Pengeluaran Transportasi:", pengeluaran_transportasi)
print("Pengeluaran Tagihan:", pengeluaran_tagihan)
print("Total Pengeluaran Makanan:", total_makanan)
print("Total Pengeluaran Transportasi:", total_transportasi)
print("Total Pengeluaran Tagihan:", total_tagihan)
print("pengeluaran tagihan: ", pengeluaran_tagihan)
print("Total Pengeluaran Bulanan: ", total_pengeluaran)
