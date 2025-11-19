class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def inorder_traversal(self):
        result = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return result


if __name__ == "__main__":
    bst = BinarySearchTree()
    for number in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(number)

    print("Inorder traversal:", bst.inorder_traversal())
  
