class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None

        removed = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama} (keluhan: {removed.keluhan})")
        return removed

    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}")

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        no = 1
        while current:
            print(f" {no}. {current.nama} → {current.keluhan}")
            current = current.next
            no += 1

print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================")
print()

antrian = Queue()

print("[CEK] apakah antrian kosong?", "ya, antrian masih kosong." if antrian.is_empty() else "TIDAK")
print()

antrian.enqueue("BUDI", "demam tinggi")
antrian.enqueue("ANI", "batuk pilek")
antrian.enqueue("CITRA", "sakit kepala")
print()

print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")
antrian.peek()
print()
antrian.dequeue()
antrian.enqueue("DODI", "nyeri perut")
print()

antrian.display()
print()
antrian.dequeue()
print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
print()
antrian.clear()

print("[CEK] Apakah antrian kosong?", "ya, antrian sudah kosong." if antrian.is_empty() else "TIDAK")
print()

print("====================================")
print(" Simulasi Selesai!")
print("====================================")
print()

