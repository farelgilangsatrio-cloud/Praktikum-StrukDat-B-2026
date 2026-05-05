class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

def preorder(node):
    if node is not None:
        print(node.data, end=" - ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" - ")
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" - ")

def leaf_nodes(node):
    if node is not None:
        if node.left is None and node.right is None:
            print(node.data, end=", ")
        leaf_nodes(node.left)
        leaf_nodes(node.right)

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print()

tree = BinaryTree()

print("[INFO] Membangun Struktur Gudang...")

tree.insert_root("A")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "C")
tree.insert_left(tree.root.left, "D")
tree.insert_right(tree.root.left, "E")
tree.insert_right(tree.root.right, "F")

print("[INFO] Struktur berhasil dibuat")
print()

print("HASIL AUDIT:")

print("1. Pre-Order  : ", end="")
preorder(tree.root)
print("")

print("2. In-Order   : ", end="")
inorder(tree.root)
print("")

print("3. Post-Order : ", end="")
postorder(tree.root)
print("")
print()

print("[DATA] Gudang Ujung (Leaf Nodes): ", end="")
leaf_nodes(tree.root)
print("")

print("======================================")
print("Audit Selesai!")