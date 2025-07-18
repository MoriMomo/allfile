def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    year = int(input("Masukkan tahun: "))
    if is_leap_year(year):
        print(year, "adalah tahun kabisat.")
    else:
        print(year, "bukan tahun kabisat.")


if __name__ == "__main__":
    main()
