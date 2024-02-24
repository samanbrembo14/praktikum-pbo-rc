# Alwi arfan solin
# 122140197
# soal 2

def create_nilai(num_murid) :
  daftar_nilai = {}

  for i in range (num_murid) :
    nama = input("Masukkan Nama : ")
    nilai = int(input("Masukkan Nilai : "))

    if nama in daftar_nilai :
      print(f"'{nama}' Sudah ada")

    daftar_nilai[nama] = nilai 

  return daftar_nilai

num_murid = int(input("Banyak Murid : "))
daftar_nilai = create_nilai(num_murid)

print("Grade : ", daftar_nilai)