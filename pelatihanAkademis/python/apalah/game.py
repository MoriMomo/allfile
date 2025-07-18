print("Selamat datang di Game Decision Making!") 

name = input("Masukkan nama pemain: ")

print(f"Halo {name}! Silakan pilih opsi berikut:")

print("1. Mulai game")
print("2. Bantuan")
print("3. Keluar")

option = input("Pilihan menu: ")

if option == "1":
  print("\nAnda memasuki hutan belantara...")
  
  print("Anda menemukan 2 jalan:")
  path = input("Pilih jalan mana yang akan dilewati (kiri/kanan)? ")
  
  if path == "kiri":
    print("\nJalan berakhir. Anda tersesat di hutan.") 
  elif path == "kanan":
    print("\nAnda menemukan sungai.")
    across = input("Berenang menyebrangi sungai atau jalan mengikuti aliran sungai (berenang/jalan)? ")
    
    if across == "berenang":
      print("\nAnda tenggelam dan mati.")
    elif across == "jalan":
      print("\nSelamat! Anda berhasil melewati sungai dan hutan. Anda menang!")
      
elif option == "2":
  print("\nPetunjuk: \n1. Baca setiap skenario dengan saksama \n2. Pilih opsi dengan bijak untuk melanjutkan perjalanan \n3. Semoga berhasil!")
  
elif option == "3":
  print("\nTerima kasih telah bermain. Sampai jumpa!")

else:
  print("Pilihan menu tidak valid. Silakan coba lagi.")