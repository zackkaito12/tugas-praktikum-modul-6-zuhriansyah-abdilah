# tugas-praktikum-modul-6-zuhriansyah-abdilah

print("Nama : Zuhriansyah Abdilah")
print("Nim  : 2310432020")
print("Program Nilai ujian Mahasiswa")
print("==========================================")

n = int(input("Masukkan jumlah mahasiswa   : "))
m = int(input("Masukkan jumlah mata kuliah : "))

print("------------------------------------------")
print("          Nama Mahasiswa")
print("------------------------------------------")
nama_mahasiswa = []
print("Masukkan Nama Mahasiswa : ")
for i in range(n):
    nmh = input(f"Nama ke-{i+1}= ")
    nama_mahasiswa.append(nmh)

print("------------------------------------------")
print("          Nama Mata Kuliah")
print("------------------------------------------")
nama_mata_kuliah = []
print("Masukkan Nama Mata Kuliah : ")
for i in range(m):
    nmk = input(f"Nama ke-{i+1}= ")
    nama_mata_kuliah.append(nmk)

data_nilai = []
for i in range(n):
    nilai_mahasiswa = []
    print(f"Masukkan nilai ujian {nama_mahasiswa[i]}:")
    for j in range(m):
        nilai = float(input(f"Nilai mata kuliah {nama_mata_kuliah[j]}: "))
        nilai_mahasiswa.append(nilai)
    data_nilai.append(nilai_mahasiswa)

print("\nData Nilai Ujian:")
for i in range(n):
    print("Mahasiswa", nama_mahasiswa[i], end=": ")
    for nilai in data_nilai[i]:
        print(nilai, end=" ")
    print()

print("\nRata-rata Nilai Ujian:")
for i in range(n):
    total_nilai = 0
    for nilai in data_nilai[i]:
        total_nilai += nilai
    rata_rata = total_nilai / m
    print("Mahasiswa", nama_mahasiswa[i], ":", rata_rata)

print("\nNilai Tertinggi dan Terendah:")
for j in range(m):
    nilai_tertinggi = float('-inf')
    nilai_terendah = float('inf')
    mahasiswa_tertinggi = ""
    mahasiswa_terendah = ""
    for i in range(n):
        nilai = data_nilai[i][j]
        if nilai > nilai_tertinggi:
            nilai_tertinggi = nilai
            mahasiswa_tertinggi = nama_mahasiswa[i]
        if nilai < nilai_terendah:
            nilai_terendah = nilai
            mahasiswa_terendah = nama_mahasiswa[i]
    print("Mata Kuliah", nama_mata_kuliah[j])
    print("   Nilai Tertinggi:", nilai_tertinggi, "oleh", mahasiswa_tertinggi)
    print("   Nilai Terendah:", nilai_terendah, "oleh", mahasiswa_terendah)
