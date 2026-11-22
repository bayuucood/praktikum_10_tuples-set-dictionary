# A. Tuple dan set 
# LIST
data_list = [10, 2, 4, 3, 2]
print(data_list)
print ()

# TUPLES
data_tuples = (7, 8, 10, 11)
print(data_tuples)
print(data_tuples[1])
print ()

# SET
data_sets = {10, 4, 3, 2, 7, 6, 5}
print(data_sets)
print ()

# B. Dictionary
# LIST
data_list = ['harry', 'bayu', 'pamungkas']
print(data_list[0])

# DICTIONARY
data_dict = {
    'key': 'value',
    'hr': 'harry',
    'by': 'bayu',
    'pm': 'pamungkas',
    'nmbr': 100,
    'list': data_list
}

# Mengakses data berdasarkan key
print(data_dict['hr'])
print(data_dict['nmbr'])
print(data_dict['list'])
print ()

# C. Operasi pada dictionary
# Membuat dictionary
data_dict = {
    "hr": "harry serepet",
    "pet": "bayu tetetet",
    "ndo": "bang nando"
}

# Menghitung panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# Mengecek keberadaan key
KEY = "hr"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengakses value menggunakan get()
print(data_dict["hr"])
print(data_dict.get("hr"))
print(data_dict.get("kis", "key tidak ditemukan"))

# Mengubah data
data_dict["hr"] = "harry si ganteng"
print(data_dict)

# Menambahkan data baru
data_dict["de"] = "ade si adek"
print(data_dict)

# Menggunakan update()
data_dict.update({"hr": "harry serepet"})
print(data_dict)

data_dict.update({"iwn": "iwan pak dosen"})
print(data_dict)

# Menghapus data
del data_dict["iwn"]
print(data_dict)
print ()

# D. Looping pada dict
teman_teman = {
    "r": "royan",
    "s": "pak sulis",
    "t": "toto",
    "u": "untsa"
}

# Menampilkan key
for teman in teman_teman:
    print(teman)
print ()

# menggunakan keys ()
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
print ()

# menggunakan values ()
values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
print ()

# menggunakan items ()
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)
print ()

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")
print ()

# latihan soal 
# 1.a
mahasiswa = (
    "Harry Bayu Pamungkas",
    "2605060024",
    "Teknologi Informasi"
)

print(mahasiswa)
print ()

# 1.b
print("NIM:", mahasiswa[1])
print("Prodi:", mahasiswa[2])
print ()

# 1.c
#mahasiswa[2] = "Teknologi Informasi" # g bisa karena immutable

#1.d
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
print ()

# 2.a
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

print(data_mahasiswa)
print ()

# 2.b
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026

print(data_mahasiswa)
print ()

# 2.c 
del data_mahasiswa["nim"]
print(data_mahasiswa)
print ()

# soal 3.
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
# 3.b
for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")
print ()

# 3.c
total_belanja = 0
for harga in keranjang.values():
    total_belanja += harga

print(f"Total belanja: Rp {total_belanja}")
print ()
