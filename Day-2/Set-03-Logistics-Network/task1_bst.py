
class Node:
    def __init__(self, code):
        self.code = code
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, code):
        self.root = self._insert(self.root, code)

    def _insert(self, root, code):
        if root is None:
            return Node(code)

        if code < root.code:
            root.left = self._insert(root.left, code)

        elif code > root.code:
            root.right = self._insert(root.right, code)

        return root

    def search(self, code):
        current = self.root

        while current:
            if current.code == code:
                return True

            elif code < current.code:
                current = current.left

            else:
                current = current.right

        return False

    def height(self, root):
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)


def create_tree(values):
    tree = BST()

    for value in values:
        tree.insert(value)

    return tree


# Mixed insertion order
hubs = [
    "HUB-D", "HUB-B", "HUB-F",
    "HUB-A", "HUB-C", "HUB-E", "HUB-G"
]

tree = create_tree(hubs)

# Sorted insertion order
sorted_hubs = sorted(hubs)
sorted_tree = create_tree(sorted_hubs)

print("LOGISTICS HUB BST")

print("\nInsertion Order:")
print(hubs)

print("\nSearch HUB-E:")
print(tree.search("HUB-E"))

print("\nSearch HUB-Z:")
print(tree.search("HUB-Z"))

print("\nHeight of Mixed-Order BST:")
print(tree.height(tree.root))

print("\nSorted Insertion Order:")
print(sorted_hubs)

print("\nHeight of Sorted-Order BST:")
print(sorted_tree.height(sorted_tree.root))

print("\nConclusion:")
print("Sorted insertion can create a skewed BST.")
print("This increases the height and search time.")
