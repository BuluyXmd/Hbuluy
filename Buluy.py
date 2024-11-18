# Meminta pengguna memasukkan nama
nama = input("Masukkan nama Anda: ")

# Meminta pengguna memasukkan jumlah pengulangan
jumlah_pengulangan = int(input("Berapa kali nama akan dicetak? "))

# Mencetak nama sebanyak jumlah pengulangan
for i in range(jumlah_pengulangan):
    print(f"{i+1}. {nama}")