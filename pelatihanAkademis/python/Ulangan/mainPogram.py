# main_program.py
import modulePredikat
import moduleKenaikan
import moduleRata

mata_pelajaran = [
    "Matematika Dasar",
    "Matematika Minat",
    "Biologi",
    "Sejarah Indonesia",
    "Kimia",
    "Fisika",
    "PPKN",
    "PJOK",
    "PKU",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "PJOK",
]


def main():
    for mata_pelajaran_item in mata_pelajaran:
        print("Masukan Nilai " + mata_pelajaran_item)
        nilai_uh = float(input("Masukkan nilai UH: "))
        nilai_tugas = float(input("Masukkan nilai tugas: "))
        nilai_AAS = float(input("Masukkan nilai UAS: "))
        nilai_AAS = float(input("Masukkan nilai UAS: "))

    nilai_rapor = moduleRata.hitung_nilai_rapor(nilai_uh, nilai_tugas, nilai_AAS1)
    predikat = modulePredikat.predikat_nilai_rapor(nilai_rapor)

    print("Nilai rapor:", nilai_rapor)
    print("Predikat:", predikat)


main()
