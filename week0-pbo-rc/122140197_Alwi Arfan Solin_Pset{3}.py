def create_txt(nama, nim, resolusi):

    try:
        with open("Me.txt", "w") as file:
            file.write(f"Nama : {nama}\n")
            file.write(f"NIM : {nim}\n")
            file.write(f"Resolusi Saya di Tahun ini : {resolusi}\n")

        print("Sukses memasukkan ke Me.txt")
    except FileNotFoundError:
        print("Error: File Me.txt tidak ada/tidak ditemukan")

nama = "Alwi Arfan Solin"
nim = "122140197"
resolusi = "have a good grade for all this course"

create_txt(nama, nim, resolusi)
