# Program 10.1 Tuples dan Sets
print ("PROGRAM 10.1")
print ( )

# LIST
# Menggunakan kurung siku []
data_list = [10, 2, 4, 3, 2]
print (data_list)
print ("\n")

# tuples
# Menggunakan kurung biasa ()
data_tuples = (7, 8, 10, 11)
print (data_tuples)
# print (data_tuples [1]) 

# tidak bisa dilakukan
# data_tuples [1] = "bayem"
# data_tuples.append (1)

# set (himpunan)
data_sets = {10, 4, 3, 2, 7, 6, 5}
print (data_sets)
# print (data_sets [0])  # Ini akan menyebabkan error karena set tidak mendukung akses elemen berdasarkan indeks
print ()

# PROGRAM 10.2 DICTIONARY
# DICTIONARY
# list → array, mengakses dengan menggunakan index
data_list = ['ucup', 'rendi', 'salsa']
print (data_list[0])
# dictionary (dict) → associative array
# identifier → key
data_dict = {
'key':'value',
'cp': 'ucup',
'rd': 'rendi',
'sl': 'salsa',
'nmbr': 100,
'list': data_list
}


print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])
print()

# PROGRAM 10.3 OPERASI DICTIONARY
## --- Operasi Dictionary ---
data_dict = {
"cup":"ucup surucup",
"pet":"opet saripet",
"ndo":"nando surundo"
}
print ()

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")
print ()

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")
print ()

# MENGAKSES VALUE (READ) DENGAN GET
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan")) # cek key dengan massage
print ()

# MENGUPDATE DATA 
data_dict["cup"] = "ucup siganteng"
print(data_dict)
data_dict["de"] = "ade si adek"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"de": "iwan emang keren"})
print(data_dict)
print()

# MENGHAPUS DATA
del data_dict["de"] # error nanti dibenerin
print (data_dict)
print ()

# PROGRAM 10.4 LOOPING DICTIONARY
# --- Looping Dictionary ----

teman_teman = {
    "cup"   : "ucup surucup",
    "tong"  : "sotong surotong",
    "lur"   : " lur sedulur",
    "wel"   : "bung towel"
}

# Looping first try ( yang keluar hanya key)
for teman in teman_teman:
    print (teman)
print ()

# Operator untuk mengambil item
keys = teman_teman.keys ()
print (keys)
print ()

for key in teman_teman.keys() :
    print (teman_teman.get (key))
print ()

values = teman_teman.values ()
print (values)
print ()

for value in teman_teman.values () :
    print(value)
print ()

items = teman_teman.items()
print (items)
print ()

for item in teman_teman.items () :
    print (item)
print ()

for key, value in teman_teman.items () :
    print(f"key = {key}, value = {value}")
print ()
