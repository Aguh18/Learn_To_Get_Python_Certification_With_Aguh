# membuat tuple
tup = (1, 2, 3, "empat", "lima")

# mengakses nilai tuple
print(tup[0]) # output: 1
print(tup[3]) # output: empat

# mencetak seluruh isi tuple
print("print semua nilai pada tuple")
for item in tup:
    print(item)

# mencetak panjang tuple

print("panjang tuplenya adalah", len(tup)) # output: 5


# Menambahkan tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2
print(tup3) # output: (1, 2, 3, 4, 5, 6)

