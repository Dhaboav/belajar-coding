from datetime import datetime


def tulis_data_ke_baris(nama_file, baris_ke, data):
    with open(nama_file, "r") as file:
        lines = file.readlines()

    if baris_ke > len(lines):
        # Jika baris_ke lebih besar dari jumlah baris dalam file,
        # tambahkan baris kosong hingga mencapai baris yang diinginkan
        for _ in range(len(lines), baris_ke):
            lines.append("\n")

    lines[baris_ke - 1] = data + "\n"  # Tulis data pada baris yang spesifik

    with open(nama_file, "w") as file:
        file.writelines(lines)


def tulis_data_ke_baris_terakhir(nama_file, data):
    with open(nama_file, "a") as file:
        file.write("\n" + data)


def baca_data_dari_file(nama_file):
    with open(nama_file, "r") as file:
        return file.read()


def waktu():
    now = datetime.now()
    log_waktu = f"{now:%h-%d-%Y}, {now:%H:%M:%S}"
    return log_waktu


nama_file = "Experimental/teks.txt"
tulis_data_ke_baris(nama_file, 1, f"Last Log: {waktu()}") # Waktu log

# # Pengisian file
# banyakData = int(input("Masukan berapa banyak data yang dimasukan? "))
# for data in range(banyakData):
#     nama = input("Masukan nama lengkap anda: ").title()
#     umur = int(input("Masukan umur anda: "))
#     jenis_kelamin = input("Masukan jenis kelamin anda: ").title()
#     biodata = f"{nama}, {umur}, {jenis_kelamin}"
#     tulis_data_ke_baris_terakhir(nama_file, biodata)
# else:
#     print("\nDone!!!")

# =======================================================

# Pembacaan file dan pemasukan ke dict
data_mahasiswa = {}
file = baca_data_dari_file(nama_file)
for line in file.split("\n"):
    data = line.strip().split(", ")
    if len(data) != 3:
        continue

    nama = data[0]
    umur = int(data[1])
    jenis_kelamin = data[2]
    data_mahasiswa[nama] = (umur, jenis_kelamin)

# Klasifikasi berdasarkan jenis kelamin
pria = []
perempuan = []
for nama in data_mahasiswa:
    data_umur, data_jenis_kelamin = data_mahasiswa[nama]
    if data_jenis_kelamin == "Pria":
        pria.append(nama)
    else:
        perempuan.append(nama)

# Menampilkan hasil dari klasifikasi
print(f"Pria: {len(pria)}, Perempuan: {len(perempuan)}")
# Bebas ditambahkan sesuai kebutuhan
# for x in perempuan:
#     print(f"Nama: {x}, Umur: {data_mahasiswa[x][0]}")