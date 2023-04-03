# Membuat sebuah list
my_list = ['apel', 'pisang', 'jeruk', 'mangga']

# Menampilkan list
print(my_list) # Output: ['apel', 'pisang', 'jeruk', 'mangga']

# Mengakses elemen di dalam list
print(my_list[0]) # Output: 'apel'
print(my_list[2]) # Output: 'jeruk'

# Menambahkan elemen baru ke dalam list
my_list.append('anggur')
# menambahkan elemen baru pada urutan tertentu  
my_list.insert(2,'singa')
print(my_list) # Output: ['apel', 'singa' 'pisang', 'jeruk', 'mangga', 'anggur']

# Menghapus elemen dari list
my_list.remove('pisang')
print(my_list) # Output: ['apel', 'jeruk', 'mangga', 'anggur']

#menghapus suatu element pada urutan tertentu
my_list.pop(0) # Output: ['singa' 'jeruk', 'mangga', 'anggur']
print(my_list)

my_list.sort()  # Mengurutkan list secara ascending
print(my_list)  # Output: ['anggur', 'jeruk', 'manga', 'singa']
my_list.sort(reverse=True)  # Mengurutkan list secara descending
print(my_list)  # Output: ['singa','mangga', 'jeruk', 'anggur']
