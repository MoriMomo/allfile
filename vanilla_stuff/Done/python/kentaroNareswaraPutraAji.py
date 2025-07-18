def add(a, b):
    answer = a + b
    print(str(a) + " + " + str( b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b ) + " = " + str(answer) + "\n")
def mul(a, b):
    answer = a*b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Penambahan")
    print("B. Pengurangan")
    print("C. Perkalian")
    print("D. Pembagian")
    print("E. Exit")
    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Penambahan")
        a = int(input("Masukan angka pertama: "))
        b = int(input("Masukan angka kedua: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Pengurangan")
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Perkalian")
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Pembagian" )
        a = int(input("Masukan angka pertama:"))
        b = int(input("Masukan angka kedua: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()