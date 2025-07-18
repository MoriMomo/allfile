A = 400  # m²
C = 0.6
R = [300, 260, 272, 100, 38, 9, 12, 54, 36, 44, 45, 70]  # mm

# Ubah curah hujan ke meter
R = [r * 0.001 for r in R]  # m

# Hitung volume air per bulan
V = [A * r * C for r in R]  # m³

# Jumlahkan untuk mendapatkan total volume air dalam satu tahun
V_total = sum(V)  # m³

print(V_total)
