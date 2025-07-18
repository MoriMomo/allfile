import numpy as np

# Data nilai ujian (dalam skala 0-100)
nilai_ujian = np.array([75, 80, 85, 90, 95])

# Menghitung rata-rata nilai ujian
rata_rata = np.mean(nilai_ujian)

# Menghitung standar deviasi nilai ujian
standar_deviasi = np.std(nilai_ujian)

print("Data Nilai Ujian:", nilai_ujian)
print("Rata-rata Nilai Ujian:", rata_rata)
print("Standar Deviasi Nilai Ujian:", standar_deviasi)
