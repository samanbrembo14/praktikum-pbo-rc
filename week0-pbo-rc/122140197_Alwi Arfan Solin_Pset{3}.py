def create_txt(nama, nim, resolusi):

    try:
        with open("Me.txt", "w") as file:
            file.write(f"Nama : {nama}\n")
            file.write(f"NIM : {nim}\n")
            file.write(f"Resolusi Saya di Tahun ini : {resolusi}\n")

        print("Sukses memasukkan ke Me.txt")
    except FileNotFoundError:
        print("Error: File Me.txt tidak ada/tidak ditemukan")

nama = str(input('Masukkan nama : '))
nim = str(input('Masukkan NIM : '))
resolusi = str(input('Masukkan Resolusi : '))

create_txt(nama, nim, resolusi)
