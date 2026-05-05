# Bagian B
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if not self.head:
            return

        temp = self.head
        while True:
            print(temp.nama, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke awal)")

    def delete_head(self):
        if not self.head:
            return
        temp = self.head
        if temp.next == self.head:
            self.head = None
            return
        last = self.head
        while last.next != self.head:
            last = last.next

        self.head = self.head.next
        last.next = self.head

antrian = CircularLinkedList()

antrian.insert_tail("Andi")
antrian.insert_tail("Budi")
antrian.insert_tail("Citra")
antrian.insert_tail("Dina")

print("Antrian awal:")
antrian.print_antrian()

antrian.insert_tail("Edo")
print("Setelah tambah Edo:")
antrian.print_antrian()

antrian.delete_head()
print("Setelah Andi dilayani:")
antrian.print_antrian()