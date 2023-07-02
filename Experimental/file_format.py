Note = """
Untuk pengisian file dan pembacaan file bisa dilakukan terpisah
ataupun bersamaan disesuaikan dengan kebutuhan.
"""


# Pengisian file
banyakData = int(input("Masukan berapa banyak data yang dimasukan? "))
for data in range(banyakData):
    nama = input("Masukan nama lengkap anda: ").title()
    umur = int(input("Masukan umur anda: "))
    jenisKelamin = input("Masukan jenis kelamin anda: ").title()
    print("\n")
    biodata = f"{nama}, {umur}, {jenisKelamin}"
    with open("Experimental/teks.txt", "a") as file:
        file.write("\n" + biodata)
else:
    print("Done!!!")

# =======================================================

# Pembacaan file dan pemasukan ke dict
data_mahasiswa = {}
with open("Experimental/teks.txt", "r") as file:
    for line in file:
        data = line.strip().split(", ")
        nama = data[0]
        umur = int(data[1])
        jenis_kelamin = data[2]
        data_mahasiswa[nama] = (umur, jenis_kelamin)

# Klasifikasi berdasarkan jenis kelamin
pria = []
perempuan = []
for nama in data_mahasiswa:
    data_umur, data_jenisKelamin = data_mahasiswa[nama]
    if data_jenisKelamin == "Pria":
        pria.append(nama)
    else:
        perempuan.append(nama)

# Menampilkan hasil dari klasifikasi
print(f"Pria: {len(pria)}, Perempuan: {len(perempuan)}")
for x in perempuan:
    print(f"Nama: {x}, Umur: {data_mahasiswa[x][0]}")