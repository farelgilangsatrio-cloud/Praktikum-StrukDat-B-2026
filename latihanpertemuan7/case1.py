# tugas 1 :
history_array = ["google.com", "python.org"]
def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)
    return history_array

tambah_pencarian_array("histori array")
print(history_array)

# tugas 2 :
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        newNode = Node(keyword)
        newNode.next = self.head
        self.head = newNode

    def tampilkan_history(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

history = HistoryLinkedList()

history.tambah_pencarian_linked("google.com")
history.tambah_pencarian_linked("python.org")
history.tambah_pencarian_linked("github.com")

print("Riwayat Pencarian:")
history.tampilkan_history()

