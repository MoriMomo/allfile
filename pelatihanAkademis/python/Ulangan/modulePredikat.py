# modul2.py
def predikat_nilai_rapor(nilai_rapor):
    if 91 <= nilai_rapor <= 100:
        return "A"
    elif 83 <= nilai_rapor <= 90:
        return "B"
    elif 75 <= nilai_rapor <= 82:
        return "C"
    else:
        return "D"
