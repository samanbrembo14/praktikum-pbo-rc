import random

class Karakter:
    def __init__(self, nama, attack, hp, defense):
        self.nama = nama
        self.attack = attack
        self.hp = hp
        self.defense = defense

    def attack_enemy(self, musuh):
        # Menghitung akurasi serangan
        akurasi = random.randint(1, 100)

        # Jika serangan meleset
        if akurasi < 28:
            print(f"\n ========== {self.nama} menyerang, tapi meleset! ==========")
        else:
            # Menghitung damage
            damage = self.attack - musuh.defense

            # Mengurangi HP musuh
            musuh.hp -= damage
            print(f"\n =========== {self.nama} menyerang {musuh.nama} dan memberikan {damage} damage! ==========")

            # Cek apakah musuh masih hidup
            if musuh.hp <= 0:
                print(f"\n ========== {musuh.nama} dikalahkan! ============ ")

    def regen_health(self):
        # Menambah HP
        heal_amount = random.randint(1, 25)
        self.hp += heal_amount
        print(f"\n ========== {self.nama} memulihkan {heal_amount} HP! =========== ")


# Daftar karakter
karakter_list = [
    Karakter("Pejuang", 20, 100, 10),
    Karakter("Penyihir", 50, 80, 4),
    Karakter("Pemburu", 32, 90, 7),
]

# Memilih karakter
print("Pilih karakter untuk Player 1:")
for i, karakter in enumerate(karakter_list):
    print(f"{i+1}. {karakter.nama}")

pilihan1 = int(input("Masukkan pilihan: ")) - 1

print("\nPilih karakter untuk Player 2:")
for i, karakter in enumerate(karakter_list):
    if i != pilihan1:
        print(f"{i+1}. {karakter.nama}")

pilihan2 = int(input("Masukkan pilihan: ")) - 1

# Memulai permainan
karakter1 = karakter_list[pilihan1]
karakter2 = karakter_list[pilihan2]

turn = 1

while karakter1.hp > 0 and karakter2.hp > 0:
    # Tampilan menu
    if turn == 1:
        print(f"\n--- Giliran {karakter1.nama} ---")
        print(f"\nHP : {karakter1.hp} | Attack : {karakter1.attack} | Def : {karakter1.defense}")
        print("\n1. Serang   2. Pulihkan HP ")
        pilihan1 = int(input("\nMasukkan pilihan: "))

        # Tetapkan aksi berdasarkan pilihan
        if pilihan1 == 1:
            action1 = "attack"
        elif pilihan1 == 2:
            action1 = "heal"
        else:
            print("Pilihan tidak valid!")
    else:
        print(f"\n--- Giliran {karakter2.nama} ---")
        print(f"\nHP : {karakter2.hp} | Attack : {karakter2.attack} | Def : {karakter2.defense}")
        print("\n1. Serang   2. Pulihkan HP ")
        pilihan2 = int(input("\nMasukkan pilihan: "))

        # Tetapkan aksi berdasarkan pilihan
        if pilihan2 == 1:
            action2 = "attack"
        elif pilihan2 == 2:
            action2 = "heal"
        else:
            print("Pilihan tidak valid!")

    # Lakukan aksi sesuai giliran
    if turn == 1:
        # Player 1 melakukan aksi
        if action1 == "attack":
            karakter1.attack_enemy(karakter2)
        elif action1 == "heal":
            karakter1.regen_health()
    else:
        # Player 2 melakukan aksi
        if action2 == "attack":
            karakter2.attack_enemy(karakter1)
        elif action2 == "heal":
            karakter2.regen_health()

    # Ganti giliran setelah setiap aksi
    turn = 3 - turn

# Menentukan pemenang
if karakter1.hp > 0:
    print(f"\n ========== {karakter1.nama} menang! ==========")
else:
    print(f"\n ========== {karakter2.nama} menang! ==========")
