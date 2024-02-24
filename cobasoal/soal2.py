# alwi arfan solin
# 122140197
# soal 2

def create_nilai(num_murid) : 
	daftar_nilai = {}

	for i in range(num_murid) :
		nama = input("masukkan nama : ")
		nilai = int(input("masukkan nilai : "))

		if nama in daftar_nilai : 
			print(f"'{nama}'sudah ada")

		daftar_nilai[nama] = nilai 
	return daftar_nilai

num_murid = int(input("banyak murid ? :  "))
daftar_nilai = create_nilai(num_murid)

print("Grade : ", daftar_nilai )





