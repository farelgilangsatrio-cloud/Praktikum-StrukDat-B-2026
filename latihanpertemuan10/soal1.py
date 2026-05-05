'''
1. Simulasi Riwayat Navigasi Browser
Skenario: Bayangkan Anda adalah seorang Software Engineer yang ditugaskan
untuk membuat sistem "Riwayat Navigasi" (Browser History) sederhana. Setiap kali
pengguna mengunjungi halaman web baru, URL halaman tersebut akan ditumpuk.
Jika pengguna menekan tombol "Back", halaman terakhir akan dihapus dari riwayat
dan pengguna kembali ke halaman sebelumnya.
Sistem ini sangat cocok menggunakan struktur data Stack (LIFO - Last In First
Out).

Tugas Anda: Anda diminta untuk mengimplementasikan sistem ini menggunakan
dua cara yang berbeda:
1. Menggunakan List biasa (Dynamic Array) bawaan Python.
2. Menggunakan Linked List.
Kedua implementasi tersebut wajib memiliki 5 operasi dasar Stack berikut:
1. is_empty(): Memeriksa apakah riwayat kosong (mengembalikan True atau
False).
2. push(url): Menambahkan URL baru ke posisi teratas (pengguna membuka
halaman baru).
3. pop(): Menghapus dan mengembalikan URL di posisi teratas (pengguna
menekan tombol 'Back'). Jika kosong, kembalikan teks "Riwayat kosong".
4. peek(): Melihat URL yang ada di posisi teratas tanpa menghapusnya (melihat
halaman yang sedang aktif). Jika kosong, kembalikan None.
5. size(): Menghitung total URL yang tersimpan di dalam riwayat saat ini.

Instruksi Pengerjaan
Untuk mempermudah, lengkapilah kerangka kode (skeleton code) di bawah ini.
Tuliskan logika Anda pada bagian yang ditandai dengan komentar # Tulis kode di
sini.
Bagian 1: Implementasi Menggunakan List Biasa
class StackList:
def __init__(self):
self.items = [] # Menggunakan list bawaan Python
def is_empty(self):
# Tulis kode di sini
pass
def push(self, url):
# Tulis kode di sini (Petunjuk: gunakan append)
pass
def pop(self):
# Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
pass
def peek(self):
# Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
pass
def size(self):
# Tulis kode di sini (Petunjuk: gunakan len())
pass
Bagian 2: Implementasi Menggunakan Linked List
class Node:
def __init__(self, url):
self.url = url
self.next = None

class StackLinkedList:
def __init__(self):
self.top = None
self.count = 0 # Variabel bantuan untuk melacak ukuran
def is_empty(self):
# Tulis kode di sini (Petunjuk: periksa apakah top bernilai None)
pass
def push(self, url):
# Tulis kode di sini
# 1. Buat Node baru
# 2. Hubungkan 'next' node baru ke 'top' saat ini
# 3. Jadikan node baru sebagai 'top' yang baru
# 4. Tambahkan nilai 'count'
pass
def pop(self):
# Tulis kode di sini
# 1. Periksa is_empty()
# 2. Simpan url dari 'top' saat ini
# 3. Geser 'top' ke node berikutnya (top = top.next)
# 4. Kurangi nilai 'count'
# 5. Kembalikan url yang disimpan
pass
def peek(self):
# Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
pass
def size(self):
# Tulis kode di sini (Petunjuk: kembalikan nilai variabel 'count')
pass
'''
# Bagian 1
class Stack:
  def __init__(self):
    self.stack = []

  def push(self, url):
    self.stack.append(url)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

myStack = Stack()

myStack.push('www.google.com')
myStack.push('www.faceebook.com')

print(myStack.stack)
print(myStack.pop())
print(myStack.peek())
print(myStack.size())


# bagian 2
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, url):
    new_node = Node(url)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

Stack1 = Stack()
Stack1.push('www.intagram.com')
Stack1.push('www.youtube.com')


print(Stack1.pop())
print(Stack1.peek())
print(Stack1.stackSize())
