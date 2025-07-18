def hitung_operasi_tiga_bilangan(bilangan1, bilangan2, bilangan3):
    # Penjumlahan
    penjumlahan = bilangan1 + bilangan2 + bilangan3

    # Pengurangan
    pengurangan = bilangan1 - bilangan2 - bilangan3

    # Perkalian
    perkalian = bilangan1 * bilangan2 * bilangan3

    # Pembagian
    if bilangan3 != 0:  # Menghindari pembagian oleh nol
        pembagian = (bilangan1 * bilangan2) / bilangan3
    else:
        pembagian = "Pembagian oleh nol tidak dapat dilakukan"

    # Perpangkatan
    perpangkatan = bilangan1 ** (bilangan2**bilangan3)

    return {
        "Penjumlahan": penjumlahan,
        "Pengurangan": pengurangan,
        "Perkalian": perkalian,
        "Pembagian": pembagian,
        "Perpangkatan": perpangkatan,
    }


# Contoh pemanggilan fungsi untuk tiga bilangan
hasil_tiga_bilangan = hitung_operasi_tiga_bilangan(3, 2, -1)
print("\nHasil Operasi untuk Tiga Bilangan:")
print(hasil_tiga_bilangan)
