
class Node:
    def __init__(self, claim_id):
        self.claim_id = claim_id
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, claim_id):
        self.root = self._insert(self.root, claim_id)

    def _insert(self, root, claim_id):
        if root is None:
            return Node(claim_id)

        if claim_id < root.claim_id:
            root.left = self._insert(root.left, claim_id)

        elif claim_id > root.claim_id:
            root.right = self._insert(root.right, claim_id)

        return root

    def search(self, root, claim_id):
        if root is None:
            return False

        if root.claim_id == claim_id:
            return True

        if claim_id < root.claim_id:
            return self.search(root.left, claim_id)

        return self.search(root.right, claim_id)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.claim_id, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.claim_id, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.claim_id, end=" ")


claims = [105, 80, 130, 60, 95,
          120, 150, 55, 70, 90]

tree = BST()

for claim in claims:
    tree.insert(claim)

print("INSURANCE CLAIM BST")

print("\nSearch 120:",
      tree.search(tree.root, 120))

print("Search 999:",
      tree.search(tree.root, 999))

print("\nInorder Traversal:")
tree.inorder(tree.root)

print("\nPreorder Traversal:")
tree.preorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)

print("\n\nInorder traversal gives sorted claim IDs.")
