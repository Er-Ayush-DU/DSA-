class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def display(root):
        if root is None:
            return

        print(f"{root.data} -> ", end="")
        if root.left is not None:
            print(f"{root.left.data} ", end="")
        if root.right is not None:
            print(f"{root.right.data} ", end="")
        print()

        Node.display(root.left)
        Node.display(root.right)

    @staticmethod
    def preorder(root):
        if root is None:
            return
        print(root.data)
        Node.preorder(root.left)
        Node.preorder(root.right)

    @staticmethod
    def size(root):
        if root is None:
            return 0
        return 1 + Node.size(root.left) + Node.size(root.right)

    @staticmethod
    def max_val(root):
        if root is None:
            return float('-inf')
        max_left = Node.max_val(root.left)
        max_right = Node.max_val(root.right)
        return max(root.data, max_left, max_right)

    @staticmethod
    def height(root):
        if root is None:
            return -1  # Empty tree has height -1
        left_height = Node.height(root.left)
        right_height = Node.height(root.right)
        return max(left_height, right_height) + 1


# Main part
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    Node.display(root)
    print("\nPreorder Traversal:")
    Node.preorder(root)

    print("\nSize of the tree:", Node.size(root))
    print("Max value of the tree:", Node.max_val(root))
    print("Height of the tree:", Node.height(root))
