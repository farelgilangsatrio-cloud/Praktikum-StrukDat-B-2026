class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new = Node(id_buku, judul)

        if self.root == None:
            self.root = new
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return
        
        P = self.root
        Q = self.root

        while Q != None and new.id != P.id:
            P = Q

            if new.id < P.id:
                Q = P.left
            else:
                Q = P.right

        if new.id == P.id:
            print("Data duplikat!")
            return
        
        if new.id < P.id:
            P.left = new
        else:
            P.right = new
        
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def search(self, id_buku):
        current = self.root

        while current is not None:
            if id_buku == current.id:
                return current
            elif id_buku < current.id:
                current = current.left
            else:
                current = current.right

        return None

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    def get_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def height(self, node):
        if node is None:
            return -1
        kiri = self.height(node.left)
        kanan = self.height(node.right)
        return max(kiri, kanan) + 1

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

bst = BinarySearchTree()

bst.insert(50, "Dasar Pemrograman")
bst.insert(30, "Struktur Data")
bst.insert(70, "Kecerdasan Buatan")
bst.insert(20, "Matematika Diskrit")
bst.insert(40, "Basis Data")
bst.insert(60, "Jaringan Komputer")
bst.insert(80, "Sistem Operasi")
print()

print("[INFO] Koleksi Buku (In-Order Traversal):")
bst.inorder(bst.root)
print()

print("[SEARCH] Mencari ID 60...", end="")
hasil = bst.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end="")
hasil = bst.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")
    print()

min_buku = bst.get_min()
max_buku = bst.get_max()

print(f"[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")

print(f"[INFO] Tinggi (Height) Tree: {bst.height(bst.root)}")

print("=========================================")
print("Simulasi Selesai!")