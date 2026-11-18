
# Day 2 - Set 1 - Task 1
# Binary Search Tree for E-Commerce Product Categories

class Node:
    def __init__(self, category):
        self.category = category
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Insert a category into the BST
    def insert(self, category):
        self.root = self._insert(self.root, category)

    def _insert(self, root, category):
        if root is None:
            return Node(category)

        if category < root.category:
            root.left = self._insert(root.left, category)
        elif category > root.category:
            root.right = self._insert(root.right, category)

        return root

    # Search for a category
    def search(self, category):
        return self._search(self.root, category)

    def _search(self, root, category):
        if root is None:
            return False

        if root.category == category:
            return True
        elif category < root.category:
            return self._search(root.left, category)
        else:
            return self._search(root.right, category)

    # Inorder: Left, Root, Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.category, end=" | ")
            self.inorder(root.right)

    # Preorder: Root, Left, Right
    def preorder(self, root):
        if root:
            print(root.category, end=" | ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder: Left, Right, Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.category, end=" | ")


# Main program
bst = BinarySearchTree()

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Furniture",
    "Beauty",
    "Mobiles",
    "Laptops",
    "Shoes",
    "Home Decor",
    "Sports",
    "Toys",
    "Groceries",
    "Watches",
    "Accessories",
    "Kitchen"
]

print("E-COMMERCE PRODUCT CATEGORY BST")
print("-" * 45)

# Insert 15 categories
for category in categories:
    bst.insert(category)

print("\nTotal categories inserted:", len(categories))

# Search demonstration
search_category = "Mobiles"

print("\nSearching for:", search_category)

if bst.search(search_category):
    print("Result: Category found!")
else:
    print("Result: Category not found!")

# Traversals
print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\n\nPreorder Traversal:")
bst.preorder(bst.root)

print("\n\nPostorder Traversal:")
bst.postorder(bst.root)

print("\n\nBST execution completed.")
