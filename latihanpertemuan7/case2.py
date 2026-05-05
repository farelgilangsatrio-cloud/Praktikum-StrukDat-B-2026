# soal 1:
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array("Pasien D (Darurat)", 2)

print("Antrean Pasien:")
for pasien in antrean_array:
    print(pasien)

# soal 2:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def insert_at_position(self, nama_pasien, posisi):
        newNode = Node(nama_pasien)

        if posisi == 1:
            newNode.next = self.head
            self.head = newNode
            return

        current = self.head
        count = 1

        while current.next and count < posisi - 1:
            current = current.next
            count += 1
        newNode.next = current.next
        current.next = newNode

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

antrean = AntreanLinkedList()

antrean.append("Pasien A (Stabil)")
antrean.append("Pasien B (Stabil)")
antrean.append("Pasien C (Stabil)")

antrean.insert_at_position("Pasien D (Darurat)", 2)

print("Antrean Pasien:")
antrean.tampilkan()
