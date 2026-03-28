Program ini digunakan untuk merepresentasikan dan melakukan operasi aritmatika pada bilangan berukuran sangat besar (Big Integer) dengan menggunakan struktur data linked list. Hal ini dilakukan karena tipe data bawaan seperti int memiliki batasan kapasitas.

1. Struktur Node
class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None
Penjelasan:
Node adalah elemen dasar dari linked list
data menyimpan 1 digit angka
next menunjuk ke node berikutnya

 Jadi satu angka besar dipecah jadi digit-digit kecil

Contoh:

123 → 1 → 2 → 3
2. Class BigInteger
class BigInteger:

Class ini digunakan untuk:

Menyimpan angka besar
Melakukan operasi matematika
3. Constructor (Inisialisasi)
def __init__(self, number):
    self.head = None
    for digit in number:
        self.append(digit)
Penjelasan:
Menerima input berupa string angka
Setiap digit dimasukkan ke linked list
Menggunakan fungsi append()
4. Method append()
def append(self, digit):
Penjelasan:
Menambahkan digit ke akhir linked list
Jika kosong → jadi head
Jika tidak → ditambahkan di node terakhir
5. Method toString()
def toString(self):
Penjelasan:
Mengubah linked list kembali menjadi string angka
Digunakan untuk menampilkan hasil
6. Method size()
def size(self):
Penjelasan:
Menghitung jumlah digit dalam linked list
7. Operasi Penjumlahan (add)
def add(self, other):
Konsep:
Dilakukan dari belakang (digit terakhir)
Menggunakan carry
Alur:
Balik angka ([::-1])
Tambahkan digit per digit
Simpan sisa (carry)
Balik kembali hasilnya
8. Operasi Pengurangan (subtract)
def subtract(self, other):
Konsep:
Menggunakan borrow (pinjam)
Jika digit atas < bawah → pinjam dari depan
9. Operasi Perkalian (multiply)
def multiply(self, other):
Konsep:
Menggunakan metode perkalian bersusun
Setiap digit dikalikan satu per satu
Disimpan dalam array hasil
10. Operasi Pembagian (divide)
def divide(self, other):
Penjelasan:
Mengubah BigInteger menjadi int
Menggunakan pembagian biasa

⚠️ Catatan:

Ini bukan full linked list (masih sederhana)
Cocok untuk tugas dasar
11. Program Utama (Main)
if __name__ == "__main__":
Penjelasan:

Membuat dua objek BigInteger:

a = BigInteger("123456789123456789")
b = BigInteger("987654321")
Menampilkan:
Nilai awal
Hasil operasi:
Penjumlahan
Pengurangan
Perkalian
Pembagian
